from fastapi import FastAPI

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
from pathlib import Path

import os
from model import InputResponse

load_dotenv()

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path, override=True)

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true" # LANGSMITH TACKING 


#chatModel of OpenAI
llm=ChatOpenAI(model_name="gpt-4o")

#prompt template 
prompt=ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please answer the following question:"),
    ("user", "questions : {question} and the number of word should not exceed more than {words}")
])

#piplinema
pipe = prompt|llm|StrOutputParser()


# create object of FastAPI
app=FastAPI()


@app.post("/chat")
async def chat(data: InputResponse):
    response =pipe.invoke({"question":data.question,"words":data.words})
    return response



