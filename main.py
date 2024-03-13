from jira_dao import JiraDAO


if __name__ == "__main__":
    jira_dao = JiraDAO()
    query="JBK"

    try:
        total = jira_dao.search_issues(query)
        print(f"Total issues: {total}")
    except Exception as e:
        print(f"Error: {e}")
              
    