from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('attention.pdf',extract_images=True)

print(loader.load())