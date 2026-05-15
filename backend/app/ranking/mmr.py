import numpy as np

from sklearn.metrics.pairwise import (
    cosine_similarity
)


def mmr_rerank(
    query_embedding,
    candidate_embeddings,
    candidates,
    top_k=5,
    lambda_param=0.7
):

    selected = []

    selected_indices = []

    candidate_indices = list(
        range(len(candidates))
    )

    similarity_to_query = cosine_similarity(
        [query_embedding],
        candidate_embeddings
    )[0]

    first_idx = np.argmax(
        similarity_to_query
    )

    selected.append(
        candidates[first_idx]
    )

    selected_indices.append(
        first_idx
    )

    candidate_indices.remove(
        first_idx
    )

    while (
        len(selected) < top_k
        and candidate_indices
    ):

        mmr_scores = []

        for idx in candidate_indices:

            relevance = similarity_to_query[idx]

            redundancy = max([
                cosine_similarity(
                    [candidate_embeddings[idx]],
                    [candidate_embeddings[selected_idx]]
                )[0][0]

                for selected_idx
                in selected_indices
            ])

            mmr_score = (
                lambda_param * relevance
                - (1 - lambda_param)
                * redundancy
            )

            mmr_scores.append(
                (idx, mmr_score)
            )

        best_idx = max(
            mmr_scores,
            key=lambda x: x[1]
        )[0]

        selected.append(
            candidates[best_idx]
        )

        selected_indices.append(
            best_idx
        )

        candidate_indices.remove(
            best_idx
        )

    return selected