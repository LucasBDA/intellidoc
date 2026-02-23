from pydantic import BaseModel
from typing import List

class DocumentAnalysisResponse(BaseModel):
    main_subject: str
    important_clauses: List[str]
    risk_factors: List[str]
    document_type: str