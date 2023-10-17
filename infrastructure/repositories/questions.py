"""Этот модуль содержит в себе реализацию репозитория вопросов на основе SQLAlchemy.
Для реализации репозитория на других ORM, необходимо отнаследоваться от базового класса репозитория и реализовать абстрактные методы
"""

from .base import AlchemyBaseRepository
from domains.models import Base, Question

class QuestionsRepository(AlchemyBaseRepository):
    def __init__(self): 
        super().__init__()
        self.model = Question
        Base.metadata.create_all(bind=self.engine) 
    

