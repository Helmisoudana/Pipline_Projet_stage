from typing import List, Optional ,TYPE_CHECKING
from sqlmodel  import Field , SQLModel , Relationship


if TYPE_CHECKING:
    from models.article import article


class arfamille(SQLModel , table = True):
    IDArFamille : Optional[int] = Field (default = None , primary_key= True )
    Famille : str
    Code : str

