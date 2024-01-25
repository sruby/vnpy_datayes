Midify the Code, First. Get ASSET_CLASS by TICKER_SYMBOL and EXCHANGE_CD, and then get data from table according to ASSET_CLASS, Final put data into bar.
- ASSET_CLASS dict :B债券CBBC牛熊证CD信用衍生品CP数字货币E股票F基金FEX外汇FP理财产品（私募）FU期货GDR全球存托凭证IDX指数IR市场利率O其他OP期权PE优先股REPO债券回购SPOT现货W权证.
- map of ASSET_CLASS and table:
| ASSET_CLASS | table |
| --- | --- |
| IDX | F_DATAYES.mkt_idxd |
| F | F_DATAYES.mkt_fundd |
| E | F_DATAYES.mkt_equd |
- table defined in F_DATAYES.mkt_idxd F_DATAYES.mkt_fundd F_DATAYES.mkt_equd
```sql
-- auto-generated definition
create table MKT_EQUD
(
    ID                  NUMBER(19) not null
        constraint PK_MKT_EQUD_1
            primary key,
    SECURITY_ID         NUMBER(19),
    TICKER_SYMBOL       VARCHAR2(60),
    EXCHANGE_CD         VARCHAR2(8),
    TRADE_DATE          DATE,
    PRE_CLOSE_PRICE     NUMBER(9, 3),
    ACT_PRE_CLOSE_PRICE NUMBER(9, 3),
    OPEN_PRICE          NUMBER(9, 3),
    HIGHEST_PRICE       NUMBER(9, 3),
    LOWEST_PRICE        NUMBER(9, 3),
    CLOSE_PRICE         NUMBER(9, 3),
    TURNOVER_VOL        NUMBER(20),
    TURNOVER_VALUE      NUMBER(20, 3),
    DEAL_AMOUNT         NUMBER(10),
    PE                  NUMBER(19, 4),
    PE1                 NUMBER(19, 4),
    PB                  NUMBER(19, 4),
    NEG_MARKET_VALUE    NUMBER(19, 4),
    MARKET_VALUE        NUMBER(19, 4),
    CHG_PCT             NUMBER(19, 4),
    TURNOVER_RATE       NUMBER(19, 4),
    UPDATE_TIME         TIMESTAMP(6),
    TMSTAMP             NUMBER(19)
)
/

comment on table MKT_EQUD is 'null'
/

comment on column MKT_EQUD.ID is '自增ID'
/

comment on column MKT_EQUD.SECURITY_ID is '证券内部ID'
/

comment on column MKT_EQUD.TICKER_SYMBOL is '证券代码'
/

comment on column MKT_EQUD.EXCHANGE_CD is '交易市场代码'
/

comment on column MKT_EQUD.TRADE_DATE is '交易日'
/

comment on column MKT_EQUD.PRE_CLOSE_PRICE is '昨收盘'
/

comment on column MKT_EQUD.ACT_PRE_CLOSE_PRICE is '实际昨收盘'
/

comment on column MKT_EQUD.OPEN_PRICE is '今开盘'
/

comment on column MKT_EQUD.HIGHEST_PRICE is '最高价'
/

comment on column MKT_EQUD.LOWEST_PRICE is '最低价'
/

comment on column MKT_EQUD.CLOSE_PRICE is '今收盘'
/

comment on column MKT_EQUD.TURNOVER_VOL is '成交量'
/

comment on column MKT_EQUD.TURNOVER_VALUE is '成交金额'
/

comment on column MKT_EQUD.DEAL_AMOUNT is '成交笔数'
/

comment on column MKT_EQUD.PE is '市盈率TTM'
/

comment on column MKT_EQUD.PE1 is '动态市盈率'
/

comment on column MKT_EQUD.PB is '市净率'
/

comment on column MKT_EQUD.NEG_MARKET_VALUE is '流通市值'
/

comment on column MKT_EQUD.MARKET_VALUE is '总市值'
/

comment on column MKT_EQUD.CHG_PCT is '涨跌幅'
/

comment on column MKT_EQUD.TURNOVER_RATE is '日换手率'
/

comment on column MKT_EQUD.UPDATE_TIME is '更新时间'
/

comment on column MKT_EQUD.TMSTAMP is '时间戳'
/

create index IDX_MKT_EQUD1
    on MKT_EQUD (SECURITY_ID, TRADE_DATE)
/

create index IDX_MKT_EQUD2
    on MKT_EQUD (TICKER_SYMBOL, TRADE_DATE)
/

create index IDX_MKT_EQUD3
    on MKT_EQUD (TRADE_DATE)
/

create index IDX_MKT_EQUD4
    on MKT_EQUD (UPDATE_TIME)
/

-- auto-generated definition
create table MKT_FUNDD
(
    ID              NUMBER(19) not null
        constraint PK_MKT_FUNDD_1
            primary key,
    SECURITY_ID     NUMBER(19),
    TICKER_SYMBOL   VARCHAR2(90),
    SEC_SHORT_NAME  VARCHAR2(150),
    EXCHANGE_CD     VARCHAR2(8),
    TRADE_DATE      DATE,
    PRE_CLOSE_PRICE NUMBER(18, 4),
    OPEN_PRICE      NUMBER(18, 4),
    HIGHEST_PRICE   NUMBER(18, 4),
    LOWEST_PRICE    NUMBER(18, 4),
    CLOSE_PRICE     NUMBER(18, 4),
    CHG             NUMBER(18, 4),
    CHG_PCT         NUMBER(18, 4),
    TURNOVER_VOL    NUMBER(20),
    TURNOVER_VALUE  NUMBER(17, 3),
    DISCOUNT        NUMBER(18, 4),
    DISCOUNT_RATIO  NUMBER(18, 6),
    UPDATE_TIME     TIMESTAMP(6)
)
/

comment on table MKT_FUNDD is 'null'
/

comment on column MKT_FUNDD.ID is '信息编码'
/

comment on column MKT_FUNDD.SECURITY_ID is '证券内部ID'
/

comment on column MKT_FUNDD.TICKER_SYMBOL is '交易代码'
/

comment on column MKT_FUNDD.SEC_SHORT_NAME is '基金简称'
/

comment on column MKT_FUNDD.EXCHANGE_CD is '交易所代码'
/

comment on column MKT_FUNDD.TRADE_DATE is '交易日期'
/

comment on column MKT_FUNDD.PRE_CLOSE_PRICE is '昨收盘'
/

comment on column MKT_FUNDD.OPEN_PRICE is '今开盘'
/

comment on column MKT_FUNDD.HIGHEST_PRICE is '最高价'
/

comment on column MKT_FUNDD.LOWEST_PRICE is '最低价'
/

comment on column MKT_FUNDD.CLOSE_PRICE is '收盘价'
/

comment on column MKT_FUNDD.CHG is '涨跌'
/

comment on column MKT_FUNDD.CHG_PCT is '涨跌幅'
/

comment on column MKT_FUNDD.TURNOVER_VOL is '成交量'
/

comment on column MKT_FUNDD.TURNOVER_VALUE is '成交金额'
/

comment on column MKT_FUNDD.DISCOUNT is '贴水'
/

comment on column MKT_FUNDD.DISCOUNT_RATIO is '贴水率'
/

comment on column MKT_FUNDD.UPDATE_TIME is '更新时间'
/

create index IDX_MKT_FUNDD1
    on MKT_FUNDD (SECURITY_ID, TRADE_DATE)
/

create index IDX_MKT_FUNDD2
    on MKT_FUNDD (TICKER_SYMBOL, TRADE_DATE)
/

create index IDX_MKT_FUNDD3
    on MKT_FUNDD (TRADE_DATE, SECURITY_ID)
/

create index IDX_MKT_FUNDD4
    on MKT_FUNDD (UPDATE_TIME)
/

-- auto-generated definition
create table MKT_IDXD
(
    ID              NUMBER(19) not null
        constraint PK_MKT_IDXD_1
            primary key,
    INDEX_ID        NUMBER(19),
    TICKER_SYMBOL   VARCHAR2(90),
    EXCHANGE_CD     VARCHAR2(8),
    TRADE_DATE      DATE,
    PRE_CLOSE_INDEX NUMBER(11, 5),
    OPEN_INDEX      NUMBER(11, 5),
    HIGHEST_INDEX   NUMBER(11, 5),
    LOWEST_INDEX    NUMBER(11, 5),
    CLOSE_INDEX     NUMBER(11, 5),
    TURNOVER_VALUE  NUMBER(24, 4),
    TURNOVER_VOL    NUMBER(19, 2),
    CHG             NUMBER(19, 5),
    CHG_PCT         NUMBER(20, 6),
    UPDATE_TIME     TIMESTAMP(6)
)
/

comment on table MKT_IDXD is '指数日行情'
/

comment on column MKT_IDXD.ID is '信息编码'
/

comment on column MKT_IDXD.INDEX_ID is '证券内部ID'
/

comment on column MKT_IDXD.TICKER_SYMBOL is '交易代码'
/

comment on column MKT_IDXD.EXCHANGE_CD is '交易市场代码'
/

comment on column MKT_IDXD.TRADE_DATE is '交易日期'
/

comment on column MKT_IDXD.PRE_CLOSE_INDEX is '昨收盘价'
/

comment on column MKT_IDXD.OPEN_INDEX is '开盘价'
/

comment on column MKT_IDXD.HIGHEST_INDEX is '最高价'
/

comment on column MKT_IDXD.LOWEST_INDEX is '最低价'
/

comment on column MKT_IDXD.CLOSE_INDEX is '收盘价'
/

comment on column MKT_IDXD.TURNOVER_VALUE is '成交金额'
/

comment on column MKT_IDXD.TURNOVER_VOL is '成交量'
/

comment on column MKT_IDXD.CHG is '涨跌'
/

comment on column MKT_IDXD.CHG_PCT is '涨跌幅'
/

comment on column MKT_IDXD.UPDATE_TIME is '更新时间'
/

create index IDX_MKT_IDXD5
    on MKT_IDXD (UPDATE_TIME)
/

create index IDX_MKT_IDXD4
    on MKT_IDXD (TRADE_DATE)
/

create index IDX_MKT_IDXD3
    on MKT_IDXD (TICKER_SYMBOL, TRADE_DATE)
/

create index IDX_MKT_IDXD1
    on MKT_IDXD (INDEX_ID, TRADE_DATE)
/



```

Code:
```python
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
        """Query bar history data from MKT_FUNDD or MKT_IDXD tables."""
        symbol = req.symbol
        exchange: Exchange = req.exchange
        interval: Interval = req.interval
        start_date = req.start.strftime("%Y-%m-%d")
        end_date = req.end.strftime("%Y-%m-%d")

        ts_exchange = EXCHANGE_VT2TS[exchange]

        # 查询证券主表获取资产类别
        # Execute the query
        cursor_security = self.connection.cursor()
        query_security = f"""
            select ASSET_CLASS from F_DATAYES.md_security WHERE TICKER_SYMBOL = :symbol AND EXCHANGE_CD = :exchange
        """
        cursor_security.execute(query_security, symbol=symbol, exchange=ts_exchange)
        records_security = cursor_security.fetchall()

        # Determine the table based on symbol
        # This is a simple example; you might need more sophisticated logic
        table_name = "F_DATAYES.MKT_IDXD"
        price_columns = "OPEN_INDEX OPEN_PRICE, HIGHEST_INDEX HIGHEST_PRICE, LOWEST_INDEX LOWEST_PRICE, CLOSE_INDEX CLOSE_PRICE"

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

```




