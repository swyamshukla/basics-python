from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path, override=True)

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')



loader=PyPDFLoader(file_path='attention.pdf')

documents=loader.load()

chunker=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=150,keep_separator=True)

chunk=chunker.split_documents(documents=documents)


print(len(documents))  # -> list of documents they are 1 pdf page 1 chunk 
#-> not better to have because context length, size, token, etc. can be different for different documents
print(len(chunk))  # -> list of chunks they are 1000 character 1 chunk 


embedd=OpenAIEmbeddings(model='text-embedding-3-small')

texts = [doc.page_content for doc in chunk]
vector=embedd.embed_documents(texts)


vector_store = Chroma.from_documents(
    documents=chunk,
    embedding=embedd,
    collection_name="attention"
)

results=vector_store.similarity_search(query='who is Denny Britz',k=3) # -> list of documents they are 1000 words 1 chunk )

print(results)