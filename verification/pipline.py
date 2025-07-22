from verification.fetchdata import get_articles_yesterday
from verification.verif_duplication import detect_duplicates
from verification.verifnull import detect_null_or_vide_champs
from verification.VerifCode import detect_code_errors
from verification.detect_avec_model import detcter_les_anomalies
from verification.save_anomalies import save_anomalies
from fastapi import HTTPException

def pipline():
    try:
        anomalies = []
        articles = get_articles_yesterday()
        if not articles:
            print("Aucun article à traiter hier.")
            return 
        anomalies += detect_duplicates(articles)
        anomalies_null = detect_null_or_vide_champs(articles)
        if not anomalies_null:
            anomalies += detect_code_errors(articles) 
        anomalies += anomalies_null
        anomalies += detcter_les_anomalies(articles)
        save_anomalies(anomalies)
        return anomalies

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur dans le pipeline : {str(e)}")


