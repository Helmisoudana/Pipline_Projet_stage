from typing import Optional , TYPE_CHECKING
from sqlmodel  import Field , SQLModel , Relationship


if TYPE_CHECKING:
    from models.arfamille import arfamille
    from models.ar_sfamille import ar_sfamille
    from models.saison import saison
class article(SQLModel , table =True ) :
    IDArticle : Optional[int] =Field(default = None , primary_key = True)
    Article : str
    PrixFac : float
    prixAchat: float
    Code : str
    Etat : int 
    numInterne : int
    IDArFamille : Optional[int] = Field(foreign_key="arfamille.IDArFamille")
    IDArSousFamille : Optional[int] = Field(foreign_key="ar_sfamille.IDArSousFamille")
    IDGrille : Optional[int] = Field(foreign_key="grille.IDGrille")
    IDSaison : Optional[int] = Field(foreign_key="saison.IDSaison")
    IDFournisseur : Optional[int] = Field(foreign_key="fournissuer.IDFournisseur")
    IDAr_Couleur : Optional[int] = Field(foreign_key="ar_couleur.IDAr_Couleur")
    

