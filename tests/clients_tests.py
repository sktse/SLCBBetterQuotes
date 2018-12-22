import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../SLCBBetterQuotes/lib"))  # Manually import

from unittest import TestCase
from mock import MagicMock

from clients import QuotesClient


class QuotesClientTests(TestCase):
    def setUp(self):
        self.mock_parent = MagicMock()
        self.mock_parent.GetRequest.return_value = "Ah Ah Ah. You didn't say the magic word."

        self.client = QuotesClient(
            parent=self.mock_parent,
            read_only_key="ShakenNotStirred",
            admin_key="ICouldaBeenAContender",
        )

    def test_get_quote__with_no_query__makes_api_call(self):
        result = self.client.get_quote()
        self.mock_parent.GetRequest.assert_called_once_with(
            "https://twitch.center/customapi/quote?token=ShakenNotStirred&data=",
            {},
        )
        self.assertEqual(result, "Ah Ah Ah. You didn't say the magic word.")

    def test_add_quote__makes_api_call(self):
        result = self.client.add_quote("The ratio of people to cake is too big.")
        expected_url = "https://twitch.center/customapi/addquote?token=ICouldaBeenAContender" \
                       "&data=The%20ratio%20of%20people%20to%20cake%20is%20too%20big."
        self.mock_parent.GetRequest.assert_called_once_with(expected_url, {})
        self.assertEqual(result, "Ah Ah Ah. You didn't say the magic word.")

    def test_delete_quote__makes_api_call(self):
        result = self.client.delete_quote("\"Deserve's got nothin' to do with it\"")
        expected_url = "https://twitch.center/customapi/delquote?token=ICouldaBeenAContender" \
                       "&data=%22Deserve%27s%20got%20nothin%27%20to%20do%20with%20it%22"
        self.mock_parent.GetRequest.assert_called_once_with(expected_url, {})
        self.assertEqual(result, "Ah Ah Ah. You didn't say the magic word.")

    def test_list_quotes__makes_api_call(self):
        result = self.client.list_quotes()
        self.mock_parent.GetRequest.assert_called_once_with(
            "https://twitch.center/customapi/quote/list?token=ShakenNotStirred",
            {},
        )
        self.assertEqual(result, "Ah Ah Ah. You didn't say the magic word.")
