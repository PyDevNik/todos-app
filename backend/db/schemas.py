from pydantic import BaseModel
from datetime import datetime
from typing import List
from app._app import generate_id

class Todo(BaseModel):
    id: int = generate_id()
    user_id: int
    task_name: str
    time: datetime
    status: bool = False

class User(BaseModel):
    id: int = generate_id()
    username: str
    password: str
    is_active: bool = True
    todos: List[Todo] = []
    is_active: bool = True
    is_authenticated = True
    is_anonymous: bool = False

    def get_id(self):
        return str(self.id)