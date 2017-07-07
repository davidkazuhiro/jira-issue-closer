from configparser import ConfigParser

class Closer():
    def __init__(self, config_path):
        self.config = ConfigParser()
        self.config.read(config_path)
        self.jira_url = self.config.get('jira','url')
