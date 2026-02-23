from bs4 import BeautifulSoup
from .base_processor import BaseProcessor

class HTMLProcessor(BaseProcessor):

    def extract_text(self, file_bytes: bytes) -> str:
        soup = BeautifulSoup(file_bytes, "html.parser")
        return soup.get_text(separator="\n")