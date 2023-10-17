"""Этот модуль содержит модели для сериализации и валидации данных
"""
from datetime import datetime
from pydantic import BaseModel, Field 

class QuestionsPost(BaseModel): 
    """Этот класс содержит модель для валидации тела ПОСТ запроса на эндпоинт questions
    """
    questions_num:int = Field(ge=1)

class QuestionPydantic(BaseModel):
    """Этот класс содержит в себе сериализатор для данных из БД. 
    Схема данных в бд находится в файле models.py
    """
    id:int
    question_text: str
    answer_text:str
    creation_date:datetime

    class Config:
        orm_mode = True
        from_attributes = True
    
    
