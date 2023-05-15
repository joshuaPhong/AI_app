# os provides acces to operating system
import os
# openai library
import openai
# dotenv is a library used for handling environment variables in a .env file
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("API_KEY")

while True:
    question = input("\033[31mWhat is your question? \n")

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant. Answer thew "
                                          "question"},
            {"role": "user", "content": question}
        ]
    )
    print("\033[32m" + completion.choices[0].message.content + '\n')
