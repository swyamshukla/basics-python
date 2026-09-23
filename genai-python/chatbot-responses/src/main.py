import dotenv
import openai

dotenv.load_dotenv()

client = openai.OpenAI()

response =client.responses.create(model="gpt-4o",input="Write a story on Java developer story ")

print(response.output_text)
