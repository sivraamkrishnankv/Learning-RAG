# RAG Pipeline Implementation - Project Documentation

## 📋 Project Overview

This project implements a complete **Retrieval-Augmented Generation (RAG) pipeline** for document ingestion, embedding, and retrieval. The system processes PDF documents, converts them into vector embeddings, stores them in a vector database, and enables semantic search capabilities.

## 🏗️ Architecture

The RAG pipeline consists of four main components:

1. **Document Loading** - Extract text from PDF files
2. **Text Splitting** - Chunk documents for optimal retrieval
3. **Embedding Generation** - Convert text to vector embeddings
4. **Vector Storage & Retrieval** - Store and query documents using ChromaDB



## 🔧 Implementation Details

### 1. Document Loading (`pdf_loader.ipynb`)

**Function: `process_all_pdfs()`**
- Recursively finds all PDF files in a directory
- Uses `PyPDFLoader` from LangChain to extract text
- Adds metadata (source file, file type) to each document
- Handles errors gracefully

**Results:**
- Processed 3 PDF files
- Extracted 23 pages total
- Files processed:
  - `714022201098_SIVRAAMKRISHNAN.pdf` (2 pages)
  - `FTH-Quaterly-Insight-Sep-2025.pdf` (20 pages)
  - `SivRaamKrishnan.pdf` (1 page)

### 2. Text Splitting

**Function: `split_documents()`**
- Uses `RecursiveCharacterTextSplitter` from LangChain
- **Chunk size:** 1000 characters
- **Chunk overlap:** 200 characters (maintains context between chunks)
- **Separators:** `["\n\n", "\n", " ", ""]` (hierarchical splitting)

**Results:**
- Split 23 documents into **76 chunks**
- Each chunk preserves metadata from original document

### 3. Embedding Generation

**Class: `EmbeddingManager`**
- **Model:** `all-MiniLM-L6-v2` (Sentence Transformers)
- **Embedding dimension:** 384
- Generates dense vector representations of text chunks
- Supports batch processing with progress bars

**Key Features:**
- Lazy loading of the model
- Error handling for model loading
- Efficient batch encoding

### 4. Vector Storage

**Class: `VectorStore`**
- **Database:** ChromaDB (persistent vector database)
- **Collection name:** `pdf_documents`
- **Storage location:** `../data/vector_store/`
- Generates unique IDs for each document chunk
- Stores embeddings, metadata, and original text

**Features:**
- Persistent storage (data survives restarts)
- Automatic collection creation
- Metadata preservation
- Document counting and tracking

**Current Status:**
- **169 documents** stored in the vector store

### 5. Retrieval System

**Class: `RAGRetriever`**
- Takes a query string and returns relevant documents
- Uses the same embedding model for query encoding
- Performs cosine similarity search in ChromaDB
- Filters results by similarity score threshold

**Parameters:**
- `top_k`: Number of results to return (default: 5)
- `score_threshold`: Minimum similarity score (default: -0.5)

**Query Process:**
1. Generate embedding for the query
2. Search ChromaDB using cosine similarity
3. Convert distances to similarity scores (1 - distance)
4. Filter by threshold
5. Return ranked results with metadata

## 🐛 Issues Encountered & Solutions

### Issue 1: Import Error
**Problem:** `ModuleNotFoundError: No module named 'langchain.text_splitter'`

**Solution:** 
- Updated import to `from langchain_text_splitters import RecursiveCharacterTextSplitter`
- Added `langchain-text-splitters` to `requirements.txt`
- LangChain restructured text splitters into a separate package

### Issue 2: Zero Retrieval Results
**Problem:** Query "who is sivraam" returned 0 documents despite documents being in the database

**Root Cause:**
- ChromaDB was returning documents correctly
- Similarity scores were negative (~-0.30) due to high cosine distances
- Default `score_threshold: 0.0` filtered out all results

**Solution:**
- Lowered `score_threshold` to `-0.5` to allow negative similarity scores
- Added debug output to inspect ChromaDB results structure
- Verified that documents were being retrieved but filtered out

**Key Learning:** 
- Cosine distance ranges from 0 (identical) to 2 (opposite)
- Similarity = 1 - distance, so high distances result in negative similarities
- Need to adjust thresholds based on embedding model characteristics

## 📊 Current Status

### Working Components ✅
- ✅ PDF document loading and processing
- ✅ Text chunking with overlap
- ✅ Embedding generation using Sentence Transformers
- ✅ Vector storage in ChromaDB
- ✅ Document retrieval with similarity search
- ✅ Metadata preservation throughout pipeline

### Test Results
- **Query:** "who is sivraam"
- **Results:** Successfully retrieves 5 relevant documents
- **Documents contain:** Resume information about SIV RAAM KRISHNAN

## 🔍 Key Technical Decisions

1. **Embedding Model:** Chose `all-MiniLM-L6-v2` for balance between quality and speed
2. **Chunk Size:** 1000 characters with 200 overlap for context preservation
3. **Vector DB:** ChromaDB for simplicity and persistence
4. **Similarity Metric:** Cosine similarity (default in ChromaDB)

## 📚 Dependencies
langchain
langchain-community
langchain-core
langchain-text-splitters
pypdf
pymupdf
sentence-transformers
faiss-cpu
chromadb
hf_xet


## 🚀 Usage Example

```python
# Initialize components
embedding_manager = EmbeddingManager()
vectorstore = VectorStore()
rag_retriever = RAGRetriever(vectorstore, embedding_manager)

# Query the system
results = rag_retriever.retrieve("who is sivraam", top_k=5, score_threshold=-0.5)

# Access results
for doc in results:
    print(f"Score: {doc['similarity_score']:.4f}")
    print(f"Content: {doc['content'][:200]}...")
    print(f"Source: {doc['metadata']['source_file']}")
```

## 🎯 Next Steps / Future Improvements

1. **Query Enhancement:**
   - Implement query expansion techniques
   - Add re-ranking for better relevance
   - Support multi-query retrieval

2. **Performance:**
   - Experiment with different embedding models
   - Optimize chunk sizes for specific document types
   - Add caching for frequent queries

3. **Features:**
   - Add LLM integration for answer generation
   - Implement hybrid search (keyword + semantic)
   - Add document update/deletion capabilities
   - Create a user interface for querying

4. **Monitoring:**
   - Track retrieval quality metrics
   - Log query patterns
   - Monitor embedding generation time

## 💡 Key Learnings

1. **Vector Similarity:** Understanding cosine distance vs similarity scores is crucial
2. **Threshold Tuning:** Similarity thresholds need to be adjusted based on the embedding model
3. **Chunking Strategy:** Overlap is essential for maintaining context across chunks
4. **Metadata Preservation:** Keeping source information helps with result interpretation
5. **Debugging:** Inspecting raw ChromaDB results helps identify filtering issues

## 📝 Notes

- The system successfully processes and retrieves documents from PDFs
- ChromaDB provides persistent storage, so embeddings don't need to be regenerated
- The current implementation focuses on retrieval; answer generation can be added as a next step
- Similarity scores may vary based on query phrasing and document content

---

**Project Status:** ✅ Core RAG Pipeline Complete