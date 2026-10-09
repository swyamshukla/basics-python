from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

from dotenv import load_dotenv
from pathlib import Path

import streamlit as st

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path, override=True)


# format the prompt to be a chat prompt
prompt = ChatPromptTemplate.from_messages([
    ('system', 'You are an AI assistant explain in eassay '),
    ('user', 'question:{text}')
])

#chatModel 

llm=ChatOpenAI(model='gpt-4o')

# pipeline

parser = StrOutputParser()

pipe = prompt|llm|parser

#streaminit

st.title("This is chatModel of \'gpt-4o\' with pedophile aistant")

input_text = st.chat_input("Enter the OpenAi Prompt")

if input_text:
    st.write(pipe.invoke({'text':input_text}))


local =Ollama(model='qwen2.5-coder:3b')

promptLocal = ChatPromptTemplate.from_messages([
    ('system', 'You are an AI assistant explain in poem '),
    ('user', 'question:{text_poem}')
])


pipe2=promptLocal|local|parser

st.write()
st.header("local LLm ")
input_text_local = st.chat_input("Enter the Local llm poem Prompt")

if input_text_local:
    st.write(pipe2.invoke({'text_poem':input_text_local}))


st.badge("Made with ❤️ by Langchain")

    
