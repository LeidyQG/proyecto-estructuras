
from delta_tsp.gui import GUI

def delta_tsp() -> None:
    try:
        app_gui = GUI()
        app_gui.run()
    except KeyboardInterrupt as err:
        pass
    return
