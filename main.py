import os
import openai

os.environ['OPENAI_API_KEY'] = "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"

openai.api_key = os.getenv("OPENAI_API_KEY")

question = input("\033[31mWhat is your question? \n")

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an assistant. Answer thew "
                                      "question"},
        {"role": "user", "content": question}
    ]
)
print(completion.choices[0].message.content)
