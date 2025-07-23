from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv
import os
from utils.logger import logger  # Importer le logger

load_dotenv()

DATABASE_URL = os.getenv("MYSQL_URL")
logger.info(f"Chargement de la base de données avec l'URL : {DATABASE_URL}")

try:
    engine = create_engine(DATABASE_URL, echo=False)
    logger.info("Moteur de base de données créé avec succès.")
except Exception as e:
    logger.error(f"Erreur lors de la création du moteur de base de données : {e}")
    raise

# Création automatique des tables
def create_db_and_tables():
    try:
        SQLModel.metadata.create_all(engine)
        logger.info("Tables créées ou déjà existantes dans la base de données.")
    except Exception as e:
        logger.error(f"Erreur lors de la création des tables : {e}")
        raise

create_db_and_tables()

def get_session():
    try:
        session = Session(engine)
        logger.debug("Nouvelle session de base de données créée.")
        return session
    except Exception as e:
        logger.error(f"Erreur lors de la création de la session : {e}")
        raise
