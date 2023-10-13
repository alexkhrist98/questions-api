"""Этот модуль содержит в себе класс сервер, отвечающий за создание и запуск сервера uvicorn"""

import os 
import uvicorn

class Server: 
    """Этот класс содержит в себе функции, связанные с сервером, его параметрами и запуском
    """
    def __init__(self, app_path: str = "infrastructure.app:app"):
        """Этот метод инициализирует объект класса сервер. Поля класса содержат в себе параметры сервера.

        Args:
            app_path (str, optional): Путь к объекту FastAPI. Defaults to "app.app:app".
        """        
        self.app_path = app_path 
        self.address:str = os.getenv("ADDRESS") #Адрес сервера
        self.port:int = int(os.getenv("PORT")) #Порт
        self.reload = bool(os.getenv("RELOAD")) #Флаг позволяет отслеживать изменения и перезапускать сервер без необходимости перезагрузки контейнера

    def run(self) -> None:
        """Эта функция запускает сервер uvicorn с указанными в полях объекта параметрами
        """        
        uvicorn.run(self.app_path, host=self.address, port=self.port, reload=self.reload)
