import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../SLCBBetterQuotes/lib"))  # Manually import

from unittest import TestCase
from mock import MagicMock

from managers import CommandManager


class CommandManagerTests(TestCase):
    def setUp(self):
        self.mock_client = MagicMock()
        self.mock_data = MagicMock()
        self.mock_parent = MagicMock()
        self.mock_parent.HasPermission.return_value = True

        self.mock_settings = MagicMock()

        self.manager = CommandManager(
            parent=self.mock_parent,
            client=self.mock_client,
            script_settings=self.mock_settings,
        )

    def test_execute__with_quote_command_and_params__calls_client(self):
        mock_data_values = [
            "!quote",
            "Sir",
            "Isaac",
            "Brock",
            "is",
            "the",
            "best",
            "Brock!"
        ]
        self.mock_data.GetParam.side_effect = mock_data_values
        self.mock_data.GetParamCount.return_value = len(mock_data_values)

        self.manager.execute(data=self.mock_data)

        self.mock_client.get_quote.assert_called_once_with(
            query="Sir Isaac Brock is the best Brock!"
        )

    def test_execute__with_quote_command_and_no_permission__calls_client(self):
        mock_data_values = [
            "!quote",
            "Sir",
            "Isaac",
            "Brock",
            "is",
            "the",
            "best",
            "Brock!"
        ]
        self.mock_data.GetParam.side_effect = mock_data_values
        self.mock_data.GetParamCount.return_value = len(mock_data_values)

        self.mock_parent.HasPermission.return_value = False

        self.manager.execute(data=self.mock_data)

        self.mock_client.get_quote.assert_not_called()

    def test_execute__with_quote_command_and_no_params__calls_client(self):
        mock_data_values = [
            "!quote",
        ]
        self.mock_data.GetParam.side_effect = mock_data_values
        self.mock_data.GetParamCount.return_value = len(mock_data_values)

        self.manager.execute(data=self.mock_data)

        self.mock_client.get_quote.assert_called_once_with(
            query=""
        )

    def test_execute__with_add_quote_command_and_params__calls_client(self):
        mock_data_values = [
            "!addquote",
            "\"Soylent",
            "Green",
            "is",
            "people!\"",
        ]
        self.mock_data.GetParam.side_effect = mock_data_values
        self.mock_data.GetParamCount.return_value = len(mock_data_values)

        self.manager.execute(data=self.mock_data)

        self.mock_client.add_quote.assert_called_once_with(
            query="\"Soylent Green is people!\""
        )

    def test_execute__with_add_quote_command_and_no_permissions__calls_client(self):
        mock_data_values = [
            "!addquote",
            "\"Soylent",
            "Green",
            "is",
            "people!\"",
        ]
        self.mock_data.GetParam.side_effect = mock_data_values
        self.mock_data.GetParamCount.return_value = len(mock_data_values)
        self.mock_parent.HasPermission.return_value = False

        self.manager.execute(data=self.mock_data)

        self.mock_client.add_quote.assert_not_called()

    def test_execute__with_delete_quote_command_and_params__calls_client(self):
        mock_data_values = [
            "!delquote",
            "\"Look",
            "at",
            "what",
            "they",
            "make",
            "you",
            "give.\"",
        ]
        self.mock_data.GetParam.side_effect = mock_data_values
        self.mock_data.GetParamCount.return_value = len(mock_data_values)

        self.manager.execute(data=self.mock_data)

        self.mock_client.delete_quote.assert_called_once_with(
            query="\"Look at what they make you give.\""
        )

    def test_execute__with_delete_quote_command_and_no_permission__calls_client(self):
        mock_data_values = [
            "!delquote",
            "\"Look",
            "at",
            "what",
            "they",
            "make",
            "you",
            "give.\"",
        ]
        self.mock_data.GetParam.side_effect = mock_data_values
        self.mock_data.GetParamCount.return_value = len(mock_data_values)
        self.mock_parent.HasPermission.return_value = False

        self.manager.execute(data=self.mock_data)

        self.mock_client.delete_quote.assert_not_called()

    def test_execute__with_list_quote_command__calls_client(self):
        mock_data_values = [
            "!listquote",
        ]

        self.mock_data.GetParam.side_effect = mock_data_values
        self.mock_data.GetParamCount.return_value = len(mock_data_values)

        self.manager.execute(data=self.mock_data)

        self.mock_client.list_quotes.assert_called_once_with()

    def test_execute__with_list_quote_command_and_no_permission__calls_client(self):
        mock_data_values = [
            "!listquote",
        ]

        self.mock_data.GetParam.side_effect = mock_data_values
        self.mock_data.GetParamCount.return_value = len(mock_data_values)
        self.mock_parent.HasPermission.return_value = False

        self.manager.execute(data=self.mock_data)

        self.mock_client.list_quotes.assert_not_called()

    def test_execute__with_not_command__does_not_call_client(self):
        mock_data_values = [
            "Admiral,",
            "there",
            "be",
            "whales",
            "here!",
        ]

        self.mock_data.GetParam.side_effect = mock_data_values
        self.mock_data.GetParamCount.return_value = len(mock_data_values)

        self.manager.execute(data=self.mock_data)

        self.mock_client.get_quote.assert_not_called()
        self.mock_client.add_quote.assert_not_called()
        self.mock_client.delete_quote.assert_not_called()
        self.mock_client.list_quotes.assert_not_called()
