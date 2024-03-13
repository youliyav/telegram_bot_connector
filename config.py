from requests.auth import HTTPBasicAuth
from env import JIRA_TOKEN, JIRA_USER, JIRA_URL


class JiraAPIConfig:
    _config = None

    def __init__(self):

        self.JIRA_URL = JIRA_URL
        self.JIRA_USER = JIRA_USER
        self.JIRA_TOKEN = JIRA_TOKEN

        self.auth = HTTPBasicAuth(JIRA_USER, JIRA_TOKEN)

# config = JiraAPIConfig()
# print(config.JIRA_USER)


 



    



