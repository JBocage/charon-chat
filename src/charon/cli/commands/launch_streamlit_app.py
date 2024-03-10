import os

import click

from charon.utils.paths import Paths


@click.command("chat")
@click.pass_context
def launch_streamlit_app(ctx, *args, **kwargs):
    """
    Launches the streamlit app
    """

    os.chdir(str(Paths.ROOT))
    os.system(f"streamlit run {str(Paths.STREAMLIT_APP / 'main.py')}")
