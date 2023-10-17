"""В этом модуле содержится сервис для работы с вопросами (домен Questions)
"""

from infrastructure.repositories.questions import QuestionsRepository
from infrastructure.integrations.jserviceapi import JserviceApiIntegration
from domains.serializers import QuestionsPost
from .base import BaseService


class QuestionsService(BaseService):
    """Этот класс содержит в себе имплементацию сервиса для работы с доменом вопросов
    """

    def __init__(self):
        """Этот метод инициализирует объект класса сервис, присваевая ему поле self.repo  для работы с репозиторием вопросов
        """
        self.repo = QuestionsRepository()
        self.jserviceapi = JserviceApiIntegration()

    async def handle_post(self, request_body:QuestionsPost):
        response = await self.jserviceapi.get_random_question(request_body.questions_num)
        return response
        


    