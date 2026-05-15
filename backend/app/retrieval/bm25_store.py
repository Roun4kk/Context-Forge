from rank_bm25 import BM25Okapi

bm25 = None
tokenized_chunks = []
stored_chunks = []


def build_bm25_index(chunks):

    global bm25
    global tokenized_chunks
    global stored_chunks

    stored_chunks = chunks

    tokenized_chunks = [
        chunk.text.lower().split()
        for chunk in chunks
    ]

    bm25 = BM25Okapi(tokenized_chunks)


def search_bm25(query, top_k=3):

    global bm25

    tokenized_query = query.lower().split()

    scores = bm25.get_scores(tokenized_query)

    ranked_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )[:top_k]

    return [
        {
            "chunk": stored_chunks[i].text,
            "metadata": stored_chunks[i],
            "score": float(scores[i])
        }
        for i in ranked_indices
    ]