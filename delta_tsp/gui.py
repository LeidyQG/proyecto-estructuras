
from tkinter import *
from tkinter import Misc
from tkinter import ttk

APP_NAME = "CC - Delta TSP Solver"

class GUI ():
    root: Tk = None
    main_frame: ttk.Frame = None

    _screen_width: int = 0
    _screen_height: int = 0
    _win_width: int = 0
    _win_height: int = 0

    def __init__ (self, *args, **kwargs):
        self.root = Tk()

        self.__set_root_style()

        self.__set_notebook(self.main_frame)

        self.root.mainloop()
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
            padding=self._get_win_percentage(2),
            borderwidth=3,
            relief=GROOVE
        )

        self.main_frame.pack(
            anchor=CENTER,
            padx=self._get_win_percentage(2),
            pady=self._get_win_percentage(2),
            fill=BOTH,
            expand=True
        )
        return

    def __set_notebook (self, parent: Misc) -> None:
        nbook = ttk.Notebook(parent)

        f1 = ttk.Frame(nbook)
        f2 = ttk.Frame(nbook)
        f3 = ttk.Frame(nbook)

        nbook.add(f1, text="Load")
        nbook.add(f2, text="Process")
        nbook.add(f3, text="Results")

        ttk.Label(f1, text="Hello World!").pack()
        ttk.Button(f1, text="Quit", command=self.root.destroy).pack()

        nbook.pack()
        return
