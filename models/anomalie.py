from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Anomalie(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    IDArticle: Optional[int]
    Code: Optional[str]
    Type: Optional[str]
    message: str
    date_detection: datetime = Field(default_factory=datetime.utcnow)