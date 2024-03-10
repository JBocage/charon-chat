import os

import click


@click.command("launch-api")
@click.pass_context
def launch_api(ctx, *args, **kwargs):
    """
    Launch api for charon
    """

    from charon.utils.paths import Paths

    os.chdir(str(Paths.ROOT))
    os.system("uvicorn src.charon.api.main:app --reload")
