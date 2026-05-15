from pydantic import BaseModel


class ChunkMetadata(BaseModel):

    chunk_id: int

    text: str

    source: str

    section: str