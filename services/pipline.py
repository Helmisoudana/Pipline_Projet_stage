from loguru import logger
from verification.fetchdata import get_articles_yesterday
from verification.verif_duplication import detect_duplicates
from verification.verifnull import detect_null_or_vide_champs
from verification.VerifCode import detect_code_errors
from verification.detect_avec_model import detcter_les_anomalies
from verification.save_anomalies import save_anomalies
from fastapi import HTTPException

def pipline():
    try:
        logger.info("Début du pipeline de vérification des articles.")

        anomalies = []
        articles = get_articles_yesterday()
        if not articles:
            logger.info("Aucun article à traiter hier.")
            return
        
        logger.info(f"{len(articles)} articles récupérés pour traitement.")

        anomalies += detect_duplicates(articles)
        logger.info(f"{len(anomalies)} anomalies détectées après duplication.")

        anomalies_null = detect_null_or_vide_champs(articles)
        if not anomalies_null:
            anomalies += detect_code_errors(articles) 
            logger.info("Détection d'erreurs de code effectuée.")
        anomalies += anomalies_null

        anomalies += detcter_les_anomalies(articles)
        logger.info(f"Nombre total d'anomalies détectées : {len(anomalies)}.")

        save_anomalies(anomalies)
        logger.info("Anomalies sauvegardées avec succès.")

        return anomalies

    except Exception as e:
        logger.error(f"Erreur dans le pipeline : {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Erreur dans le pipeline : {str(e)}")
