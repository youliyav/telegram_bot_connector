"""
   Класс для взаимодействия с Jira REST API.
"""

import requests
from config import config
from requests.auth import HTTPBasicAuth


class JiraDAO:
    def search_issues(self, query):
      """
      Отправляет GET-запрос к API Jira.

      Args --> query (str): Поиск issue по заданному запросу JQL.
      Returns --> int: Общее количество найденных issue.
      Raises --> Exception: Если код ответа сервера не равен 200.
      """

      url = f"{config.JIRA_URL}/rest/api/3/search"

      headers = {"Accept": "application/json"}

      params = f"?jql=project={query}"      # --> 5 (из всех проектов)

      response = requests.get(url, headers=headers, params=params, auth=config.JIRA_AUTH)

      if response.status_code == 200:
         return response.json()
      else:
         raise Exception(f"Error {response.status_code}: {response.text}")


jira_dao = JiraDAO()
# res = jira_dao.search_issues("JBK")


