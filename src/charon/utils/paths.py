import pathlib


class Paths:
    """A class to store the paths of the project.

    Every path is a :class:`pathlib.Path` object.
    They dynamically update themselves when the project is moved.

    Example usage:

    .. code-block:: python

        from CHARON.utils.paths import Paths

        print(Paths.ROOT)
    """

    #: The root directory of the project.
    ROOT = pathlib.Path(__file__).parent.parent.parent.parent
    #: The source directory of the project.
    #: This is where the source code of the project is stored.
    SRC = pathlib.Path(__file__).parent.parent.parent

    #: The docs directory for sphinx
    DOCS = ROOT / "docs"

    #: The data storing directory
    DATA = SRC / "charon" / "data"

    #: The CLI directory of the project. This is where the CLI scripts are stored.
    CLI = SRC / "charon" / "cli"
    #: The API directory of the project. This is where the API scripts are stored.
    API = SRC / "charon" / "api"
    #: The Streamlit app directory of the project.
    #: This is where the Streamlit app scripts are stored.
    STREAMLIT_APP = SRC / "charon" / "streamlit_app"
    #: The .env file of the project.
    ENV = ROOT / ".env"
    #: The .env file of the project, but inside the charon directory.
    ENV_INSIDE = SRC / "charon" / ".env"
