import unittest
import datetime

from libs.datetimes import is_weekend, is_weekday


class TestDatetimes(unittest.TestCase):
    def test_is_weekday_return_true(self):
        today = datetime.datetime(2023, 2, 16)
        self.assertTrue(is_weekday(today))

    def test_is_weekday_return_false(self):
        today = datetime.datetime(2023, 2, 18)
        self.assertFalse(is_weekday(today))

    def test_is_weekend_return_true(self):
        today = datetime.datetime(2023, 2, 18)
        self.assertTrue(is_weekend(today))

    def test_is_weekend_return_false(self):
        today = datetime.datetime(2023, 2, 16)
        self.assertFalse(is_weekend(today))
