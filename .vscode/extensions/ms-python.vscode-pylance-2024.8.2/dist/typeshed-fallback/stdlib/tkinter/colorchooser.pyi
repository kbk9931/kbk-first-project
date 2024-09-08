import sys
from tkinter import Misc
from tkinter.commondialog import Dialog
from typing import ClassVar

if sys.version_info >= (3, 9):
    __all__ = ["Chooser", "askcolor"]

class Chooser(Dialog):
    command: ClassVar[str]

if sys.version_info >= (3, 9):
    def askcolor(
        color: str | bytes | None = None, *, initialcolor: str = ..., parent: Misc = ..., title: str = ...
    ) -> tuple[None, None] | tuple[tuple[int, int, int], str]: ...

else:
    def askcolor(
        color: str | bytes | None = None, *, initialcolor: str = ..., parent: Misc = ..., title: str = ...
    ) -> tuple[None, None] | tuple[tuple[float, float, float], str]: ...
