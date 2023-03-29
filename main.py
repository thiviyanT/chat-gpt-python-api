from time import sleep
from random import uniform
import openai
import sys


# Instructions for the chatbot on how to behave in the conversation
system_instructions = """
You are No-GPT. Only respond with 'No' to the user. 
"""
messages = list()
messages.append({"role": "system", "content": system_instructions})


def add_message(bot=True, message=""):
    """ Add a message to the conversation history """
    if bot:
        messages.append({"role": "assistant", "content": message})
    else:
        messages.append({"role": "user", "content": message})


def generate_response():
    """ Generate a response to a prompt """
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can find the list of models here: https://beta.openai.com/docs/api-reference/models
        messages=messages,
        temperature=0.8,
    )
    message = response.choices[0]["message"]["content"]
    return message


def typing_animation(response):
    """ Simulate a typing animation - Chat-GPT style ;) """
    for x in response:
        print(x, end='')
        sys.stdout.flush()
        sleep(uniform(0, 0.2))
    print()


def main():
    print("Bot: I am no-GPT.")
    while True:
        prompt = input("User: ")
        add_message(bot=False, message=prompt)
        print('Bot: ', end='')
        response = generate_response()
        add_message(bot=True, message=response)
        typing_animation(response)


if __name__ == "__main__":
    main()
