"""
Хранит конфигурационные данные (API токены, URL и т.д.)
"""
from requests.auth import HTTPBasicAuth
from pydantic_settings import BaseSettings, SettingsConfigDict 



class JiraAPIConfig(BaseSettings):
    """
    Класс для управления конфигурацией подключения к Jira REST API
    """
    model_config = SettingsConfigDict(env_file=".env") 


    JIRA_URL: str = ""
    JIRA_USER: str = ""
    JIRA_TOKEN: str = ""
    TELEGRAM_TOKEN: str = ""

    @property
    def JIRA_AUTH(self):
        return HTTPBasicAuth(self.JIRA_USER, f"{self.JIRA_TOKEN}=638E3D23")

config = JiraAPIConfig()
# print(config.JIRA_TOKEN)
    


   


class EvaAPIConfig:
    """
    Класс для управления конфигурацией подключения к Eva REST API
    """
    pass


class BitrixAPIConfig:
    """
    Класс для управления конфигурацией подключения к Bitrix REST API
    """
    pass


 



    



