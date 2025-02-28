
import pathlib
import json

from tkinter import Toplevel, Frame, Label, Button, PhotoImage, Misc
from tkinter import LEFT, W, NONE

from ..algorithms import ALGORITHMS_LIST

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

    btn = Button(
        btn_wrapper,
        text=text,
        command=lambda: command(uid)
    )

    if icon:
        btn_img = PhotoImage(
            file=str(pathlib.Path().resolve()) + "/resources/icons/" + icon,
            width=16,
            height=16
        )
        btn.image = btn_img
        btn.config(image=btn_img, compound=LEFT)
    
    info_btn_img = PhotoImage(
        file=str(pathlib.Path().resolve()) + "/resources/icons/help-about-mid.png",
        width=24,
        height=24
    )
    info_btn = Button(
        btn_wrapper,
        image=info_btn_img,
        command=lambda: open_algorithm_info(uid)
    )
    info_btn.image = info_btn_img
    info_btn.config(image=info_btn_img)

    btn.pack(side=LEFT)
    info_btn.pack(side=LEFT)

    return btn_wrapper

def open_algorithm_info (uid: int) -> None:
    info_window = Toplevel()
    win_width = (info_window.winfo_screenwidth()) // 2
    win_height = (info_window.winfo_screenheight()) // 2

    info_window.config(padx=win_width // 25, pady=win_height // 25)

    info_window.geometry(
        f"{win_width}x{win_height}" + \
        f"+{(info_window.winfo_screenwidth() - win_width) // 2}" + \
        f"+{(info_window.winfo_screenheight() - win_height) // 2}"
    )

    algorithm_data = ALGORITHMS_LIST[uid]

    info_window.title("Algoritmo - " + algorithm_data["name"])
    
    with open(str(pathlib.Path().resolve()) + "/resources/info/" + algorithm_data["info_file"], "r") as json_file:
        algorithm_info = json.load(json_file)
        
        Label(
            info_window, 
            text=algorithm_info["title"],
            wraplength=(win_width * 0.9),
            justify=LEFT,
            font=("", 20, "bold")
        ).pack()
        Label(
            info_window, 
            text=algorithm_info["info"],
            wraplength=(win_width * 0.75),
            justify=LEFT,
            font=("", 12, "normal")
        ).pack(pady=12)

        complexity_wrapper = Frame(info_window)
        Label(
            complexity_wrapper,
            text="Complejidad:",
            justify=LEFT,
            font=("", 20, "bold")
        ).pack(anchor=W, padx=12, expand=False, fill=NONE)
        Label(
            complexity_wrapper,
            justify=LEFT,
            text=algorithm_info["complexity"],
            font=("", 14, "normal")
        ).pack(anchor=W, padx=(win_width // 10), expand=False, fill=NONE)
        complexity_wrapper.pack(anchor=W)

        memory_wrapper = Frame(info_window)
        Label(
            memory_wrapper,
            text="Uso de Memoria:",
            justify=LEFT,
            font=("", 20, "bold")
        ).pack(anchor=W, padx=12, expand=False, fill=NONE)
        Label(
            memory_wrapper,
            justify=LEFT,
            text=algorithm_info["memory"],
            font=("", 14, "normal")
        ).pack(anchor=W, padx=(win_width // 10), expand=False, fill=NONE)
        memory_wrapper.pack(anchor=W)

        quality_wrapper = Frame(info_window)
        Label(
            quality_wrapper,
            text="Calidad de la Solución:",
            justify=LEFT,
            font=("", 20, "bold")
        ).pack(anchor=W, padx=12, expand=False, fill=NONE)
        Label(
            quality_wrapper,
            justify=LEFT,
            text=algorithm_info["quality"],
            font=("", 14, "normal")
        ).pack(anchor=W, padx=(win_width // 10), expand=False, fill=NONE)
        quality_wrapper.pack(anchor=W)
    return 
