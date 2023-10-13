"""В этом модули находятся эндпоинты API"""

from fastapi import Depends, FastAPI 

app = FastAPI() 

@app.get("/", description="Этот эндпоинт позволяет проверить работоспособность приложения.")
async def hello(): 
    return {"Message": "mur-mur"}