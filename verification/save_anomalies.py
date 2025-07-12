from sqlmodel import select
from database.session import get_session
from models.anomalie import Anomalie
import logging

logger = logging.getLogger(__name__)

def save_anomalies(anomalies: list):
    try:
        with get_session() as session:
            for a in anomalies:
                IDArticle = a.get("IDArticle")
                Code = a.get("Code")
                Type = a.get("Type", "anomalie_non_specifie")
                message = a.get("message", "")

                # 🔎 Vérifier si l'anomalie existe déjà
                stmt = select(Anomalie).where(
                    Anomalie.IDArticle == IDArticle,
                    Anomalie.Type == Type,
                    Anomalie.Code == Code,
                    Anomalie.message == message
                )
                existing = session.exec(stmt).first()

                if existing:
                    logger.info(f"Anomalie déjà enregistrée : {IDArticle}, {Type}, {Code}")
                    continue  # ⏭️ Passer à l'anomalie suivante

                # ✅ Ajouter si non existante
                nouvelle_anomalie = Anomalie(
                    IDArticle=IDArticle,
                    Code=Code,
                    Type=Type,
                    message=message
                )
                session.add(nouvelle_anomalie)

            session.commit()

    except Exception as e:
        logger.error(f"Erreur lors de l'enregistrement des anomalies : {e}")
        raise
