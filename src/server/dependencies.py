"""
Shared dependency helpers for server-facing modules.
"""

from functools import lru_cache

from src.pipeline.rag_pipeline import RAGPipeline


@lru_cache(maxsize=1)
def get_pipeline() -> RAGPipeline:
    """
    Lazily instantiate a single RAGPipeline instance for reuse across
    FastAPI routes and the Gradio UI.
    """
    return RAGPipeline()
