from typing import Optional 
from sqlmodel  import Field , SQLModel , Relationship

class grille (SQLModel , table = True):
    IDGrille : Optional[int] = Field(default= None , primary_key= True)
    Grille : str