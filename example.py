import requests
from requests.auth import HTTPBasicAuth
from app.config import config
import json


url = f"{config.JIRA_URL}/rest/api/3/search"

auth = HTTPBasicAuth(config.JIRA_USER, config.JIRA_TOKEN)

headers = {"Accept": "application/json"}

query = {'jql': 'project = JBK'}
# query = {"jql": f"project={query}"}    # --> 3 issue из проекта JBK 
# params = f"?jql=project={query}"      # --> 5 из всех проектов


response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query,
   auth=config.JIRA_AUTH
)


data = response.json()
print(data["total"])

# print(response.json().get('total'))
# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
