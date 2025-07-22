from verification.fetchdata_withJson import import_articles_by_ids
from verification.verif_duplication import detect_duplicates
from verification.verifnull import detect_null_or_vide_champs
from verification.VerifCode import detect_code_errors
from verification.detect_avec_model import detcter_les_anomalies
from fastapi import HTTPException

def pipline(articles):
    try:
        anomalies = []
        anomalies += detect_duplicates(articles)
        anomalies_null = detect_null_or_vide_champs(articles)
        if not anomalies_null:
            anomalies += detect_code_errors(articles) 
        anomalies += anomalies_null
        anomalies += detcter_les_anomalies(articles)
        return anomalies

    except HTTPException as http_ex:
        # Si fetch_articles a déjà levé une HTTPException
        raise http_ex

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur dans le pipeline : {str(e)}")


