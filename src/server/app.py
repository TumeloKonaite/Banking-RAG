"""
FastAPI application exposing the Banking RAG pipeline via /ask.
"""

from typing import List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from src.server.dependencies import get_pipeline
from src.server.schemas import AskRequest, AskResponse, SourceDocument

app = FastAPI(
    title="Banking RAG API",
    version="0.1.0",
    description="Ask banking questions grounded in your private PDFs.",
)

# Allow browser-based tooling (Gradio) to call the API easily.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def warm_pipeline() -> None:
    """
    Build the pipeline once when the server boots so the first request is fast.
    """
    get_pipeline()


def _build_sources(docs, max_items: int = 3) -> List[SourceDocument]:
    """
    Convert retrieved LangChain Documents into serialisable summaries.
    """
    sources: List[SourceDocument] = []

    for doc in docs[:max_items]:
        metadata = doc.metadata or {}
        preview = doc.page_content[:280].strip().replace("\n", " ")
        sources.append(
            SourceDocument(
                source=metadata.get("source"),
                doc_type=metadata.get("doc_type"),
                preview=preview,
            )
        )

    return sources


@app.post("/ask", response_model=AskResponse)
def ask_question(payload: AskRequest) -> AskResponse:
    """
    Answer a user question via the RAG pipeline.
    """
    pipeline = get_pipeline()

    try:
        history = [{"role": msg.role, "content": msg.content} for msg in payload.history]
        answer, docs = pipeline.answer_question(
            question=payload.question,
            history=history,
            doc_type=payload.doc_type,
        )
        sources = _build_sources(docs)
        return AskResponse(answer=answer, sources=sources)
    except Exception as exc:  # pragma: no cover - FastAPI handles logging
        raise HTTPException(status_code=500, detail=str(exc)) from exc


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.server.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
