from fastapi import APIRouter, UploadFile, File, HTTPException
from services.document_service import DocumentService
from api.schemas.document_schema import DocumentAnalysisResponse

router = APIRouter()
document_service = DocumentService()

@router.post("/analyze", response_model=DocumentAnalysisResponse)
async def analyze_document(file: UploadFile = File(...)):
    try:
        content = await file.read()
        result = document_service.analyze(file.filename, content)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))