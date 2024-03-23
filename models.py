# models.py
from sqlmodel import Field, SQLModel

class Hero(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int = None
