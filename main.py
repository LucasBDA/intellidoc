from fastapi import FastAPI
from fastapi.responses import FileResponse
from api.routes import documents

app = FastAPI(
    title="IntelliDock API",
    description="AI-powered document analysis API",
    version="1.0.0"
)

app.include_router(documents.router, prefix="/documents", tags=["Documents"])

@app.get("/")
def root():
    return {"message": "IntelliDock is running"}

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")