from closer import Closer
from unittest import TestCase
from unittest.mock import mock_open, patch

class TestCloser(TestCase):
    SAMPLE_CFG = "[jira]\nurl = https://jira.test.com\n"
    @patch('builtins.open', mock_open(read_data=SAMPLE_CFG))
    def test_config_basic(self):
        closer = Closer()
        self.assertEqual(closer.jira_url, 'https://jira.test.com')
