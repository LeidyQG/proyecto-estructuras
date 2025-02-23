
from tkinter import *
from tkinter import Event, Misc
from tkinter import NORMAL, DISABLED
from tkinter import ttk

from tkinterdnd2 import TkinterDnD

from .frame_load import Frame_Load
from .frame_process import Frame_Process
from .frame_results import Frame_Results

from .custom_widgets import WindowAppTools

from ..app_globals import get_file_loaded, get_file_processed, get_file_graphed

APP_NAME = "CC - Delta TSP Solver"

class GUI (WindowAppTools):
    root: Tk = None
    main_frame: ttk.Frame = None

    nbook: ttk.Notebook = None

    fload: ttk.Frame = None
    fprocess: ttk.Frame = None
    fresults: ttk.Frame = None

    def __init__ (self, *args, **kwargs):
        self.root = TkinterDnD.Tk()

        self.__set_root_style()

        self.__set_notebook(self.main_frame)

        return

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
        self.nbook = ttk.Notebook(
            parent,
            name="main-book"
        )

        self.fload = Frame_Load(self.nbook, self._win_width, self._win_height)
        self.fprocess = Frame_Process(self.nbook, self._win_width, self._win_height)
        self.fresults = Frame_Results(self.nbook, self._win_width, self._win_height)
        fothers = ttk.Frame(self.nbook)

        self.nbook.add(
            self.fload.root, 
            text="Load",
        )
        self.nbook.add(
            self.fprocess.root, 
            text="Process",
            state=DISABLED
        )
        self.nbook.add(
            self.fresults.root,
            text="Results",
            state=DISABLED
        )
        self.nbook.add(fothers, text="Info")

        self.fload.start()
        self.fprocess.start()
        self.fresults.start()
        
        self.nbook.bind("<<CheckStep>>", self.update_tabs)

        self.nbook.pack(
            anchor=CENTER,
            fill=BOTH,
            expand=True
        )
        return

    def update_tabs (self, event: Event) -> None:
        if get_file_loaded():
            self.nbook.tab(1, state=NORMAL)
            self.nbook.select(1)

            self.fload.set_input_label(loaded=True)
            return
        else:
            self.nbook.tab(1, state=DISABLED)
            return

        if get_file_loaded() and get_file_processed():
            self.nbook.tab(2, state=NORMAL)
            self.nbook.select(2)
            return
        else:
            self.nbook.tab(2, state=DISABLED)
            return

        return


    def run (self) -> None:
        self.root.mainloop()
        return
