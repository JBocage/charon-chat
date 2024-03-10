import json
import os
import pathlib
from typing import List, Literal, TypedDict

from charon.utils.config import CONFIG
from charon.utils.paths import Paths


class ChatHistoryEntry(TypedDict):
    """Describes a message from the openai api chat"""

    role: Literal["system", "assistant", "user"]

    #: The content of the message
    content: str


class HistoryEntryAlreadyExistsError(Exception):
    """Raised when a history entry already exists"""


class HistoryEntryDoesNotExistError(Exception):
    """Raised when a history entry does not exist"""


def list_history_entries() -> List[str]:
    """Returns the list of all available chat histories"""
    return [
        pathlib.Path(filename).stem
        for filename in os.listdir(Paths.DATA / "chat_history")
        if filename.endswith(".json")
    ]


def get_history(filename_stem: str) -> List[ChatHistoryEntry]:
    """Get the history content

    :param filename_stem: The filename stem (without suffix) of the history file
    :type filename_stem: str

    :returns: The chat history
    :rtype: List[ChatHistoryEntry]
    """

    with open(Paths.DATA / "chat_history" / (filename_stem + ".json"), "r") as file:
        return json.load(file)


def new_history(filename_stem: str) -> List[ChatHistoryEntry]:
    """Create a new history file

    :param filename_stem: The filename stem (without suffix) of the history file
    :type filename_stem: str
    :raises HistoryEntryAlreadyExistsError: Raised when the history entry already exists
    """
    if (Paths.DATA / "chat_history" / (filename_stem + ".json")).exists():
        raise HistoryEntryAlreadyExistsError(
            f"A history entry with the name '{filename_stem}' already exists"
        )

    with open(Paths.DATA / "chat_history" / (filename_stem + ".json"), "w") as file:
        history = [
            {"role": "system", "content": "Your name is " + CONFIG["ASSISTANT_NAME"]}
        ]
        json.dump(
            history,
            file,
            indent=4,
        )
    return history


def save_history(
    filename_stem: str, history: List[ChatHistoryEntry]
) -> List[ChatHistoryEntry]:
    """Save the chat history

    :param filename_stem: The filename stem (without suffix) of the history file
    :type filename_stem: str
    :raises HistoryEntryDoesNotExistError: Raised when the history entry does not exist
    :param history: The chat history
    :type history: List[ChatHistoryEntry]

    :returns: The chat history
    :rtype: List[ChatHistoryEntry]
    """
    if not (Paths.DATA / "chat_history" / (filename_stem + ".json")).exists():
        raise HistoryEntryDoesNotExistError(
            f"A history entry with the name '{filename_stem}' does not exist"
        )

    with open(Paths.DATA / "chat_history" / (filename_stem + ".json"), "w") as file:
        json.dump(history, file, indent=4)

    return history
