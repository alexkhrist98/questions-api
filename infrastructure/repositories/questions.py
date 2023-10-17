"""Этот модуль содержит в себе реализацию репозитория вопросов на основе SQLAlchemy.
Для реализации репозитория на других ORM, необходимо отнаследоваться от базового класса репозитория и реализовать абстрактные методы
"""

from sqlalchemy import desc
from domains.models import Base, Question
from .base import AlchemyBaseRepository

class QuestionsRepository(AlchemyBaseRepository):
    def __init__(self): 
        super().__init__()
        self.model = Question
        Base.metadata.create_all(bind=self.engine)

    def fetch_one(self):
        return super().fetch_one(self.model)
    
    def fetch_all(self):
        return super().fetch_all(self.model)

    def insert_one(self, model):
        return super().insert_one(model)
    
    def fetch_by_id(self, id: int):
        return super().fetch_by_id(self.model, id)
    
    def fetch_most_recent(self):
        return self.session.query(self.model).order_by(desc(self.model.id)).first()
    

