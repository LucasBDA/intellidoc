from processors.pdf_processor import PDFProcessor
from processors.csv_processor import CSVProcessor
from processors.html_processor import HTMLProcessor
from services.llm_service import LLMService

class DocumentService:

    def __init__(self):
        self.llm_service = LLMService()

    def analyze(self, filename: str, file_bytes: bytes):
        if filename.endswith(".pdf"):
            processor = PDFProcessor()
        elif filename.endswith(".csv"):
            processor = CSVProcessor()
        elif filename.endswith(".html"):
            processor = HTMLProcessor()
        else:
            raise ValueError("Unsupported file type")

        text = processor.extract_text(file_bytes)

        return self.llm_service.analyze_document(text)