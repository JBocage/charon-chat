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

    #: An example configuration value.
    OPENAI_API_KEY: str


@lru_cache
def load_config() -> Config:
    """Loads the configuration from the .env file."""
    return dotenv.dotenv_values(Paths.ROOT / ".env")


CONFIG = load_config()
