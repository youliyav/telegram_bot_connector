from jira_dao import jira_dao


class TaskService:
    def get_total_issues_jira(self, query="JBK"):
        try:
            resp_json = jira_dao.search_issues(query)
            return resp_json.get('total')
        except Exception as e:
            print(f"Error: {e}")
            return None

service = TaskService()
# print(service.get_total_issues_jira())

