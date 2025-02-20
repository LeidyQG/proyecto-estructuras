
from tkinter import Frame, Button, Label, LabelFrame, PhotoImage, Misc
from tkinter import N, NW, NE, E, W, S, X, CENTER, BOTH, NONE, LEFT, RIGHT

from tkinterdnd2 import DND_FILES, TkinterDnD

from .custom_widgets import WindowAppTools, create_title

class Frame_Load (WindowAppTools):
    root: Frame = None
    main_frame: Frame = None

    def __init__ (self, parent: Misc, win_width: int, win_height: int) -> Frame:
        self.root = Frame(parent)

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
        file_input_label = Label(
            file_label_wrapper,
            text="Drag and Drop Your TSP instance File Here \nor",
        )
        file_input_btn = Button(
            file_label_wrapper,
            text="Find File",
            compound=LEFT
        )
        file_input_btn.image = file_input_btn_img
        file_input_btn.config(image=file_input_btn_img)

        file_input_label.pack()
        file_input_btn.pack()

        file_label_wrapper.pack(anchor=CENTER, expand=True)

        file_wrapper.drop_target_register(DND_FILES)
        file_wrapper.dnd_bind("<<Drop>>", lambda e: print(e))
        
        file_wrapper.pack(
            padx=self._get_win_percentage(12),
            pady=self._get_win_percentage(1),
            anchor=CENTER,
            expand=True,
            fill=BOTH
        )
        return

    def __create_footer_section (self, parent: Misc):
        footer_wrapper = Frame(parent)
        
        download_files_btn_img = self._get_icon("download.png")
        download_files_btn = Button(
            footer_wrapper,
            text="Download TSP Files",
            image=download_files_btn_img,
            compound=LEFT
        ) # God I hate Tk
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
