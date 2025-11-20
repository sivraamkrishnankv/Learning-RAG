# RAG (Retrieval-Augmented Generation) System

A complete RAG pipeline implementation for document processing, embedding, vector storage, and intelligent question-answering using Faiss and Google Gemini.

## 📋 Overview

This project implements a full-featured Retrieval-Augmented Generation system that can:
- Process multiple document formats (PDF, TXT, CSV, Excel, Word, JSON)
- Generate embeddings using Sentence Transformers
- Store vectors in Faiss for efficient similarity search
- Answer questions using Google Gemini LLM with retrieved context

## 🏗️ Architecture
Documents → Text Chunks → Embeddings → Faiss Vector Store → Query → Retrieval → LLM Generation

## 📄 Supported Document Formats
- PDF (`.pdf`) via `PyPDFLoader`
- Text (`.txt`) via `TextLoader`
- CSV (`.csv`) via `CSVLoader`
- Excel (`.xls`, `.xlsx`) via `UnstructuredExcelLoader`
- Word (`.docx`) via `Docx2txtLoader`
- JSON (`.json`) via `JSONLoader`

## ✨ Key Features
- Multi-format document ingestion with detailed logging and error handling
- Recursive text chunking with configurable size and overlap
- High-quality embeddings using `all-MiniLM-L6-v2` (Sentence Transformers)
- Faiss-based vector store with persistence and metadata tracking
- Semantic search with top-k retrieval and distance metadata
- Gemini-powered summarization grounded in retrieved context

## ✨ Execution Method

- Create a virtual env and download all requirements from `requirements.txt`
- add pdfs or any other previously metnioned files to `data` folder
- Run `app.py` file to initiate vector DB creation followed by query searching
- make sure to add `.env` folder with valid gemini api key in the name of `GEMINI_API_KEY`
---

**Made with ❤️ by SIV RAAM KRISHNAN.K.V**