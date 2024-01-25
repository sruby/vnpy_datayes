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
ORACLE_PASSWORD = os.getenv('ORACLE_PASSWORD')
ORACLE_DSN = os.getenv('ORACLE_DSN')

# 交易所映射
EXCHANGE_VT2TS: Dict[Exchange, str] = {
    Exchange.SSE: "XSHG",
    Exchange.SZSE: "XSHE",
}


# Class to handle the connection and querying from Oracle
# new subclass inherits from BaseDatafeed
class DatayesDatafeed(BaseDatafeed):
    def __init__(self):
        self.connection = None

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
        """Query bar history data from MKT_FUNDD or MKT_IDXD tables."""
        symbol = req.symbol
        exchange: Exchange = req.exchange
        interval: Interval = req.interval
        start_date = req.start.strftime("%Y-%m-%d")
        end_date = req.end.strftime("%Y-%m-%d")

        ts_exchange = EXCHANGE_VT2TS[exchange]

        # Determine the table based on symbol
        # This is a simple example; you might need more sophisticated logic
        if "IDX" in symbol:
            table_name = "F_DATAYES.MKT_IDXD"
            price_columns = "OPEN_INDEX, HIGHEST_INDEX, LOWEST_INDEX, CLOSE_INDEX"
        else:
            table_name = "F_DATAYES.MKT_FUNDD"
            price_columns = "OPEN_PRICE, HIGHEST_PRICE, LOWEST_PRICE, CLOSE_PRICE"

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
    if datafeed.connect():
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
