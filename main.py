"""
1. Добавить FastAPI
2. Добавить валидацию данных с Pydantic
3. Создать модели чтения, добавления, удаления задач
.. Создать endpoints для работы с моделями
4. Добавить Алхимию
5. Привязать к ней БД (postgres)
6. Залить тестовые данные
7. Вывести их в телеграм бот
8. Создать связь Jira и БД через api
"""

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
@app.get("/")


class STaskAdd(BaseModel):
    name: str
    description: Union[str, None] = None

@app.post("/")
async def add_task(task: STaskAdd):
    return {"data": task}
