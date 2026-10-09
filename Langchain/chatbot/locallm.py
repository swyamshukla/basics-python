from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"]="true"


os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


## Prompt Template
prompt=ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant. Please response to the user queries"),
    ("user", "Question:{question}")
])

## Chatbot with Ollama


llm=Ollama(model="qwen2.5-coder:3b")

## parser
output_parser=StrOutputParser()

chain = prompt | llm | output_parser

#streamlit
st.title("Ollama Chatbot with Langchain ")

input_text=st.text_input("Ask a question on any topic")

if st.button("Ask"):
    response = chain.invoke({"question": input_text})
    st.write(response)