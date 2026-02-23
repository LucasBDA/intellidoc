# IntelliDoc

IntelliDoc is a **FastAPI-based API** that leverages artificial intelligence to analyze and extract information from documents uploaded by users. The solution employs large language models (LLMs) and agent creation techniques to classify content, detect important clauses, and provide structured risk analysis.

## Key Features

- File upload in various formats (PDF, CSV, HTML, etc.)
- Asynchronous document processing
- Text extraction and embedding generation
- Intelligent classification and risk analysis
- REST API with endpoints documented via OpenAPI/Swagger

## Project Structure

```
intellidoc/                  # repository root
├── api/                     # HTTP interface layer
│   ├── main.py              # instantiates FastAPI and registers routers
│   ├── routes/              # route definitions
│   │   └── documents.py     # document analysis endpoint
│   └── schemas/             # Pydantic schemas for request/response
│       └── document_schema.py
├── core/                    # central configuration and utilities
│   ├── config.py            # configuration loading
│   └── logger.py            # logging initialization
├── processors/              # file processing logic
│   ├── base_processor.py    # common base class
│   ├── pdf_processor.py
│   ├── html_processor.py
│   └── csv_processor.py
├── services/                # services coordinating data flow
│   ├── document_service.py  # orchestrates analysis and processor calls
│   └── llm_service.py       # language model integration
├── requirements.txt         # Python dependencies
└── README.md                # documentation for this project
```

## Getting Started

1. Create and activate a virtual environment (`python -m venv venv && venv\Scripts\Activate.ps1`).
2. Install dependencies (`pip install -r requirements.txt`).
3. Run the server with `uvicorn main:app --reload`.

---
