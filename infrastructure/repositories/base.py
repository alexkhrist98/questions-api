"""Этот модуль содержит в себе базовый класс для создания репозиториев, отвечающих за работу с различными СУБД
Также этот метод содержит реализацию базовый класс репозитория для SQLAlchemy
"""

from abc import ABC, abstractmethod
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from domains.models import Base, Question

class BaseRepository(ABC): 
    """""Этот абстрактный класс содержит в себе абстрактные методы, необходимые для работы с базой данных
    """
    
    @abstractmethod
    def fetch_one(self): 
        raise NotImplementedError(f"Этот метод пока не определён для {__class__.__name__}")
    
    @abstractmethod
    def fetch_all(self, *args, **kwargs):
        raise NotImplementedError(f"Метод пока не определён для {__class__.__name__}")
    
    @abstractmethod
    def insert_one(self): 
        raise NotImplementedError(f"Метод пока не определён для {__class__.__name__}")
    
    @abstractmethod
    def insert_many(self):
        raise NotImplementedError(f"Метод пока не определён для {__class__.__name__}")
    
    @abstractmethod
    def fetch_by_id(self):
        raise NotImplementedError(f"Метод пока не определён для {__class__.__name__}")
    
class AlchemyBaseRepository(BaseRepository):
    """Этот класс содержит в себе реализацию базовых функций репозитория, построенного на SQLAlchemy. 
    Внутри этого класса инициализируется движок и сессия, который затем будут наследоваться подклассами. 
    Класс не определяет конкретных методов для работы с бд.
    """
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    CONNECTION_STRING = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    def __init__(self):
        """Этот метод инициализирует базовый репозиторий. 
        Внутри метода инициализируются параметра подключения к бд, создаётся движок и сессия SQLAlchemy
        """
        self.engine = create_engine(__class__.CONNECTION_STRING)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def fetch_all(self, model):
        """_Этот метод позволяет получить все записи, связанные с моеделью, передаваемой в качестве аргумента model

        Args:
            model (Модель models.py): _Модель данных, отаражющая содержимое таблицы для ORM_

        Returns:
            modelobject: объект класса, переданного в аргумент model_
        """        
        result = self.session.query(model).all()
        return result
    
    def fetch_one(self, model):
        """Этот метод позволяет получить один объект из репозитория

        Args:
            model (Модель models.py): Модель данных для ORM

        Returns:
            modelobject: Объект класса, переданого в аргументе model
            пустой словарь: при возникновении исключения NoResultFound
        """        
        try:
            result = self.session.query(model).first()
            return result
        except NoResultFound:
            return {}
    
    def insert_one(self, model):
        """_Этот метод позволяет добавить данные в БД при помощи ORM 

        Args:
            model (объект models.py): _Объект класса, описанного в models.py для рабты с ORM

        Returns:
            Call: возвращает вызов session.commit()
        """        
        self.session.add(model)
        return self.session.commit()
    
    def fetch_by_id(self, model, id: int):
        try:
            result = self.session.query(model).filter_by(id=id).one()
            return result
        except NoResultFound:
            return {}
    
    def insert_many(self):
        return super().insert_many()
         
