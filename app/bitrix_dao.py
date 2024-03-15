import requests
from config import BitrixAPIConfig


class BitrixDAO:
    """
    Класс для взаимодействия с Bitrix REST API.
    """

    def __init__(self):
        """
        Инициализирует экземпляр класса с уже загруженной конфигурацией 
        из файла .env и заголовками запроса.
        """
        self.config = BitrixAPIConfig()
        self.headers = {"Accept": "application/json"}


    def get_tasks(self):
        # Логика для получения задач из Bitrix
        pass
