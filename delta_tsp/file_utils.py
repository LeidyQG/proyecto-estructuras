
import pathlib

from tkinterdnd2.TkinterDnD import DnDEvent

from delta_tsp.app_globals import set_file_path

def handle_file_drop (file_drop_event: DnDEvent) -> None:
    file_path = pathlib.Path(file_drop_event.data)

    error = set_file_path(file_path)
    if not error:
        # TODO: Notify or smth
        pass

    return
