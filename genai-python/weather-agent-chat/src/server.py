from openai import OpenAI
from dotenv import load_dotenv
import requests
load_dotenv()


def main():
    # Initialize the OpenAI client
    client = OpenAI()
    str= input('>')
    # Send a chat completion request to GPT-4

    res = client.chat.completions.create(model='gpt-4o',
        messages=[{"role": "user", "content": str}])
    print(res.choices[0].message.content)


#main()



def weather_api():
    city = input('Enter the city name: ')
    # Construct the URL for the weather API
    url=f"https://wttr.in/{city.lower()}?format=%C+%t"
    res= requests.get(url)
    return res.text if res.status_code==200 else "something went wrong"





print(weather_api())


