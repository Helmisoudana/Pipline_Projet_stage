article=[{"IDArticle":"","Article":"","Code":"THNT99A","numInterne":0,"PrixFac":0.0,"prixAchat":0.0,"Etat":1,"Famille":"T-SHIRT","SousFamille":"","Saison":"BASE BE"},{"IDArticle":17092,"Article":"JUPE 34/46","Code":"ZENJ001","numInterne":1,"PrixFac":1.0,"prixAchat":0.29,"Etat":1,"Famille":"JUPE","SousFamille":"JUPE CET","Saison":"BASE BE"},{"IDArticle":15518,"Article":"BIMA MC","Code":"THNT99A","numInterne":0,"PrixFac":0.0,"prixAchat":0.0,"Etat":1,"Famille":"T-SHIRT","SousFamille":"SWEAT SHIRT","Saison":"BASE BE"},{"IDArticle":17092,"Article":"JUPE 34/46","Code":"ZENJ001","numInterne":1,"PrixFac":1.0,"prixAchat":0.29,"Etat":1,"Famille":"JUPE","SousFamille":"JUPE CET","Saison":"BASE BE"},{"IDArticle":17293,"Article":"PANTALON Work 34/46","Code":"ZENP001","numInterne":1,"PrixFac":1.0,"prixAchat":0.29,"Etat":1,"Famille":"PANTALON WORK","SousFamille":"PANTALON","Saison":"BASE BE"},{"IDArticle":17309,"Article":"CHEMISE manche montée 34/46","Code":"ZENC001","numInterne":1,"PrixFac":1.0,"prixAchat":0.29,"Etat":1,"Famille":"CHEMISE","SousFamille":"CHEMISE ML","Saison":"BASE BE"},{"IDArticle":17342,"Article":"VESTE manche montée 34/46","Code":"ZENW001","numInterne":1,"PrixFac":1.0,"prixAchat":0.29,"Etat":1,"Famille":"VESTES","SousFamille":"VESTE TAILLEUR","Saison":"BASE BE"},{"IDArticle":17420,"Article":"SHORT 34/46","Code":"ZENB002","numInterne":2,"PrixFac":1.0,"prixAchat":0.29,"Etat":1,"Famille":"SHORT","SousFamille":"SHORT","Saison":"BASE BE"},{"IDArticle":17426,"Article":"CHEMISE manche raglan 34/46","Code":"ZENC002","numInterne":2,"PrixFac":1.0,"prixAchat":0.29,"Etat":1,"Famille":"CHEMISE","SousFamille":"CHEMISE ML","Saison":"BASE BE"},{"IDArticle":17427,"Article":"TOP Bretelles 34/46","Code":"ZENTO001","numInterne":1,"PrixFac":1.0,"prixAchat":0.29,"Etat":1,"Famille":"TOP","SousFamille":"DEBARDEUR","Saison":"BASE BE"},{"IDArticle":17431,"Article":"ROBE Bustier 34/46","Code":"ZENR001","numInterne":1,"PrixFac":1.0,"prixAchat":0.29,"Etat":1,"Famille":"ROBE","SousFamille":"ROBE CET BUSTIER","Saison":"BASE BE"},{"IDArticle":17433,"Article":"ROBE manche montée 34/46","Code":"ZENR002","numInterne":2,"PrixFac":1.0,"prixAchat":0.29,"Etat":1,"Famille":"ROBE","SousFamille":"ROBE CET DOUBLEE","Saison":"BASE BE"},{"IDArticle":17444,"Article":"MANTEAU MANCHE MONTEE 34/46","Code":"ZENH001","numInterne":1,"PrixFac":1.0,"prixAchat":0.29,"Etat":1,"Famille":"MANTEAU","SousFamille":"MANTEAU","Saison":"BASE BE"},{"IDArticle":17451,"Article":"ROBE manche raglan 34/46","Code":"ZENR003","numInterne":3,"PrixFac":1.0,"prixAchat":0.29,"Etat":1,"Famille":"ROBE","SousFamille":"ROBE CET DOUBLEE","Saison":"BASE BE"},{"IDArticle":17452,"Article":"COMBI PANTALON manche montée 34/46","Code":"ZEND001","numInterne":1,"PrixFac":0.0,"prixAchat":1.0,"Etat":1,"Famille":"COMBINAISON","SousFamille":"COMBI PANTALON W","Saison":"BASE BE"},{"IDArticle":17454,"Article":"COMBI PANTALON manche raglan 34/46","Code":"ZEND003","numInterne":3,"PrixFac":1.0,"prixAchat":0.29,"Etat":1,"Famille":"COMBINAISON","SousFamille":"COMBI PANTALON W","Saison":"BASE BE"},{"IDArticle":17455,"Article":"COMBI SHORT manche montée 34/46","Code":"ZEND004","numInterne":4,"PrixFac":1.0,"prixAchat":0.29,"Etat":1,"Famille":"COMBINAISON","SousFamille":"COMBI SHORT","Saison":"BASE BE"},{"IDArticle":17456,"Article":"COMBI SHORT manche raglan 34/46","Code":"ZEND005","numInterne":5,"PrixFac":1.0,"prixAchat":0.29,"Etat":1,"Famille":"COMBINAISON","SousFamille":"COMBI SHORT","Saison":"BASE BE"}]
from sqlmodel import select
from database.session import get_session
from models.article import article
from models.arfamille import arfamille
from models.ar_sfamille import ar_sfamille
from models.saison import saison
from models.grille import grille
from fastapi.responses import JSONResponse

def get_articles():
    with get_session() as session:
            stmt = (
                select(
                    article.IDArticle,
                    article.Article,
                    article.Code,
                    article.PrixFac,
                    article.prixAchat,
                    article.Etat,
                    article.IDArFamille,
                    article.IDArSousFamille,
                    arfamille.Famille,
                    ar_sfamille.SousFamille,
                    saison.Saison,
                    saison.Ordre,
                    arfamille.Code
                )
                .join(arfamille, arfamille.IDArFamille == article.IDArFamille , isouter=True)
                .join(ar_sfamille, ar_sfamille.IDArSousFamille == article.IDArSousFamille, isouter=True)
                .join(saison, saison.IDSaison == article.IDSaison, isouter=True)
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
                    "Ordre": row[9],
                    "codeFamille": row[10]
                }
                result.append(d)

            return rows
article=get_articles()


print(len(article))