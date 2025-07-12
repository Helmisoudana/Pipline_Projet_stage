from typing import Optional 
from sqlmodel  import Field , SQLModel , Relationship

class codebarre(SQLModel , table = True):
    IDCodeBarre : Optional[int] = Field(default= None , primary_key= True)
    CodeBarre : str
    IdEntite : int
    IdTaille : int
    IDAr_Couleur : int
    NumInterne : int
