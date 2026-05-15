from fastapi import FastAPI
from app.api.upload import router as upload_router
from app.api.rag import (
    router as rag_router
)

app = FastAPI(
    title="ContextForge",
    version="0.1.0"
)

app.include_router(upload_router)
app.include_router(rag_router)

@app.get("/")
async def root():
    return {
        "message": "ContextForge backend running"
    }