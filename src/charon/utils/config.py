"""
Exports the CONFIG object that is used for loading the project's config

.. code-block :: python

    from charon.utils.config import CONFIG

    print(CONFIG)
"""

from functools import lru_cache
from typing import TypedDict

import dotenv

from charon.utils.paths import Paths


class Config(TypedDict):
    """A dictionary that holds the configuration values."""

    #: The name of the assistant
    ASSISTANT_NAME: str

    #: An example configuration value.
    OPENAI_API_KEY: str


class EnvFileNotFoundError(Exception):
    """Raised when the .env file is not found."""


@lru_cache
def load_config() -> Config:
    """Loads the configuration from the .env file.

    :raises EnvFileNotFoundError: If the .env file is not found.

    :return: The configuration values.
    :rtype: Config
    """
    if Paths.ENV.exists():
        return dotenv.dotenv_values(Paths.ENV)
    elif Paths.ENV_INSIDE.exists():
        return dotenv.dotenv_values(Paths.ENV_INSIDE)
    else:
        raise EnvFileNotFoundError("The .env file was not found.")


CONFIG = load_config()
