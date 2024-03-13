# Telegram Bot Connector for JIRA, Eva, and Bitrix

Этот проект представляет собой основу для будущего Telegram бота-коннектора, который будет интегрироваться с JIRA, Eva и Bitrix для агрегации данных о задачах. Используется паттерн DAO (Data Access Object) на языке Python 3 для подключения к JIRA REST API.

## Структура проекта
Проект включает следующие ключевые файлы:

- `config.py`: Управление конфигурацией подключения к JIRA, включает URL, имя пользователя и токен.
- `jira_dao.py`: Класс `JiraDAO`, реализующий взаимодействие с JIRA REST API для поиска задач.
- `main.py`: Пример использования `JiraDAO` для поиска задач в JIRA и вывода их количества.

### config.py
Файл `config.py` содержит класс `JiraAPIConfig`, загружающий конфигурационные данные из `env.py`.

### jira_dao.py
В `jira_dao.py` находится класс `JiraDAO`, который использует JIRA REST API для поиска задач. Подробнее о API см. [здесь](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search#api-rest-api-3-search-get).

### main.py
Файл `main.py` демонстрирует использование `JiraDAO` для выполнения JQL запросов в JIRA.

## Планы на будущее
- Интеграция с EVA и Bitrix.
- Разработка Telegram бота для удобного доступа к агрегированным данным о задачах.

## Как использовать
Для работы проекта установите зависимости из `requirements.txt` и настройте `env.py` с данными для подключения к JIRA.

Пример `env.py`:
```python
JIRA_URL="https://your-domain.atlassian.net"
JIRA_USER="email@example.com"
JIRA_TOKEN="<api_token>"
```
