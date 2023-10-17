""""Этот модуль содержит в себе адаптеры для преобразования вопросов и приведения к разилчным схеама внутри приложения
"""
from datetime import datetime
from .models import Question
from .serializers import QuestionPydantic

def api_question_to_orm(api_question: dict):
    """_Эту функция позволяет конвертировать dict, содержащий 
    данные, приходящие с jservice api в модель models.Question (SQLAlchemy)

    Args:
        api_question (dict): _словарь, содержаий вопрос от jservice api

    Returns:
        Question: Объект класса Question (models.Question)
    """    
    question_orm = Question()
    question_orm.id = int(api_question.get("id"))
    question_orm.question_text = api_question.get("question")
    question_orm.answer_text = api_question.get("answer")
    question_orm.creation_date = datetime.strptime(api_question.get("created_at"), "%Y-%m-%dT%H:%M:%S.%fZ")
    return question_orm

def question_orm_to_pydantic(model):
    """Этот адаптер позволяет конвертировать данные из models.Question в serializers.QuestionPydantic

    Args:
        model (Question): объект класса models.Question

    Returns:
        QuestionPydantic: объект класса QuestionPydantic
    """    
    return QuestionPydantic.from_orm(model)

def question_api_to_pydantic(question:dict):
    """_Этот адаптер позволяет конвертировать данные, поступающие от jservice api в serializers.QuestionPydantic

    Args:
        question (dict): _Данные, поступающие от jservice api

    Returns:
        QuestionPydantic: объект класса serializers.QuestionPydantic
    """    
    mapper = {"id": question.get("id"),
              "question_text": question.get("question"),
              "answer_text": question.get("answer"),
              "creation_date": datetime.strptime(question.get("created_at"), "%Y-%m-%dT%H:%M:%S.%fZ")}
    return QuestionPydantic(**mapper)
              
