
from models import Hero
from database import engine
from sqlmodel import Session

try:
    def create_heroes():
        hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson", age=18)
        hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador", age=39)
        hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

        # ********Best Practice**************
        with Session(engine) as session:
            session.add(hero_1)
            session.add(hero_2)
            session.add(hero_3)

            session.commit()
except Exception as e:
    print("No Table is found")
    exit(1)

if __name__ == "__main__":
    create_heroes()
