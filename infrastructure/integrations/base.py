"""Этот модуль содержит в себе базовый класс для создания интеграций со сторонними REST API
"""

from abc import ABC, abstractmethod

class BaseApiIntegration(ABC):
    """Этот абстрактный класс является базовым для создания интеграций с RESTful API. 
    """

    @abstractmethod
    def __init__(self):
        """Этот метод является шаблоном для создания методов инициализации подклассов
        Внутрь этого метода в качестве полей класса записываются API Endpoints.
        """
        self.base_uri:str = None #базовый URI
        self.endpoint1:str = self.base_uri + None #в таком формате необходимо добавлять эндпоинты

        @abstractmethod
        def get(self, *args, **kwargs): 
            """Этот метод является шаблоном для создания метода get для ресурсов сторонних API.
            """
            raise NotImplemented(f"Метод пока не определён для {__class__.__name__}")
        
        
