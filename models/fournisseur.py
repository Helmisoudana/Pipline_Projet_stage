from typing import Optional 
from sqlmodel  import Field , SQLModel , Relationship

class fournisseur (SQLModel , table = True):
    IDFournisseur : Optional[int] = Field(default= None ,primary_key=True)
    Fournisseur : str 
    Adresse : str 
    Code : str