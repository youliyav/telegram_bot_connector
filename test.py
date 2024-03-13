import requests
from requests.auth import HTTPBasicAuth
from env import JIRA_TOKEN, JIRA_USER, JIRA_URL
import json


url = f"{JIRA_URL}/rest/api/3/search"

auth = HTTPBasicAuth(JIRA_USER, JIRA_TOKEN)

headers = {"Accept": "application/json"}

query = {'jql': 'project = JBK'}

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query,
   auth=auth
)

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


data = response.json()
print(data["total"])