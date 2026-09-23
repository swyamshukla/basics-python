import dotenv
dotenv.load_dotenv()
from openai import OpenAI

client = OpenAI()

response = client.responses.create(model="gpt-6-astra", input="write 10 jokes on java developer")

print(response.output_text)