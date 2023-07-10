from .config import *
import random
from pymongo import MongoClient
from .schemas import User, Todo
from typing import List

class DB:
    def __init__(self) -> None:
        self.__client = MongoClient(db_url)
        self._db = self.__client.get_default_database(default=db_name)
        self._users = self._db.get_collection(users)
        self._id_length = id_length

    def generate_id(self):
        todos = [todo.id for todo in self.get_all_todos()]
        users = [user.id for user in self.get_all_users()]
        min = "1"+'0'*(self._id_length-1)
        max = "9"*self._id_length
        def generate():
            return random.randint(
                int(min), 
                int(max)
                )
        id = generate()
        while id in users or id in todos:
            id = generate()
        return id

    def get_all_users(self) -> List[User]:
        return [User(**data) for data in self._users.find()]
    
    def get_user(self, **params) -> User:
        data = self._users.find_one(params)
        return User(**data) if data else None
    
    def add_user(self, user: User) -> None:
        self._users.insert_one(user.dict())

    def update_user(self, user: User) -> None:
        filter = {"id": user.id}
        self._users.update_one(filter, {"$set": user.dict()})

    def get_all_todos(self) -> List[Todo]:
        return sum([user.todos for user in self.get_all_users()], [])
    
    def done_todo(self, user_id: int, todo_id: int) -> None:
            user = self.get_user(id=user_id)
            for todo in user.todos:
                if todo.id == todo_id:
                    user.todos.remove(todo)
                    todo.status = True
                    user.todos.append(todo)
            self.update_user(user)

    def delete_todo(self, user_id: int, todo_id: int) -> None:
            user = self.get_user(id=user_id)
            for todo in user.todos:
                if todo.id == todo_id:
                    user.todos.remove(todo)
            self.update_user(user)