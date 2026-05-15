import faiss
import numpy as np

dimension = 384

index = faiss.IndexFlatIP(dimension)

stored_chunks = []


def add_to_faiss(chunks, embeddings):

    global stored_chunks

    embeddings = np.array(
        embeddings
    ).astype("float32")

    faiss.normalize_L2(embeddings)

    index.add(embeddings)

    stored_chunks.extend(chunks)


def search_faiss(query_embedding, top_k=3):

    query_embedding = np.array(
        [query_embedding]
    ).astype("float32")

    faiss.normalize_L2(query_embedding)

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for i, idx in enumerate(indices[0]):

        if idx < len(stored_chunks):

            results.append({
                "chunk": stored_chunks[idx].text,
                "metadata": stored_chunks[idx],
                "score": float(distances[0][i])
            })

    return results