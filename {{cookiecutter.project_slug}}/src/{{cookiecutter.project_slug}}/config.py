"""This module contains the general configuration of the project."""
from pathlib import Path


try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"


SRC = Path(__file__).parent.resolve()
BLD = SRC.joinpath("..", "..", "bld")


__all__ = ["__version__", "BLD", "SRC"]
