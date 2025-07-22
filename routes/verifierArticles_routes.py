from fastapi import APIRouter , HTTPException
from schemas.article_schema import ArticlesImportRequest , ArticleImportRequest
from verification.pipline_API import pipline
from verification.fetchdata_withJson import import_articles_by_ids

router = APIRouter(prefix="", tags=["Articles"])
@router.get("/articles")
def VerifierTestArticle(payload : ArticlesImportRequest):
    try :
        articles=import_articles_by_ids(payload)
        anomalies=pipline(articles)
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

@router.post("/testarticle")
def Verifier_articles(payload: ArticleImportRequest):
    try:
        article_dict = payload.dict()
        anomalies=pipline([article_dict])
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