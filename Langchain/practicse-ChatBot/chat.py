from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pathlib import Path
from dotenv import load_dotenv
import os
import streamlit as st

# format the prompt to be a chat prompt



env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path, override=True)

load_dotenv()


os.environ['OPEN_AI_API_KEY']=os.getenv("OPENAI_API_KEY")
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']='true'


llm=ChatOpenAI(model='gpt-4o')

prompt = ChatPromptTemplate.from_messages([
    ('system', 'You are an AI assistant.'),
    ('user', '{input}')
])

parser = StrOutputParser()
pipe = prompt|llm|parser

st.title("langchain demo with OpenAI API")

input_text = st.chat_input("Enter your prompt")

if input_text:

    st.write(pipe.invoke({'input': input_text}))


st.balloons()

