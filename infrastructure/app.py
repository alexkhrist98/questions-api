"""В этом модули находятся эндпоинты API"""

from fastapi import Depends, FastAPI
from domains.serializers import QuestionsPost
from services.question_service import QuestionsService

app = FastAPI() 

@app.get("/", description="Этот эндпоинт позволяет проверить работоспособность приложения.")
async def hello(): 
    return {"Message": "mur-mur"}

@app.post("/questions", 
          tags=["Вопросы для викторины"], 
          description="Этот эндпоинт принимает пост запросы и возвращает последний записаный в бд вопрос для викторины")
async def request_handler(request:QuestionsPost, service:QuestionsService = Depends(QuestionsService().__init__())):
    return await service.handle_post(request)