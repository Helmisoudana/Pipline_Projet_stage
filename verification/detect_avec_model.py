import joblib
import pandas as pd
import json
from fastapi import HTTPException
import math
import xgboost as xgb
from xgboost import DMatrix
import traceback  # pour logguer les erreurs
from catboost import CatBoostRegressor


 # Assure-toi que le chemin est correct

def data_pretraitement(articles):
    df = pd.DataFrame(articles)
    
    # Charger le mapping
    with open("famille_sf_mapping.json", "r", encoding="utf-8") as f:
        mapping = json.load(f)

    df['SousFamille'] = df['SousFamille'].fillna('Aucune').replace('', 'Aucune')
    df['Famille'] = df['Famille'].fillna('Aucune').str.strip().str.lower()
    df['SousFamille'] = df['SousFamille'].str.strip().str.lower()
    df['Famille_SousFamille'] = df['Famille'] + '_' + df['SousFamille']
    df['Famille_SousFamille_encoded'] = df['Famille_SousFamille'].map(mapping).fillna(-1)  # ou gérer les inconnus
    return df[['IDArticle', 'Code', 'PrixFac', 'prixAchat', 'Famille_SousFamille_encoded']]



def detcter_les_anomalies(articles):
    anomalies = []
    model = CatBoostRegressor()
    model.load_model("catboost_model.cbm")
    try:
        df = data_pretraitement(articles)

        for _, row in df.iterrows():
            x = pd.DataFrame([[
                row['PrixFac'],
                row['prixAchat'],
                row['Famille_SousFamille_encoded']
            ]], columns=["PrixFac", "prixAchat", "Famille_SousFamille_encoded"])
            prediction = model.predict(x)
            if prediction[0] == 1:
                anomalies.append({
                    "IDArticle": row['IDArticle'],
                    "Type" : 'Anomalie de prix',
                    "Code": row['Code'],
                    "message": f"Cet article possède une anomalie au niveau des prix de facturation {row['PrixFac']} ou prix d'achat{row['prixAchat']} . la précison de notre model est 80%"
                })

        return anomalies

    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Modèle ou Fichier mapping non trouvé. Vérifiez que 'model.pkl' existe.")
    
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Champ manquant : {str(e)}")

    except Exception as e:
        # Pour debug : tu peux aussi logguer traceback.format_exc()
        print(traceback.format_exc())  
        raise HTTPException(status_code=500, detail="Une erreur interne est survenue lors de l'analyse.")

