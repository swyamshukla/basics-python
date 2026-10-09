from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from pathlib import Path
import dotenv

dotenv.load_dotenv()

env_path = Path(__file__).resolve().parent.parent / ".env"
dotenv.load_dotenv(env_path, override=True)

import streamlit as st      # Streamlit framework enables python scripts into interactive into interactive web apps, without writing any
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
#os.environ["LANGSMITH_ENDPOINT"]="https://api.smith.langchain.com"
os.environ["LANGSMITH_PROJECT"]="Chat Bot using LangchainOpenAI"



# create a prompt a template

prompt=ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant. Please response to the {input}")])

# create a chain

llm=ChatOpenAI(model="gpt-4o")
output=StrOutputParser()
chain=prompt|llm|output

st.title("Langchain Demo With OPENAI API")




input_text=st.text_input("Search the topic u want")

if input_text:
    st.write(chain.invoke({'input':input_text}))
