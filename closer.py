from configparser import ConfigParser

class Closer():
    def __init__(self):
        with open('closer.cfg', 'r') as fin:
            print(fin.read())
            print(type(fin.read()))
        self.config = ConfigParser()
        self.config.read('closer.cfg')
        print(self.config.items('jira'))
        self.jira_url = self.config.get('jira','url')
