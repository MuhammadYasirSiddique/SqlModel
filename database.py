# database.py
import os
from dotenv import load_dotenv
from sqlmodel import create_engine
from models import Hero

load_dotenv()
NEON_PG_CONN_STR = os.getenv("NEON_PG_CONN_STR")

engine = create_engine(NEON_PG_CONN_STR, echo=True)



if __name__ == "__main__":
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(engine)
