from app.retrieval.bm25_store import (
    search_bm25
)

from app.retrieval.vector_store import (
    search_faiss
)

from app.retrieval.embedder import (
    model
)

from app.ranking.mmr import (
    mmr_rerank
)

import numpy as np


def normalize_scores(scores):

    scores = np.array(scores)

    min_score = scores.min()
    max_score = scores.max()

    if max_score - min_score == 0:
        return [1.0 for _ in scores]

    normalized = (
        (scores - min_score)
        / (max_score - min_score)
    )

    return normalized.tolist()


def hybrid_search(query, top_k=5):

    # Generate query embedding once
    query_embedding = model.encode(query)

    # Retrieve candidates
    semantic_results = search_faiss(
        query_embedding,
        top_k=15
    )

    keyword_results = search_bm25(
        query,
        top_k=15
    )

    # Normalize semantic scores
    semantic_scores = normalize_scores(
        [
            result["score"]
            for result in semantic_results
        ]
    )

    # Normalize BM25 scores
    bm25_scores = normalize_scores(
        [
            result["score"]
            for result in keyword_results
        ]
    )

    combined_results = {}

    # Semantic fusion
    for idx, result in enumerate(
        semantic_results
    ):

        chunk_text = result["chunk"]

        metadata = result["metadata"]

        semantic_score = semantic_scores[idx]

        if chunk_text not in combined_results:

            combined_results[chunk_text] = {
                "score": 0,
                "metadata": metadata
            }

        combined_results[chunk_text]["score"] += (
            0.7 * semantic_score
        )

    # BM25 fusion
    for idx, result in enumerate(
        keyword_results
    ):

        chunk_text = result["chunk"]

        metadata = result["metadata"]

        bm25_score = bm25_scores[idx]

        if chunk_text not in combined_results:

            combined_results[chunk_text] = {
                "score": 0,
                "metadata": metadata
            }

        combined_results[chunk_text]["score"] += (
            0.3 * bm25_score
        )

    # Sort by combined score
    ranked_results = sorted(
        combined_results.items(),
        key=lambda x: x[1]["score"],
        reverse=True
    )

    # Candidate pool
    candidate_chunks = [
        item[0]
        for item in ranked_results
    ]

    candidate_metadata = [
        item[1]["metadata"]
        for item in ranked_results
    ]

    # Generate embeddings for MMR
    candidate_embeddings = model.encode(
        candidate_chunks
    )

    # Apply MMR reranking
    reranked_chunks = mmr_rerank(
        query_embedding=query_embedding,
        candidate_embeddings=candidate_embeddings,
        candidates=candidate_chunks,
        top_k=top_k
    )

    # Preserve metadata after reranking
    final_results = []

    for chunk in reranked_chunks:

        for idx, original_chunk in enumerate(
            candidate_chunks
        ):

            if chunk == original_chunk:

                final_results.append({
                    "chunk": chunk,
                    "metadata": candidate_metadata[idx]
                })

                break

    return final_results