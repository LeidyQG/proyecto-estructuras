
import pathlib

from tkinter import Frame, Button, Label, LabelFrame, PhotoImage, StringVar, Tk, Misc
from tkinter import N, NW, NE, E, W, S, X, CENTER, BOTH, NONE, LEFT, RIGHT
from tkinter.filedialog import askopenfilename

from tkinterdnd2 import DND_FILES, TkinterDnD

from .custom_widgets import WindowAppTools, create_title

from ..app_globals import get_file_loaded, get_file_path, set_file_path, TSP_FILE_TYPE
from ..file_utils import handle_file_drop

class Frame_Load (WindowAppTools):
    __app_root: Tk = None
    parent: Misc = None
    root: Frame = None

    __input_labels: list[StringVar] = []

    def __init__ (self, app_root: Tk, parent: Misc, win_width: int, win_height: int):
        self.__app_root = app_root
        self.parent = parent
        self.root = Frame(self.parent)

        self._win_width = win_width
        self._win_height = win_height

        return

    def start (self) -> None:
        main_frame = Frame(
            self.root,
            padx=self._get_win_percentage(2),
            pady=self._get_win_percentage(2),
        )

        self.__create_header_section(main_frame)
        self.__create_file_section(main_frame)
        self.__create_footer_section(main_frame)
        
        main_frame.pack(
            anchor=CENTER,
            expand=True,
            fill=BOTH
        )
        return

    def __create_header_section (self, parent: Misc) -> None:
        header_wrapper = Frame(parent)

        title = create_title(header_wrapper, "Load TSP File")
        title.pack(
            side=LEFT,
            anchor=W
        )

        help_btn_img = self._get_icon("help-about.png", big=True)
        help_btn = Button(
            header_wrapper,
            image=help_btn_img
        )
        help_btn.image = help_btn_img
        help_btn.config(image=help_btn_img)
        help_btn.pack(
            side=RIGHT,
            anchor=W
        )
        
        header_wrapper.pack(anchor=N,expand=False,fill=X)
        return

    def __create_file_section (self, parent: Misc) -> None:
        file_wrapper = LabelFrame(
            parent, 
            text="Enter your TSP instance file",
            padx=self._get_win_percentage(5),
            pady=self._get_win_percentage(1, use_width=False),
        )

        file_label_wrapper = Frame(file_wrapper)
        
        file_input_btn_img = self._get_icon("find.png")
        self.set_input_label()
        file_input_label_1 = Label(
            file_label_wrapper,
            textvariable=self.__input_labels[0]
        )
        file_input_label_2 = Label(
            file_label_wrapper,
            textvariable=self.__input_labels[1]
        )
        file_input_btn = Button(
            file_label_wrapper,
            text="Find File",
            compound=LEFT,
            command=self.__open_file_dialog
        )
        file_input_btn.image = file_input_btn_img
        file_input_btn.config(image=file_input_btn_img)

        file_input_label_1.pack()
        file_input_label_2.pack()
        file_input_btn.pack()

        file_label_wrapper.pack(anchor=CENTER, expand=True)

        file_wrapper.drop_target_register(DND_FILES)
        file_wrapper.dnd_bind("<<Drop>>", lambda e: handle_file_drop(e, self.parent))
        
        file_wrapper.pack(
            padx=self._get_win_percentage(12),
            pady=self._get_win_percentage(1),
            anchor=CENTER,
            expand=True,
            fill=BOTH
        )
        return

    def __create_footer_section (self, parent: Misc) -> None:
        footer_wrapper = Frame(parent)
        
        download_files_btn_img = self._get_icon("download.png")
        download_files_btn = Button(
            footer_wrapper,
            text="Download TSP Files",
            image=download_files_btn_img,
            compound=LEFT,
            command=lambda: print(get_file_loaded())
        )
        # God I hate Tk
        download_files_btn.image = download_files_btn_img
        download_files_btn.configure(image=download_files_btn_img)
        download_files_btn.pack(
            side=LEFT,
            anchor=W
        )

        footer_wrapper.pack(
            anchor=S,
            expand=False,
            fill=X
        )
        return

    def __open_file_dialog (self) -> None:
        file_name = askopenfilename(
            title="Select a TSP Instance File",
            # initialdir=
            filetypes=(("TST Instance file", TSP_FILE_TYPE),)
        )

        if file_name == "":
            return

        file_path = pathlib.Path(file_name)
        
        error = set_file_path(file_path, self.parent)
        if error:
            # TODO: notify or smth
            pass

        return

    def set_input_label (self, loaded:bool=False) -> None:
        if len(self.__input_labels) == 0:
            self.__input_labels.append(StringVar(self.root, "Drag and Drop Your TSP instance File Here \nor"))
            self.__input_labels.append(StringVar(self.root, ""))

        if loaded:
            file_loaded_name = get_file_path().stem + get_file_path().suffix
            self.__input_labels[0].set(f"Loaded '{file_loaded_name}'")
            self.__input_labels[1].set("need to use other file? Drag and Drop the file or")
        else:
            self.__input_labels[0].set("Drag and Drop Your TSP instance File Here \nor")
            self.__input_labels[1].set("")

        return
