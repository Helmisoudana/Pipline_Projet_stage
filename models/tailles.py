from typing import Optional 
from sqlmodel  import Field , SQLModel , Relationship

class tailles ( SQLModel , table = True):
    IdTaille : Optional[int] = Field(default = None , primary_key= True)
    LibTaille : str
    IDGrille : Optional[int] = Field(foreign_key="grille.IDGrille")
