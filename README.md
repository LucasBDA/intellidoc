# IntelliDoc

IntelliDoc é uma **API baseada em FastAPI** que utiliza inteligência artificial para analisar e extrair informações de documentos carregados pelo usuário. A solução emprega modelos de linguagem grande (LLMs) e técnicas de criação de agentes para classificar conteúdo, detectar cláusulas importantes e oferecer análises de risco estruturadas.

## Principais funcionalidades

- Upload de arquivos em diversos formatos (PDF, CSV, HTML etc.)
- Processamento assíncrono dos documentos
- Extração de texto e geração de embeddings
- Classificação inteligente e análise de riscos
- API REST com endpoints documentados via OpenAPI/Swagger

## Estrutura do projeto

```
intellidoc/                  # raiz do repositório
├── api/                     # camada de interface HTTP
│   ├── main.py              # instancia FastAPI e registra routers
│   ├── routes/              # definicao de rotas
│   │   └── documents.py     # endpoint de análise de documentos
│   └── schemas/             # Pydantic schemas de request/response
│       └── document_schema.py
├── core/                    # configurações e utilitários centrais
│   ├── config.py            # carregamento de configurações
│   └── logger.py            # inicialização de logging
├── processors/              # lógica de processamento de arquivos
│   ├── base_processor.py    # classe base comum
│   ├── pdf_processor.py
│   ├── html_processor.py
│   └── csv_processor.py
├── services/                # serviços que coordenam o fluxo de dados
│   ├── document_service.py  # orquestra análise e chamada aos processors
│   └── llm_service.py       # integração com modelos de linguagem
├── requirements.txt         # dependências do Python
└── README.md                # documentação deste projeto
```

## Execução

1. Crie e ative um ambiente virtual (`python -m venv venv && venv\Scripts\Activate.ps1`).
2. Instale dependências (`pip install -r requirements.txt`).
3. Execute o servidor com `uvicorn api.main:app --reload`.

---
