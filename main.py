from fastapi import FastAPI, HTTPException
from routes.article_routes import router as article_router
from services.pipline import pipline
from apscheduler.schedulers.background import BackgroundScheduler
from routes.verifierArticles_routes import router as verifierArticles
from fastapi.middleware.cors import CORSMiddleware
from utils.logger import logger
from config.config import settings
import uvicorn

app = FastAPI()
app.include_router(article_router)
app.include_router(verifierArticles)
scheduler = BackgroundScheduler()

 


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)
@app.get("/")
def home() :
    logger.info("welcome to our system")

@app.on_event("startup")
def démarrer_scheduler():
    scheduler.add_job(pipline, 'interval', hours=24)
    scheduler.start()
    logger.info("Scheduler démarré - Vérification toutes les 24 heures")

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.app_host, port=settings.app_port, reload=True)