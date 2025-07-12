from typing import List, Optional , TYPE_CHECKING
from sqlmodel import Field , SQLModel , Relationship
if TYPE_CHECKING:
    from models.article import article

class ar_sfamille ( SQLModel , table = True):
    IDArSousFamille : Optional[int] = Field ( default= None , primary_key= True)
    SousFamille : str
    IDArFamille : Optional[int] = Field(foreign_key="arfamille.IDArFamille")
