import openai

from charon.utils.config import CONFIG

client = openai.OpenAI(api_key=CONFIG["OPENAI_API_KEY"])


def chat_completion(messages):
    return client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
    )
