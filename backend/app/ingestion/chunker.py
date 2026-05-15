from nltk.tokenize import sent_tokenize

from app.models.chunk import (
    ChunkMetadata
)


def chunk_text(
    text: str,
    source: str,
    chunk_size: int = 3,
    overlap: int = 1
):

    sentences = sent_tokenize(text)

    chunks = []

    start = 0

    chunk_id = 0

    while start < len(sentences):

        end = start + chunk_size

        chunk_text = " ".join(
            sentences[start:end]
        )

        chunk = ChunkMetadata(
            chunk_id=chunk_id,
            text=chunk_text,
            source=source,
            section="general"
        )

        chunks.append(chunk)

        chunk_id += 1

        start += chunk_size - overlap

    return chunks