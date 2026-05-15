from fastapi import APIRouter

from app.retrieval.hybrid_search import (
    hybrid_search
)

from app.generation.llm import (
    generate_response
)

router = APIRouter()


@router.get("/rag")
async def rag(query: str):

    retrieved_results = hybrid_search(query)

    chunks = [
        result["chunk"]
        for result in retrieved_results
    ]

    response = generate_response(
        query,
        chunks
    )

    return {
        "query": query,
        "retrieved_chunks": chunks,
        "response": response
    }