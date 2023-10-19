"""В этом модуле содержится сервис для работы с вопросами (домен Questions)
"""

from infrastructure.repositories.questions import QuestionsRepository
from infrastructure.integrations.jserviceapi import JserviceApiIntegration
from domains.serializers import QuestionsPost
from domains.adapters import api_question_to_orm, question_orm_to_pydantic, question_api_to_pydantic
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
        """Этот метод содержит в себе логику обработки post запроса на эндпоинт /questions

        Args:
            request_body (QuestionsPost): тело запроса

        Returns:
            QuestionPydantic: ответ на запрос, содерщаий в себе вопрос serializers.QuestionsPydantic
        """
        response = question_orm_to_pydantic(self.repo.fetch_most_recent())      
        new_question = await self._collect_questions(count=request_body.questions_num)
        await self._save_questions(new_question)
        return response

    
    async def _collect_questions(self, count:int):
        """Это вспомогательный метод, учасвтующий в обработке пост запроса к эндпоинту questions.
        Он собирает список вопросов для их сохранения в БД.

        Args:
            count (int): количество вопросов.

        Returns:
            дшые: список вопросов
        """        
        questions_list = []
        while len(questions_list) < count:
            questions_left = count - len(questions_list)
            questions_list += await self._aggregate_new_questions(count=questions_left)
        return questions_list
    
    async def _aggregate_new_questions(self, count:int):
        """Это всопомгательный метод, участвующий в обработке post запроса к эндпоинту questions.
        Этот метод делает запрос к стороннему api для получения вопросов, а также вызывает метод, проверяющий наличие вопроса в БД.

        Args:
            count (int): количество запрашиваемых вопросов

        Returns:
            list: список новых вопросов (отсутствующих в БД)
        """        
        new_questions = await self.jserviceapi.get_random_question(count=count)
        result = []
        for i, question in enumerate(new_questions):
            if not self.repo.fetch_by_api_id(question.get("id")):
                result.append(question)
        return result
    
    async def _save_questions(self, questions:list):
        """Этот вспомогательный метод участвует в обработке post запроса.
        Он сохраняет получившиеся вопросы в БД, предварительно их преобразовывая в необходимый формат.

        Args:
            questions (list): список вопросов для сохранения в БД
        """        
        for question in questions:
            question = api_question_to_orm(question)
            self.repo.insert_one(question)
        
            
                
            
            
            
    
    
        


    