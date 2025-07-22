from fastapi import FastAPI, HTTPException
from routes.article_routes import router as article_router
from verification.pipline import pipline
from apscheduler.schedulers.background import BackgroundScheduler
from routes.verifierArticles_routes import router as verifierArticles
app = FastAPI()
app.include_router(article_router)
app.include_router(verifierArticles)
scheduler = BackgroundScheduler()

 

@app.get("/")
def home() :
    return {'welcome to our system'}

@app.on_event("startup")
def démarrer_scheduler():
    scheduler.add_job(pipline, 'interval', hours=24)
    scheduler.start()
    print("✅ Scheduler démarré - Vérification toutes les 24 heures")
