# schemas/article_schema.py
from pydantic import BaseModel
from typing import Optional , List

class ArFamilleSchema(BaseModel):
    IDArFamille: int
    Famille: str

    class Config:
        orm_mode = True

class ArSousFamilleSchema(BaseModel):
    IDArSousFamille: int
    SousFamille: str

    class Config:
        orm_mode = True

class SaisonSchema(BaseModel):
    IDSaison: str
    Saison: Optional[str] = None  # optionnel si tu veux

    class Config:
        orm_mode = True

class ArticleRead(BaseModel):
    IDArticle: int
    Article: str
    Code: str
    PrixFac: float
    prixAchat: float
    Etat: int
    famille: Optional[ArFamilleSchema] = None
    sousfamille: Optional[ArSousFamilleSchema] = None
    saison: Optional[SaisonSchema] = None

    class Config:
        orm_mode = True
class ArticlesImportRequest(BaseModel):
    ids: List[int]



class ArticleImportRequest(BaseModel) :
    IDArticle:int
    Article:str
    Etat : int
    prixAchat:float
    PrixFac: float
    Famille: str
    SousFamille: str
    codeFamille: str
    Saison: str
    Ordre: str
    couleur: str
    fournisseur: str
    Code:str
