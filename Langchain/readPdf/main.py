from langchain_community.document_loaders import PyPDFLoader

def load_pdf(url):
    loader = PyPDFLoader(file_path=url)
    

    pages = loader.load() # unnified Document object , consist of content and metadata
    print(loader) # Document object
    print(pages)
    print(len(pages))
    #pages.append("this is a docs")
    #print(pages[-1])
    #print(pages[0].page_content)


#load_pdf('attention.pdf')

#load_pdf('https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf')

from langchain_community.document_loaders.text import TextLoader
from langchain_core.documents import Document


def load_text(file):

    loader =TextLoader(file_path=file)
    print(loader) # Document object
    docs = loader.load() # Document object
    print(docs[0].page_content)
    doc= Document(page_content=docs[0].page_content, metadata={"source": file})
    print(doc.page_content)



#load_text('speech.txt')
load_pdf('attention.pdf')

    
