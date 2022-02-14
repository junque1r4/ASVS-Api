from pydantic import BaseModel
from typing import Optional


class Requirement(BaseModel):
    chapter_id: Optional[str] = None
    chapter_name: Optional[str] = None
    section_id: Optional[str] = None
    section_name: Optional[str] = None
    req_id: Optional[str] = None
    req_description: Optional[str]= None
    level1: Optional[bool] = None
    level2: Optional[bool] = None
    level3: Optional[bool] = None
    cwe: Optional[str] = None
    nist: Optional[str] = None

