import openai
from altair import Literal

from charon.utils.config import CONFIG

client = openai.OpenAI(api_key=CONFIG["OPENAI_API_KEY"])


def chat_completion(
    messages,
    model: Literal["gpt-3.5-turbo", "gpt4"] = "gpt-3.5-turbo",
):
    """
    Get a chat completion from the openai api

    :param messages: The messages to send to the chat
    :type messages: List[ChatHistoryEntry]
    :param model: The model to use, defaults to "gpt-3.5-turbo"
    :type model: Literal["gpt-3.5-turbo", "gpt4"], optional
    :return: The chat completion
    """
    return client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
