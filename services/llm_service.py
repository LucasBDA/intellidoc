from google import genai
import re
from google.genai import types
from core.config import settings
import json

class LLMService:

    def __init__(self):
        self.client = genai.Client(api_key=settings.GOOGLE_API_KEY)

    def analyze_document(self, text: str) -> dict:
        prompt = f"""
        Analyze the following document and return a JSON in this format:

        {{
            "main_subject": "",
            "important_clauses": [],
            "risk_factors": [],
            "document_type": ""
        }}

        Document:
        {text}
        """

        response = self.client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=[prompt]
        )

        #Parseamento do JSON da resposta do modelo
        raw_text = response.text.strip()
        raw_text = re.sub(r"```json", "", raw_text)
        raw_text = re.sub(r"```", "", raw_text)
        match = re.search(r"\{.*\}", raw_text, re.DOTALL)
        if not match:
            raise ValueError(f"Could not extract JSON from model response: {raw_text}")

        json_text = match.group(0)

        return json.loads(json_text)