"""This module contains the general configuration of the project."""
from __future__ import annotations

from pathlib import Path


try:
    from ._version import version as __version__
except ImportError:
    # broken installation, we don't even try unknown only works because we do poor mans
    # version compare
    __version__ = "unknown"


SRC = Path(__file__).parent.resolve()
BLD = SRC.joinpath("..", "..", "bld")


__all__ = ["__version__", "BLD", "SRC"]
