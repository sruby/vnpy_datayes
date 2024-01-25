import unittest
import pandas as pd
from unittest.mock import patch
from datetime import datetime
from vnpy.trader.object import BarData, HistoryRequest
from vnpy.trader.constant import Interval
from vnpy.trader.datafeed import BaseDatafeed
from vnpy.trader.utility import round_to
from vnpy.trader.constant import Exchange
# from增加包名和文件名
from vnpy_datayes.datayes_datafeed import DatayesDatafeed, ASSET_CLASS_TABLE_MAPPING, EXCHANGE_VT2TS

class TestDatayesDatafeed(unittest.TestCase):

    def setUp(self):
        self.datafeed = DatayesDatafeed()

    def tearDown(self):
        self.datafeed.disconnect()

    def test_query_bar_history_fund(self):
        request = HistoryRequest(
            symbol="510300",
            exchange=Exchange.SSE,  # Replace with the appropriate vn.py Exchange enum
            interval=Interval.DAILY,
            start=datetime(2020, 1, 1),
            end=datetime(2020, 12, 31)
        )

        # Fetch the historical data
        bars = self.datafeed.query_bar_history(request)

        # Do something with the bars, like converting to a DataFrame
        df = pd.DataFrame([bar.__dict__ for bar in bars])

        # Print the DataFrame
        print(df)
    def test_query_bar_history_equd(self):
        request = HistoryRequest(
            symbol="000001",
            exchange=Exchange.SSE,  # Replace with the appropriate vn.py Exchange enum
            interval=Interval.DAILY,
            start=datetime(2020, 1, 1),
            end=datetime(2020, 12, 31)
        )

        # Fetch the historical data
        bars = self.datafeed.query_bar_history(request)

        # Do something with the bars, like converting to a DataFrame
        df = pd.DataFrame([bar.__dict__ for bar in bars])

        # Print the DataFrame
        print(df)

    def test_query_bar_history_inx(self):
        request = HistoryRequest(
            symbol="000300",
            exchange=Exchange.SSE,  # Replace with the appropriate vn.py Exchange enum
            interval=Interval.DAILY,
            start=datetime(2020, 1, 1),
            end=datetime(2020, 12, 31)
        )

        # Fetch the historical data
        bars = self.datafeed.query_bar_history(request)

        # Do something with the bars, like converting to a DataFrame
        df = pd.DataFrame([bar.__dict__ for bar in bars])

        # Print the DataFrame
        print(df)

if __name__ == "__main__":
    unittest.main()
