import dotenv
import openai

dotenv.load_dotenv()

client=openai.OpenAI()


response= client.chat.completions.create(model="gpt-4o",
                              messages=[
                                  # this is system prompt 
                                  {
                                      "role":"system",
                                      "content":"you are a pirate of sea, and educator and java developer  by profession "

                                  },
                                  {
                                      "role":"user",
                                      "content":"what is java"
                                  }
                              ])


print(response.choices[0].message.content)