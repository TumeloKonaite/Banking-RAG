# 🏦 Banking RAG Assistant

> Retrieval-Augmented Generation over real banking documents  
> (account T&Cs, pricing guides, overdraft terms, risk docs, etc.)

---

<!-- ========================= -->
<!-- ⭐ TL;DR (Elevator Pitch) -->
<!-- ========================= -->

A modular **RAG (Retrieval-Augmented Generation)** system that:

- Ingests **banking PDFs** (terms & conditions, pricing guides, etc.)
- Splits them into chunks and embeds them with **OpenAI embeddings**
- Stores everything in a **Chroma** vector database
- Uses a **guardrailed LLM** (GPT) to answer banking questions
- Exposes an **interactive chat UI** via **Gradio**



---

<!-- =================== -->
<!-- 🗂 Project Overview -->
<!-- =================== -->

## 🗂 Project Overview

This repository implements a full RAG pipeline for banking content:

1. **Document ingestion** from local `data/` folder  
2. **Chunking** long PDFs into semantic pieces  
3. **Embedding** chunks using OpenAI (or HuggingFace as fallback)  
4. **Vector store** using Chroma (persistent on disk)  
5. **Retrieval** with metadata filters (e.g. `product_terms`, `pricing_guides`)  
6. **RAG pipeline** with strong guardrails and prompt-injection protection  
7. **Gradio chat UI** for demoing the assistant interactively  

The goal is **bank-grade behaviour**:  
no hallucinated fees, no invented rates, and clear “I don’t know” when context is missing.

---

<!-- =================== -->
<!-- 🧱 Folder Structure -->
<!-- =================== -->

## 🧱 Folder Structure

```text
Banking-rag/
├── .env.example          # Example env vars (no secrets)
├── .gitignore
├── README.md
│
├── data/                 # Banking PDFs go here
│   ├── product_terms/
│   ├── pricing_guides/
│   ├── risk_reports/
│   └── ...
│
├── artifacts/            # Generated artifacts (not committed)
│   ├── chunks/           # CSV / text chunks
│   └── vector_db/        # Chroma persistent DB
│
└── src/
    ├── ingestion/
    │   └── fetch_documents.py          # Load PDFs into Documents
    │
    ├── chunking/
    │   └── document_chunking.py        # Split Documents into chunks
    │
    ├── embedding/
    │   └── document_embedding.py       # Embed chunks (optional)
    │
    ├── vectorstore/
    │   └── vector_store.py             # Build Chroma DB
    │
    ├── retrieval/
    │   └── document_retriever.py       # Retrieve relevant chunks
    │
    └── rag/
        └── pipeline.py                 # RAG pipeline + guardrails
