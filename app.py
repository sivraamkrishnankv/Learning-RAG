from src.data_loader import load_all_documents
from src.embedding import EmbeddingPipeline
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

# Example usage
if __name__ == "__main__":
    docs = load_all_documents("data")
    store = FaissVectorStore("faiss_store")
    # uncomment the below line only while uploading new docs
    # store.build_from_documents(docs) 
    store.load()
    rag_search = RAGSearch()
    query = "Who is sivraam?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # test to check chunks
    # docs = load_all_documents("data")
    # chunks=EmbeddingPipeline().chunk_documents(docs)
    # chunkvectors=EmbeddingPipeline().embed_chunks(docs)
    # print(chunkvectors)
    # store = FaissVectorStore("faiss_store")