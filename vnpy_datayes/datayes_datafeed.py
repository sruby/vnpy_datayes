import cx_Oracle  # 安装的时候使用cx-Oracle搜索
import pandas as pd
import pyarrow
from dotenv import load_dotenv
import os
from datetime import datetime
from typing import Dict, List, Optional, Callable
from vnpy.trader.constant import Interval
from vnpy.trader.datafeed import BaseDatafeed
from vnpy.trader.object import BarData, HistoryRequest
from vnpy.trader.utility import round_to
from vnpy.trader.constant import Exchange, Interval

# Constants for the Oracle connection - replace with your actual credentials
# Retrieve the Oracle credentials from environment variables
load_dotenv()  # This is the crucial part
ORACLE_USERNAME = os.getenv('ORACLE_USERNAME')
if not ORACLE_USERNAME:
    # Get the home directory path
    home_dir = os.getenv('USERPROFILE')
    # Construct the path to the .env file
    env_path = os.path.join(home_dir, '.env')
    load_dotenv(env_path)
    ORACLE_USERNAME = os.getenv('ORACLE_USERNAME')
    if not ORACLE_USERNAME:
        print("No Oracle username found in environment variables")
ORACLE_PASSWORD = os.getenv('ORACLE_PASSWORD')
ORACLE_DSN = os.getenv('ORACLE_DSN')

# 交易所映射
EXCHANGE_VT2TS: Dict[Exchange, str] = {
    Exchange.SSE: "XSHG",
    Exchange.SZSE: "XSHE",
}

# Mapping of ASSET_CLASS to its corresponding table and price columns
ASSET_CLASS_TABLE_MAPPING = {
    "IDX": ("F_DATAYES.mkt_idxd", "OPEN_INDEX OPEN_PRICE, HIGHEST_INDEX HIGHEST_PRICE, LOWEST_INDEX LOWEST_PRICE, CLOSE_INDEX CLOSE_PRICE"),
    "F": ("F_DATAYES.mkt_fundd", "OPEN_PRICE, HIGHEST_PRICE, LOWEST_PRICE, CLOSE_PRICE"),
    "E": ("F_DATAYES.mkt_equd", "OPEN_PRICE, HIGHEST_PRICE, LOWEST_PRICE, CLOSE_PRICE")
}


# Class to handle the connection and querying from Oracle
# new subclass inherits from BaseDatafeed
class DatayesDatafeed(BaseDatafeed):
    def __init__(self):
        self.connect()

    def __del__(self):
        """Disconnect from the database when the object is destroyed."""
        self.disconnect()

    def connect(self):
        """Establish a connection to the Oracle database."""
        try:
            self.connection = cx_Oracle.connect(
                ORACLE_USERNAME,
                ORACLE_PASSWORD,
                ORACLE_DSN
            )
        except cx_Oracle.DatabaseError as e:
            print(f"An error occurred connecting to Oracle: {e}")
            return False
        return True

    def disconnect(self):
        """Disconnect from the Oracle database."""
        if self.connection:
            self.connection.close()
            self.connection = None

    def query_bar_history(self, req: HistoryRequest, output: Callable = print) -> Optional[List[BarData]]:
        """Query bar history data from different tables based on asset class."""
        symbol = req.symbol
        exchange: Exchange = req.exchange
        interval: Interval = req.interval
        start_date = req.start.strftime("%Y-%m-%d")
        end_date = req.end.strftime("%Y-%m-%d")

        ts_exchange = EXCHANGE_VT2TS.get(exchange, exchange.value)

        # Get the asset class of the security
        cursor_security = self.connection.cursor()
        query_security = """
            SELECT ASSET_CLASS FROM F_DATAYES.MD_SECURITY WHERE TICKER_SYMBOL = :symbol AND EXCHANGE_CD = :exchange
        """
        cursor_security.execute(query_security, symbol=symbol, exchange=ts_exchange)
        asset_class_record = cursor_security.fetchone()
        cursor_security.close()

        if asset_class_record:
            asset_class = asset_class_record[0]
        else:
            output(f"No asset class found for symbol {symbol} on exchange {exchange}")
            return None

        # Get the table and column information based on asset class
        table_info = ASSET_CLASS_TABLE_MAPPING.get(asset_class)
        if not table_info:
            output(f"No table mapping found for asset class {asset_class}")
            return None
        table_name, price_columns = table_info

        # Construct the query
        query = f"""
            SELECT TRADE_DATE, {price_columns}, TURNOVER_VOL, TURNOVER_VALUE, CHG, CHG_PCT
            FROM {table_name}
            WHERE TICKER_SYMBOL = :symbol AND EXCHANGE_CD = :exchange
            AND TRADE_DATE BETWEEN TO_DATE(:start_date, 'YYYY-MM-DD') AND TO_DATE(:end_date, 'YYYY-MM-DD')
            ORDER BY TRADE_DATE
        """

        # Execute the query
        cursor = self.connection.cursor()
        cursor.execute(query, symbol=symbol, exchange=ts_exchange, start_date=start_date, end_date=end_date)
        records = cursor.fetchall()
        cursor.close()

        # Process the records into BarData objects
        bars = []
        for record in records:
            trade_date, open_price, high_price, low_price, close_price, volume, turnover, change, change_pct = record
            bar = BarData(
                symbol=symbol,
                exchange=exchange,
                interval=interval,
                datetime=trade_date,  # Adjust if necessary to match the datetime format used by vn.py
                open_price=float(open_price),
                high_price=float(high_price),
                low_price=float(low_price),
                close_price=float(close_price),
                volume=int(volume),
                turnover=float(turnover),
                gateway_name="ORACLE"
            )
            bars.append(bar)

        return bars


# Usage example
if __name__ == "__main__":
    # Create a data feed instance and connect to Oracle
    datafeed = DatayesDatafeed()
    # if datafeed.connect():
    # Create a request for historical data

    request = HistoryRequest(
        symbol="510300",
        exchange=Exchange.SSE,  # Replace with the appropriate vn.py Exchange enum
        interval=Interval.DAILY,
        start=datetime(2020, 1, 1),
        end=datetime(2020, 12, 31)
    )

    # Fetch the historical data
    bars = datafeed.query_bar_history(request)

    # Do something with the bars, like converting to a DataFrame
    df = pd.DataFrame([bar.__dict__ for bar in bars])

    # Disconnect from the database
    datafeed.disconnect()

    # Print the DataFrame
    print(df)
