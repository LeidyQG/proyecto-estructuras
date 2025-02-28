
import time

from tkinter import Misc

from ..app_globals import set_file_processed

def test_time (parent: Misc) -> None:
    print("TEST Thread function")
    
    for i in range(3):
        print(i)
        time.sleep(1)

    set_file_processed(True, parent=parent)
    print("TEST DONE")
