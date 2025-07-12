from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("MYSQL_URL")
engine = create_engine(DATABASE_URL, echo=True)

# Création automatique des tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

create_db_and_tables()

def get_session():
    return Session(engine)
