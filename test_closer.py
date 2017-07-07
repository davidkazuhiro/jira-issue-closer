from closer import Closer
from unittest import TestCase
from unittest.mock import patch
from configparser import ConfigParser

class TestCloser(TestCase):
    def setUp(self):
        self.config_filename = 'test.cfg'
        self.config = ConfigParser()

    def write_config(self):
        with open(self.config_filename, 'w') as configfile:
            self.config.write(configfile)

    def test_config_basic(self):
        self.config['jira'] = {'url': 'https://jira.test.com'}
        self.write_config()
        closer = Closer(self.config_filename)
        self.assertEqual(closer.jira_url, 'https://jira.test.com')
