
from tkinter import Frame, LabelFrame, Button, Text, Event, Misc
from tkinter import N, NW, NE, E, W, S, X, Y, CENTER, BOTH, NONE, TOP, LEFT, RIGHT, END, NORMAL, DISABLED

from .custom_widgets import WindowAppTools, create_title, create_algorithm_btn

from ..app_globals import get_file_loaded, get_file_previewed, get_file_path, set_file_previewed
from ..file_utils import load_file_contents_buffer

MAX_ALGORITHMS_BTNS_PER_ROW = 5
ALGORITHMS_LIST: list[dict[str, any]] = [
    {
        "uid": 0,
        "name": "Algorithm 1",
        "command": lambda: print("algorithm_1"),
        "icon": "",
        "fg": "",
        "bg": ""
    },
    {
        "uid": 0,
        "name": "Algorithm 1",
        "command": lambda: print("algorithm_1"),
        "icon": "",
        "fg": "",
        "bg": ""
    },
    {
        "uid": 0,
        "name": "Algorithm 1",
        "command": lambda: print("algorithm_1"),
        "icon": "",
        "fg": "",
        "bg": ""
    },
    {
        "uid": 0,
        "name": "Algorithm 1",
        "command": lambda: print("algorithm_1"),
        "icon": "",
        "fg": "",
        "bg": ""
    },
    {
        "uid": 0,
        "name": "Algorithm 1",
        "command": lambda: print("algorithm_1"),
        "icon": "",
        "fg": "",
        "bg": ""
    },
    {
        "uid": 1,
        "name": "Algorithm 2",
        "command": lambda: print("algorithm_2"),
        "icon": "",
        "fg": "",
        "bg": ""
    },
    {
        "uid": 1,
        "name": "Algorithm 2",
        "command": lambda: print("algorithm_2"),
        "icon": "",
        "fg": "",
        "bg": ""
    },
    {
        "uid": 1,
        "name": "Algorithm 2",
        "command": lambda: print("algorithm_2"),
        "icon": "",
        "fg": "",
        "bg": ""
    },
    {
        "uid": 2,
        "name": "Algorithm 3",
        "command": lambda: print("algorithm_3"),
        "icon": "",
        "fg": "",
        "bg": ""
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
            height=self._get_win_percentage(40, use_width=False) // 16,
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
            expand=False,
            fill=BOTH
        )

        return

    def __create_footer_section (self, parent: Misc) -> None:
        footer_wrapper = Frame(parent)
        btn_row = Frame(footer_wrapper)
        
        for i, algorithm in enumerate(ALGORITHMS_LIST):
            if i % MAX_ALGORITHMS_BTNS_PER_ROW == 0 and i != 0:
                btn_row.pack(side=TOP, pady=self._get_win_percentage(1, use_width=False))
                btn_row = Frame(footer_wrapper)

            algorithm_btn = create_algorithm_btn(
                btn_row,
                algorithm["uid"],
                algorithm["name"],
                algorithm["command"],
                # icon=algorithm["icon"],
                # fgcolor=algorithm["fg"],
                # bgcolor=algorithm["bg"],

            )
            algorithm_btn.pack(
                side=LEFT,
                padx=self._get_win_percentage(1)
            )

        btn_row.pack(side=TOP)
        footer_wrapper.pack(
            anchor=S,
            expand=True,
            fill=Y
        )
        return

    def __load_file (self, event: Event) -> None:
        if get_file_previewed() or \
           not get_file_loaded() or\
           get_file_path() == None:
            return

        current_file_content = load_file_contents_buffer(get_file_path())
        self.preview_text.config(state=NORMAL)
        self.preview_text.insert(END, current_file_content)
        self.preview_text.config(state=DISABLED)
        set_file_previewed(True)
        return

