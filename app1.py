import os
from dotenv import load_dotenv
from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session    

load_dotenv()
NEON_PG_CONN_STR = os.getenv("NEON_PG_CONN_STR")

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

    

engine = create_engine(NEON_PG_CONN_STR, echo=True)
# engine.connect()

def create_db_tables():
    SQLModel.metadata.create_all(engine)






def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador", age=39)
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    # ********Best Paractice**************
    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)

        session.commit()



if __name__ == "__main__":
    create_db_tables()
    create_heroes()     