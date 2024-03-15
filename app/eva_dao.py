import requests
from config import EvaAPIConfig


class EvaDAO:
    """
    Класс для взаимодействия с Eva REST API.
    """

    def __init__(self):
        """
        Инициализирует экземпляр класса с уже загруженной конфигурацией 
        из файла .env и заголовками запроса.
        """
        self.config = EvaAPIConfig()
        self.headers = {"Accept": "application/json"}


    def get_tasks(self):
        # Логика для получения задач из EVA
        pass
