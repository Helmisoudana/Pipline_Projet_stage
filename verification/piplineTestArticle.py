from verification.verif_duplication import detect_duplicates
from verification.verifnull import detect_null_or_vide_champs
from verification.VerifCode import detect_code_errors
from verification.detect_avec_model import detcter_les_anomalies
from fastapi import HTTPException

def piplineTestArticle(payload):
    try:
        anomalies = []
        print(payload)
        try:
            anomalies += detect_duplicates(payload)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erreur dans detect_duplicates : {str(e)}")

        try:
            anomalies += detect_null_or_vide_champs(payload)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erreur dans detect_null_or_vide_champs : {str(e)}")

        try:
            anomalies += detect_code_errors(payload)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erreur dans detect_code_errors : {str(e)}")

        try:
            anomalies += detcter_les_anomalies(payload)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erreur dans detcter_les_anomalies : {str(e)}")

        return anomalies

    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur dans le pipeline : {str(e)}")
