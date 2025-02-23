
import pathlib

from tkinter import Frame, Label, Button, PhotoImage, Misc
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

def create_algorithm_btn (
        parent: Misc, 
        uid:int, 
        text: str, 
        command: callable, 
        icon:str="", 
        fgcolor:str="#000011", 
        bgcolor:str="#001100"
    ) -> Button:
    btn_wrapper = Frame(parent)

    btn: Button = None
    
    if not icon:
        btn = Button(
            btn_wrapper,
            text=text,
            command=command
        )
    else:
        btn_img = PhotoImage(
            file=str(pathlib.Path().resolve()) + "/resources/icons/" + icon,
            width=16,
            height=16
        )
        btn = Button(
            btn_wrapper,
            image=help_btn_img
        )
        btn.image = btn_img
        btn.config(image=btn_img)
    
    info_btn_img = PhotoImage(
        file=str(pathlib.Path().resolve()) + "/resources/icons/help-about-mid.png",
        width=24,
        height=24
    )
    info_btn = Button(
        btn_wrapper,
        image=info_btn_img
    )
    info_btn.image = info_btn_img
    info_btn.config(image=info_btn_img)

    btn.pack(side=LEFT)
    info_btn.pack(side=LEFT)

    return btn_wrapper
