import os
import pickle
from typing import List
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()


embedding = HuggingFaceEmbeddings()

available_models = [
    "deepseek-r1-distill-llama-70b",
    "llama-3.3-70b-versatile",
    "gemma2-9b-it",
    "mixtral-8x7b-32768",
    "deepseek-r1-distill-qwen-32b",
]

file_path = "vector_index.pkl"
def get_llm(model_name):
    if model_name in available_models:
        return ChatGroq(model=model_name, temperature=0)
    else:
        return ChatGroq(model="deepseek-r1-distill-llama-70b", temperature=0)


def process_urls (urls : List[str]):
    loaders = UnstructuredURLLoader(urls =urls)
    data = loaders.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000, 
        chunk_overlap =200,
    )

    docs = text_splitter.split_documents(data)

    vector_index = FAISS.from_documents(docs,embedding)

    
    with open(file_path,"wb") as f:
        pickle.dump(vector_index,f)

   
            
    return 0


def answer_query(query: str):
    llm = get_llm("llama-3.3-70b-versatile")
    response ={}
    if os.path.exists(file_path):
        with open(file_path,"rb") as f:
            vector_index = pickle.load(f)

            retriever = vector_index.as_retriever()
            chain = RetrievalQAWithSourcesChain.from_chain_type(
                llm=llm,
                chain_type="stuff",  # map_reduce - large documents, refine - slow as it requires multiple llm calls, map_rerank - rank based, higher rank answer is given as output
                retriever=retriever,
            )

            response = chain.invoke({"question": query})
            return response
    return None

