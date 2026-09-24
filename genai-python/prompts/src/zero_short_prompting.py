from openai import OpenAI
from dotenv import load_dotenv
import json
load_dotenv()

client = OpenAI()


# Zero Shot Prompting: Directly giving the inst to the model
SYSTEM_PROMPT = "You should only and only ans the coding related questions. Do not ans anything else. Your name is Alexa. If user asks something other than coding, just say sorry .json"

mess=[{"role":"system","content":SYSTEM_PROMPT}]
str= input("enter the user input: ")
mess.append({"role":"user","content": str})

res = client.chat.completions.create(model='gpt-4o', 
                                       response_format={"type": "json_object"},messages=mess
                                     
                                )

raw = json.loads(res.choices[0].message.content)

print(
    raw
)
