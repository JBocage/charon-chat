import click

from charon.utils.paths import Paths


@click.command("setup")
@click.pass_context
def setup(ctx, *args, **kwargs):
    """
    Launches the streamlit app
    """

    if not Paths.ENV_INSIDE.exists():
        Paths.ENV_INSIDE.touch()

        with open(Paths.ENV_INSIDE, "w") as f:
            assistant_name = input("Enter the name of your assistant: ")
            f.write(f"ASSISTANT_NAME={assistant_name}\n")

            openai_key = input("Enter your OpenAI API key: ")
            f.write(f"OPENAI_API_KEY={openai_key}\n")

        print(
            "The .env file has been created.\n"
            "You can now run the `charon chat` command to launch the app."
        )
