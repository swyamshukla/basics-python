from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path, override=True)


loader=PyPDFLoader(file_path='attention.pdf')

docs = loader.load() 
# type -> list of documents.  [document(page_content, metadata)...........]


# Lets cook egg slowly
# load ✅

spliter = RecursiveCharacterTextSplitter(
    chunk_size=500,      
    chunk_overlap=50,
)

split_docs = spliter.split_documents(docs)

print(len(split_docs))

# chunk ✅

embeedd= OpenAIEmbeddings(model='text-embedding-3-small')


texts_list=[doc.page_content for doc in split_docs ]

vector= embeedd.embed_documents(texts_list) #manual embedding 

#embedding vector ✅


vector_store = Chroma.from_documents(
    documents=split_docs[:20],
    embedding=embeedd,
    collection_name="attention")

res= vector_store.similarity_search(query='who are authors of attention all u need',k=3) 


for i in res:
    print(i.page_content)
    print(i.metadata)
    print('----------------')
