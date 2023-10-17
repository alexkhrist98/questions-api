"""Этот модуль содержит в себе интеграция с API jservice.io
"""

import httpx 
from .base import BaseApiIntegration

class JserviceApiIntegration(BaseApiIntegration):
    """Этот класс содержит в себе интеграцию с API jservice.io
    """

    def __init__(self):
        self.base_uri = "http://jservice.io/api/"
        self.random_questions = self.base_uri + "random" #Этот эндпоинт прпнимает count:int в качестве параметра запроса

    async def get_random_question(self, count:int):
        """Этот метод позволяет сделать запрос к эндпоинту random и получить в ответ список json с вопросами

        Args:
            count (int): _желаемое количество вопросов_
        """
        try: 
            async with httpx.AsyncClient() as client:
                response = await client.get(self.random_questions, params={"count": count})
                return response.json()
        except Exception as exc:
            raise exc        