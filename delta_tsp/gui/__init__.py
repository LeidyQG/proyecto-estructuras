
from tkinter import *
from tkinter import Misc
from tkinter import ttk

from tkinterdnd2 import TkinterDnD

from .frame_load import Frame_Load

from .custom_widgets import WindowAppTools

APP_NAME = "CC - Delta TSP Solver"

class GUI (WindowAppTools):
    root: Tk = None
    main_frame: ttk.Frame = None

    def __init__ (self, *args, **kwargs):
        self.root = TkinterDnD.Tk()

        self.__set_root_style()

        self.__set_notebook(self.main_frame)

        return

    def _get_win_percentage (self, percentage:int=100, use_width:bool=True) -> int:
        if use_width:
            return int(self._win_width * (percentage / 100))
        else:
            return int(self._win_height * (percentage / 100))
    
    def __set_root_style (self) -> None:
        self._screen_width = self.root.winfo_screenwidth()
        self._screen_height = self.root.winfo_screenheight()
        self._win_width = (3 * self._screen_width) // 4
        self._win_height = (5 * self._screen_height) // 8

        self.root.geometry(
            f"{self._win_width}x{self._win_height}" + \
            f"+{(self._screen_width - self._win_width) // 2}" + \
            f"+{(self._screen_height - self._win_height) // 2}"
        )

        self.root.title(APP_NAME)

        self.main_frame = ttk.Frame(
            self.root,
            # padding=self._get_win_percentage(2),
            borderwidth=3,
            relief=GROOVE
        )

        self.main_frame.pack(
            anchor=CENTER,
            padx=self._get_win_percentage(8),
            pady=self._get_win_percentage(2),
            fill=BOTH,
            expand=True
        )
        return

    def __set_notebook (self, parent: Misc) -> None:
        nbook = ttk.Notebook(
            parent,
            name="main-book"
        )

        fload = Frame_Load(nbook, self._win_width, self._win_height)
        fprocess = ttk.Frame(nbook)
        fresults = ttk.Frame(nbook)
        fothers = ttk.Frame(nbook)

        nbook.add(
            fload.root, 
            text="Load",
        )
        nbook.add(fprocess, text="Process")
        nbook.add(fresults, text="Results")
        nbook.add(fothers, text="Info")

        fload.start()

        nbook.pack(
            anchor=CENTER,
            fill=BOTH,
            expand=True
        )
        return

    def run (self) -> None:
        self.root.mainloop()
        return
