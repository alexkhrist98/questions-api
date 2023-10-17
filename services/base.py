"""Этот модуль содержит в себе абстрактный класс BaseService, который предоставляет интерфейс для проектирования
    новых сервисов внутри приложения
"""

from abc import ABC, abstractmethod

class BaseService(ABC):
    """Этот абстрактный класс позволяет создавать общие методы, тем самым расширяя слой сервисов
    """

    @abstractmethod
    def __init__(self):
        self.repo = None #Сюда передаётся репозиторий для работы с БД
        
    @abstractmethod
    def handle_post(self, request_body, *args, **kwargs):
        """Этот абстрактный метод создаёт основу для обработки POST запросов внутри сервисов

        Args:
            request_body (pydantic model): _тело запроса_

        Raises:
            NotImplemented: исключение возникает, если метод не определён внутри подклассов.
        """         
        raise NotImplemented(f'Этот метод пока не определён внутри {__class__.__name__}')