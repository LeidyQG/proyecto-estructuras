
from tkinter import Frame, LabelFrame, Button, Text, Event, Misc
from tkinter import N, NW, NE, E, W, S, X, CENTER, BOTH, NONE, TOP, LEFT, RIGHT, END, NORMAL, DISABLED

from .custom_widgets import WindowAppTools, create_title

from ..app_globals import get_file_loaded, get_file_previewed, get_file_path, set_file_previewed
from ..file_utils import load_file_contents_buffer

ALGORITHMS_LIST: list[dict[str, any]] = [
    {
        "name": "Algorithm 1",
        "execution": lambda: print("algorithm_1"),
        "icon": ""
    },
    {
        "name": "Algorithm 2",
        "execution": lambda: print("algorithm_2"),
        "icon": ""
    },
    {
        "name": "Algorithm 3",
        "execution": lambda: print("algorithm_3"),
        "icon": ""
    },
]

class Frame_Process (WindowAppTools):
    root: Frame = None
    parent: Misc = None

    preview_text: Text = None

    def __init__ (self, parent: Misc, win_width: int, win_height: int):
        self.parent = parent
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
        self.__create_preview_section(main_frame)
        self.__create_footer_section(main_frame)

        main_frame.pack(
            anchor=CENTER,
            expand=True,
            fill=BOTH
        )

    def __create_header_section (self, parent: Misc) -> None:
        header_wrapper = Frame(parent)

        title = create_title(header_wrapper, "Process TSP File")
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

    def __create_preview_section (self, parent: Misc) -> None:
        preview_wrapper = LabelFrame(
            parent, 
            text="Preview the TSP instance File and Choose a Processing Algorithm"
        )
        
        self.root.bind("<Visibility>", self.__load_file)
        self.preview_text = Text(
            preview_wrapper,
            height=self._get_win_percentage(48, use_width=False) // 16,
            state=DISABLED
        )

        self.preview_text.pack(
            anchor=CENTER,
            fill=BOTH
        )

        preview_wrapper.pack(
            padx=self._get_win_percentage(12),
            pady=self._get_win_percentage(1),
            anchor=CENTER,
            expand=True,
            fill=BOTH
        )

        return

    def __create_footer_section (self, parent: Misc) -> None:
        footer_wrapper = Frame(parent)
        
        for algorithm in ALGORITHMS_LIST:
            algorithm_btn = Button(
                footer_wrapper,
                text=algorithm["name"],
                command=algorithm["execution"]
            )
            algorithm_btn.pack(
                side=LEFT,
                padx=self._get_win_percentage(1)
            )

        footer_wrapper.pack(
            anchor=S,
            expand=False,
        )
        return

    def __load_file (self, event: Event) -> None:
        print("try")
        if get_file_previewed() or \
           not get_file_loaded() or\
           get_file_path() == None:
            return
        print("done")

        current_file_content = load_file_contents_buffer(get_file_path())
        self.preview_text.config(state=NORMAL)
        self.preview_text.insert(END, current_file_content)
        self.preview_text.config(state=DISABLED)
        set_file_previewed(True)
        return

