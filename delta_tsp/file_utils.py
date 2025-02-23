
import pathlib

from tkinter import Misc

from tkinterdnd2.TkinterDnD import DnDEvent

from delta_tsp.app_globals import set_file_path

def handle_file_drop (file_drop_event: DnDEvent, parent:Misc=None) -> None:
    file_path = pathlib.Path(file_drop_event.data)

    error = set_file_path(file_path, parent=parent)
    if not error:
        # TODO: Notify or smth
        pass

    return

def load_file_contents_buffer (file_path: pathlib.Path) -> str:
    file_buffer = ""

    with open(file_path, "r") as f:
        file_buffer = f.read()

    return file_buffer
