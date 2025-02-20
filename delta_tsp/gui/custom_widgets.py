
import pathlib

from tkinter import Label, PhotoImage, font, Misc
from tkinter import LEFT

class WindowAppTools ():
    _screen_width: int = 0
    _screen_height: int = 0

    _win_width: int = 0
    _win_height: int = 0

    _cur_path: str = str(pathlib.Path().resolve())

    def _get_win_percentage (self, percentage:int=100, use_width:bool=True) -> int:
        if use_width:
            return int(self._win_width * (percentage / 100))
        else:
            return int(self._win_height * (percentage / 100))

    def _get_icon_path (self, icon_name:str="") -> str:
        return self._cur_path + "/resources/icons/" + icon_name

    def _get_icon (self, icon_name:str="", sm:bool=False, big:bool=False) -> PhotoImage:
        icon_width = 24
        icon_height = 24

        if sm:
            icon_width = 16
            icon_height = 16
        elif big:
            icon_width = 32
            icon_height = 32

        return PhotoImage(
            file=self._get_icon_path(icon_name),
            width=icon_width,
            height=icon_height
        )

def create_title (parent: Misc, text: str) -> Label:
    title_label = Label(
        parent,
        text=text,
        justify=LEFT,
        font=("", 26, "bold")
    )

    return title_label
