
from tkinter import *
from tkinter import Label, PhotoImage, Event, Misc
from tkinter import TOP, LEFT, NORMAL, DISABLED
from tkinter import ttk

from PIL import Image, ImageTk

from tkinterdnd2 import TkinterDnD

from .frame_load import Frame_Load
from .frame_process import Frame_Process
from .frame_results import Frame_Results

from .custom_widgets import WindowAppTools

from ..app_globals import get_file_loaded, get_file_processing, get_file_processed, get_file_graphed

APP_NAME = "CC - Delta TSP Solver"

LOADING_WIDGET_SIZE = 128
LOADING_WIDGET_STEP_DELAY = 50

class GUI (WindowAppTools):
    root: Tk = None

    loading_frame: ttk.Frame = None
    main_frame: ttk.Frame = None
    nbook: ttk.Notebook = None
    
    loading_img_base: Image = None
    loading_img_current: Image = None
    loading_img_wrapper: Label = None
    __loading_img_running: bool = False

    fload: ttk.Frame = None
    fprocess: ttk.Frame = None
    fresults: ttk.Frame = None

    def __init__ (self, *args, **kwargs):
        self.root = TkinterDnD.Tk()

        self.__set_root_style()
        self.__set_loading_img()

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

        main_frame_wrapper = ttk.Frame(self.root)
        self.loading_frame = ttk.Frame(self.root)

        self.main_frame = ttk.Frame(
            main_frame_wrapper,
            borderwidth=3,
            relief=GROOVE
        )
        
        # self.loading_frame.place(
            # x=self._get_win_percentage(50) - (LOADING_WIDGET_SIZE // 2),
            # y=self._get_win_percentage(50, use_width=False) - (LOADING_WIDGET_SIZE // 2)
        # )
        main_frame_wrapper.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )
        self.main_frame.pack(
            anchor=CENTER,
            padx=self._get_win_percentage(8),
            pady=self._get_win_percentage(2),
            fill=BOTH,
            expand=True
        )
        return

    def __set_loading_img (self) -> None:
        self.loading_img_base = Image.open(self._get_icon_path("loading.png"))
        self.loading_img_current = self.loading_img_base.rotate(15 * 0)

        loading_img = ImageTk.PhotoImage(self.loading_img_current)
        self.loading_img_wrapper = Label(
            self.loading_frame,
            image=loading_img,
        )
        self.loading_img_wrapper["image"] = loading_img
        self.loading_img_wrapper.image = loading_img
        self.loading_img_wrapper.config(image=loading_img)
        self.loading_img_wrapper.pack()
        return

    def __set_notebook (self, parent: Misc) -> None:
        self.nbook = ttk.Notebook(
            parent,
            name="main-book"
        )
        
        self.fload = Frame_Load(self.root, self.nbook, self._win_width, self._win_height)
        self.fprocess = Frame_Process(self.root, self.nbook, self._win_width, self._win_height)
        self.fresults = Frame_Results(self.root, self.nbook, self._win_width, self._win_height)
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
        self.nbook.bind("<<CheckLoading>>", self.update_loader)

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

    def update_loader (self, event: Event) -> None:
        print(get_file_processing(), get_file_processed(), self.__loading_img_running)
        if get_file_processing() and not get_file_processed():
            self.loading_frame.place(
                x=self._get_win_percentage(50) - (LOADING_WIDGET_SIZE // 2),
                y=self._get_win_percentage(50, use_width=False) - (LOADING_WIDGET_SIZE // 2)
            )

            self.__loading_animation()
        else:
            self.__loading_img_running = False
            self.loading_frame.place_forget()
        print(get_file_processing(), get_file_processed(), self.__loading_img_running)

        return

    def __loading_animation (self, step_number:int=0) -> None:
        self.__loading_img_running = True

        self.loading_img_current = ImageTk.PhotoImage(self.loading_img_base.rotate(15 * step_number))
        self.loading_img_wrapper.image = self.loading_img_current
        self.loading_img_wrapper["image"] = self.loading_img_current
        self.loading_img_wrapper.config(image=self.loading_img_current)

        if get_file_processing():
            self.root.after(LOADING_WIDGET_STEP_DELAY, self.__loading_animation, (step_number + 1) % 24)

        return

    def run (self) -> None:
        self.root.mainloop()
        return
