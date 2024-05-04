from pydantic import BaseModel
from typing import List, Optional

class DocumentRequest(BaseModel):
    question: str
    documents: List[str]

class FactsResponse(BaseModel):
    question: str
    facts: Optional[List[str]] = None
    status: str

