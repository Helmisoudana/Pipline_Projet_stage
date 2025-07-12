from typing import Optional 
from sqlmodel  import Field , SQLModel , Relationship

class ar_couleur(SQLModel , table = True ):
    IDAr_Couleur : Optional[int] = Field ( default = None , primary_key=True)
    Couleur : str
    Code : str