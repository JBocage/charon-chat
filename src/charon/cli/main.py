"""This file implements a command line interface"""

import click

from charon import __VERSION__
from charon.cli.commands.setup import setup

from .commands.hello_world import hello_world
from .commands.launch_api import launch_api
from .commands.launch_streamlit_app import launch_streamlit_app
from .commands.update_sphinx_doc import doc_cli_group


class Config(object):
    """An object designed to conatin and pass the config"""

    def __init__(self) -> None:
        self.config = {}

    def set_config(self, key, value):
        """Sets a key-value pair into the config"""
        self.config[key] = value


@click.group()
@click.version_option(version=__VERSION__)
@click.pass_context
def cli(ctx, *args, **kwargs):
    """Loads all high level kwargs into the config"""
    ctx.obj = Config()
    for key, value in kwargs.items():
        ctx.obj.set_config(key, value)


cli.add_command(hello_world)
cli.add_command(launch_api)
cli.add_command(launch_streamlit_app)
cli.add_command(doc_cli_group)
cli.add_command(setup)
