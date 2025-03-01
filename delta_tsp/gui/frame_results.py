
from tkinter import Frame, Button, Label, LabelFrame, PhotoImage, Canvas, StringVar, Tk, Misc
from tkinter import N, NW, NE, E, W, S, X, Y, CENTER, BOTH, NONE, LEFT, RIGHT, LAST

from ..app_globals import get_file_results, get_file_path

from .custom_widgets import WindowAppTools, create_title

class Frame_Results (WindowAppTools):
    __app_root: Tk = None
    parent: Misc = None
    root: Frame = None

    canvas: Canvas = None
    rel_x: float = 0.00
    rel_y: float = 0.00
    node_radius: float = 2.00
    nodes: list[tuple[float, float]] = []

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
        self.__create_graph_canvas(main_frame)
        self.__create_footer_section(main_frame)

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

        # help_btn_img = self._get_icon("help-about.png", big=True)
        # help_btn = Button(
            # header_wrapper,
            # image=help_btn_img
        # )
        # help_btn.image = help_btn_img
        # help_btn.config(image=help_btn_img)
        # help_btn.pack(
            # side=RIGHT,
            # anchor=W
        # )
        
        header_wrapper.pack(anchor=N,expand=False,fill=X)
        return

    def __create_graph_canvas (self, parent: Misc) -> None:
        canvas_wrapper = LabelFrame(
            parent,
            text="See the Results"
        )

        self.canvas = Canvas(
            canvas_wrapper,
            background="white",
            width=self._get_win_percentage(80),
            height=self._get_win_percentage(60, use_width=False)
        )

        self.canvas_width = self._get_win_percentage(80)
        self.canvas_height = self._get_win_percentage(60, use_width=False)

        self.canvas.pack(
            anchor=CENTER,
            expand=True,
            fill=BOTH
        )

        canvas_wrapper.pack(
            anchor=CENTER,
            expand=True,
            fill=BOTH
        )
        return

    def __create_footer_section (self, parent: Misc) -> None:
        footer_wrapper = LabelFrame(parent, text="Results Information")

        self.__input_labels.append(StringVar(self.root, ""))
        self.__input_labels.append(StringVar(self.root, ""))
        self.__input_labels.append(StringVar(self.root, ""))
        
        distance_label = Label(
            parent,
            text="Distancia:",
            font=("", 14, "bold")
        )
        distance_info = Label(
            parent,
            textvariable=self.__input_labels[0],
            font=("", 14, "normal")
        )
        
        distance_label.pack(anchor=W, side=LEFT)
        distance_info.pack(anchor=W, side=LEFT, padx=12)

        nodes_label = Label(
            parent,
            text="Número Nodos:",
            font=("", 14, "bold")
        )
        nodes_info = Label(
            parent,
            textvariable=self.__input_labels[1],
            font=("", 14, "normal")
        )
        
        nodes_label.pack(anchor=W, side=LEFT)
        nodes_info.pack(anchor=W, side=LEFT, padx=12)

        time_label = Label(
            parent,
            text="Tiempo:",
            font=("", 14, "bold")
        )
        time_info = Label(
            parent,
            textvariable=self.__input_labels[2],
            font=("", 14, "normal")
        )
        
        time_label.pack(anchor=W, side=LEFT)
        time_info.pack(anchor=W, side=LEFT, padx=12)

        footer_wrapper.pack(
            anchor=S,
            expand=False,
            fill=X
        )
        return

    def make_graph (self):
        file_results = get_file_results()

        if file_results == None:
            return

        self.__input_labels[0].set("%.3lf" % file_results["distance"])
        self.__input_labels[1].set(file_results["nodes"])
        self.__input_labels[2].set("%.3lf" % file_results["time"])

        self.__graph_all_nodes()
        
    def __graph_all_nodes (self) -> None:
        self.nodes = []
        min_x = 0.0
        min_y = 0.0
        max_x = 0.0
        max_y = 0.0

        with open(str(get_file_path()), 'r') as f:
            file_content = f.readlines()
        
        header_done = False
        for line in file_content:
            if line.startswith("NODE_COORD_SECTION"):
                header_done = True
                continue
            elif line.startswith("EOF"):
                break

            if header_done:
                index, x, y = line.strip().split()
                
                if float(x) < min_x:
                    min_x = float(x)
                elif float(x) > max_x:
                    max_x = float(x)

                if float(y) < min_y:
                    min_y = float(y)
                elif float(y) > max_y:
                    max_y = float(y)

                self.nodes.append((float(x), float(y)))

        self.scale_x = (self.canvas_width / (abs(min_x) + abs(max_x))) / 2
        self.scale_y = (self.canvas_height / (abs(min_y) + abs(max_y))) / 2

        self.rel_x = self.canvas_width // 4
        self.rel_y = self.canvas_height // 2

        self.canvas.create_line(self.rel_x, 0, self.rel_x, self.canvas_height, arrow=BOTH)
        self.canvas.create_line(0, self.rel_y, self.canvas_width, self.rel_y, arrow=BOTH)

        prev_node: tuple(float, float) = self.nodes[0]
        for i, node in enumerate(self.nodes):
            if i != 0:
                self.canvas.create_line(
                    self.rel_x + (prev_node[0] * self.scale_x),
                    self.rel_y - (prev_node[1] * self.scale_y),
                    self.rel_x + (node[0] * self.scale_x),
                    self.rel_y - (node[1] * self.scale_y),
                    arrow=BOTH
                )

            self._create_circle(self.rel_x + (node[0] * self.scale_x), self.rel_y - (node[1] * self.scale_y))
            prev_node = node

        return
        

    def _create_circle (self, x, y) -> None:
       return self.canvas.create_oval(x - self.node_radius, y - self.node_radius, x + self.node_radius, y + self.node_radius, fill="black") 
