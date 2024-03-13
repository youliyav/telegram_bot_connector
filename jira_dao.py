import requests
from config import JiraAPIConfig


class JiraDAO:
   def __init__(self):
      self.config = JiraAPIConfig()
      self.headers = {"Accept": "application/json"}

   def search_issues(self, query):
      url = f"{self.config.JIRA_URL}/rest/api/3/search"
      params = f"?jql=project={query}"

      response = requests.request(
         "GET",
         url,
         headers=self.headers,
         params=params,
         auth=self.config.auth
      )

      if response.status_code == 200:
         return response.json().get('total')
      else:
         raise Exception(f"Error {response.status_code}: {response.text}")



