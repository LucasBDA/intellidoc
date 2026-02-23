from pypdf import PdfReader
from io import BytesIO
from .base_processor import BaseProcessor

class PDFProcessor(BaseProcessor):

    def extract_text(self, file_bytes: bytes) -> str:
        reader = PdfReader(BytesIO(file_bytes))
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        return text