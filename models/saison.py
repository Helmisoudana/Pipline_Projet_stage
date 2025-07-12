from typing import Optional , List , TYPE_CHECKING
from sqlmodel  import Field , SQLModel , Relationship
if TYPE_CHECKING :
    from models.article import article
class saison ( SQLModel , table = True):
    IDSaison : Optional[int] = Field(default=None , primary_key= True)
    Saison : str
    Code : str
    Ordre : str