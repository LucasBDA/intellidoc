import csv
from io import StringIO
from .base_processor import BaseProcessor

class CSVProcessor(BaseProcessor):

    def extract_text(self, file_bytes: bytes) -> str:
        content = file_bytes.decode("utf-8")
        reader = csv.reader(StringIO(content))
        rows = [" | ".join(row) for row in reader]
        return "\n".join(rows)