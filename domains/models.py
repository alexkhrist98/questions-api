"""В этом модуле хранятся модели для работы с БД при помощи SQLAlchemy.
Модели валидации и сериализации (pydantic) хранятся в serializers.py
"""

from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Question(Base):
    """Этот класс представляет собой модель, отражающую таблицу"""
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True) #внутренний id вопроса
    api_id = Column(Integer) #id, поступающий от API 
    question_text = Column(Text, index=True, unique=True)
    answer_text = Column(Text)
    creation_date = Column(DateTime)


    