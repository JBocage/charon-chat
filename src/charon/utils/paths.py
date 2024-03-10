import pathlib


class Paths:
    """A class to store the paths of the project.

    Every path is a :class:`pathlib.Path` object.
    They dynamically update themselves when the project is moved.

    Example usage:

    .. code-block:: python

        from src.tmp.utils.paths import Paths

        print(Paths.ROOT)
    """

    #: The root directory of the project.
    ROOT = pathlib.Path(__file__).parent.parent.parent.parent
    #: The source directory of the project.
    #: This is where the source code of the project is stored.
    SRC = ROOT / "src"

    #: The docs directory for sphinx
    DOCS = ROOT / "docs"

    #: The CLI directory of the project. This is where the CLI scripts are stored.
    CLI = SRC / "charon" / "cli"
    #: The API directory of the project. This is where the API scripts are stored.
    API = SRC / "charon" / "api"
    #: The Streamlit app directory of the project.
    #: This is where the Streamlit app scripts are stored.
    STREAMLIT_APP = SRC / "charon" / "streamlit_app"
    #: The .env file of the project.
    ENV = ROOT / ".env"
