from fastapi import FastAPI, HTTPException
from routes.article_routes import router as article_router
from verification.pipline import pipline
from apscheduler.schedulers.background import BackgroundScheduler
from verification.pipline_API import pipline as pipline_API
from pydantic import BaseModel
from typing import List
app = FastAPI()
app.include_router(article_router)
scheduler = BackgroundScheduler()

class ArticleImportRequest(BaseModel):
    ids: List[int]
@app.get("/")
def home() :
    return {'welcome to our system'}


@app.get("/articles")
def Verifier_articles(payload: ArticleImportRequest):
    try:
        anomalies = pipline_API(payload)
        return anomalies
    except HTTPException as http_ex:
        # Si une HTTPException a déjà été levée dans le pipeline
        raise http_ex
    except Exception as e:
        # Erreur inattendue (erreur système, réseau, etc.)
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors de l'exécution du pipeline : {str(e)}"
        )
@app.on_event("startup")
def démarrer_scheduler():
    scheduler.add_job(pipline, 'interval', minutes=1)
    scheduler.start()
    print("✅ Scheduler démarré - Vérification toutes les 24 heures")
