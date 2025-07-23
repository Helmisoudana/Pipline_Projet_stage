from fastapi import APIRouter , HTTPException
from schemas.article_schema import ArticlesImportRequest , ArticleImportRequest
from services.pipline_API import pipline
from verification.fetchdata_withJson import import_articles_by_ids
from schemas.response_schema import APIResponse
from utils.logger import logger 

router = APIRouter(prefix="", tags=["Articles"])
@router.get("/articles")
def VerifierTestArticle(payload: ArticlesImportRequest):
    logger.info(f"Requête /articles reçue avec payload: {payload}")
    try:
        articles = import_articles_by_ids(payload)
        anomalies = pipline(articles)
        logger.info(f"Pipeline exécuté avec succès. {len(anomalies)} anomalies détectées.")
        return APIResponse(data=anomalies, message="La vérification s'est terminée avec succès.", status=200)
    except Exception as e:
        logger.error(f"Erreur lors de l'exécution du pipeline /articles : {e}", exc_info=True)
        return APIResponse(data=[], message=f"Erreur lors de l'exécution du pipeline : {str(e)}", status=400)

@router.post("/testarticle")
def Verifier_articles(payload: ArticleImportRequest):
    logger.info(f"Requête /testarticle reçue avec payload: {payload}")
    try:
        article_dict = payload.dict()
        anomalies = pipline([article_dict])
        logger.info(f"Pipeline exécuté avec succès. {len(anomalies)} anomalies détectées.")
        return APIResponse(data=anomalies, message="La vérification s'est terminée avec succès.", status=200)
    except Exception as e:
        logger.error(f"Erreur lors de l'exécution du pipeline /testarticle : {e}", exc_info=True)
        return APIResponse(data=[], message=f"Erreur lors de l'exécution du pipeline : {str(e)}", status=400)