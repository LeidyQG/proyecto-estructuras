
from tkinter import Frame, Button, Label, LabelFrame, PhotoImage, Misc
from tkinter import N, NW, NE, E, W, S, X, CENTER, BOTH, NONE, LEFT, RIGHT

from .custom_widgets import WindowAppTools, create_title

class Frame_Results (WindowAppTools):
    def __init__ (self, parent: Misc, win_width: int, win_height: int):
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

        main_frame.pack(
            anchor=CENTER,
            expand=True,
            fill=BOTH
        )

    def __create_header_section (self, parent: Misc) -> None:
        header_wrapper = Frame(parent)

        title = create_title(header_wrapper, "Results")
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
