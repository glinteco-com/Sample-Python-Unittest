import unittest
from unittest import mock
from libs.facebook_api import FacebookAPI
from libs.user import is_registered_user


class TestDatetimes(unittest.TestCase):
    @mock.patch.object(FacebookAPI, "get_userinfo")
    def test_is_registered_user_return_true(self, mock_get_userinfo):
        mock_get_userinfo.return_value  = {"userid": 1}

        result = is_registered_user("joe")

        self.assertTrue(result)

    @mock.patch.object(FacebookAPI, "get_userinfo")
    def test_is_registered_user_return_false(self, mock_get_userinfo):
        mock_get_userinfo.return_value  = {}

        result = is_registered_user("joe")

        self.assertFalse(result)
