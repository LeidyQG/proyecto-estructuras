
import pathlib

""" File Constants """

TSP_FILE_TYPE = ".tsp"

""" General States of the program """
global file_loaded # File has been loaded, ready to process it
global file_processed # File has been processed, ready to graph it
global file_graphed # File has been graphed. 
file_loaded: bool = False
file_processed: bool = False
file_graphed: bool = False

global file_path # File Path
file_path: pathlib.Path = None

def get_file_loaded () -> bool: return file_loaded
def set_file_loaded (status:bool=True) -> None:
    global file_loaded
    file_loaded = status

    if file_loaded:
        set_file_processed(False)
        set_file_graphed(False)

    return True

def get_file_graphed () -> bool: return file_graphed
def set_file_processed (val:bool=True) -> None:
    global file_processed

    if not get_file_loaded():
        file_processed = False
        return False

    file_processed = val

    if file_processed:
        set_file_graphed(False)

    return True

def get_file_processed () -> bool: return file_processed
def set_file_graphed (val:bool=True) -> bool:
    global file_graphed

    if not get_file_loaded() or not get_file_processed():
        file_graphed = False
        return False

    file_graphed = val
    return True

def get_file_path () -> pathlib.Path: return file_path
def set_file_path (new_file_path: pathlib.Path) -> bool:
    if not new_file_path.exists() or \
        new_file_path.is_dir() or \
        new_file_path.suffix != TSP_FILE_TYPE:
        return False

    global file_path
    file_path = new_file_path
    
    if not get_file_loaded():
        set_file_loaded(True)

    return True
