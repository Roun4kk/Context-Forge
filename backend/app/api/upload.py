import os
from fastapi import APIRouter, UploadFile, File
from app.ingestion.chunker import chunk_text

from app.retrieval.embedder import (
    generate_embeddings
)

from app.retrieval.vector_store import (
    add_to_faiss
)

from app.retrieval.bm25_store import (
    build_bm25_index
)

from app.ingestion.pdf_parser import extract_text_from_pdf

router = APIRouter()

UPLOAD_DIR = "data"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    extracted_text = extract_text_from_pdf(file_path)
    chunks = chunk_text(
        extracted_text,
        source=file.filename
    )
    embeddings = generate_embeddings(chunks)

    add_to_faiss(
        chunks,
        embeddings
    )

    build_bm25_index(chunks)
    return {
        "filename": file.filename,
        "characters_extracted": len(extracted_text),
        "chunks_created": len(chunks),
        "status": "indexed successfully"
    }