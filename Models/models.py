from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    area: str
    id: str
    criticity: str
    cwe: Optional[str] = None
    NIST: Optional[str] = None
    requisito: str
