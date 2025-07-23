from sqlmodel import select, or_
from database.session import get_session
from models.article import article
from models.arfamille import arfamille
from models.ar_sfamille import ar_sfamille
from models.saison import saison
from models.grille import grille
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta


def get_articles_today():
    try:
        # Plage de date pour aujourd'hui
        today = datetime.today().date()
        today_start = datetime.combine(today, datetime.min.time())
        today_end = datetime.combine(today + timedelta(days=1), datetime.min.time())

        with get_session() as session:
            stmt = (
                select(
                    article.IDArticle,
                    article.Article,
                    article.Code,
                    article.PrixFac,
                    article.prixAchat,
                    article.Etat,
                    arfamille.Famille,
                    ar_sfamille.SousFamille,
                    saison.Saison,
                    article.numInterne,
                    grille.Grille,
                    saison.Ordre,
                    arfamille.Code
                )
                .join(arfamille, arfamille.IDArFamille == article.IDArFamille, isouter=True)
                .join(ar_sfamille, ar_sfamille.IDArSousFamille == article.IDArSousFamille, isouter=True)
                .join(saison, saison.IDSaison == article.IDSaison, isouter=True)
                .join(grille, grille.IDGrille == article.IDGrille, isouter=True)
                .where(
                    ar_sfamille.IDArFamille != 49,
                    article.Etat != 0,
                    or_(
                        article.SaisiLe >= today_start,
                        article.ModifieLe >= today_start
                    ),
                    or_(
                        article.SaisiLe < today_end,
                        article.ModifieLe < today_end
                    )
                )
            )

            rows = session.exec(stmt).all()

            result = []
            for row in rows:
                d = {
                    "IDArticle": row[0],
                    "Article": row[1],
                    "Code": row[2],
                    "PrixFac": row[3],
                    "prixAchat": row[4],
                    "Etat": row[5],
                    "Famille": row[6],
                    "SousFamille": row[7],
                    "Saison": row[8],
                    "numInterne": row[9],
                    "Grille": row[10],
                    "Ordre": row[11],
                    "codeFamille": row[12]
                }
                result.append(d)

            print(result) 

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": "Erreur lors de la récupération des articles",
                "detail": str(e)
            }
        )
get_articles_today()