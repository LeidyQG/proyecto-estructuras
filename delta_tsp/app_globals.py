
import pathlib

from tkinter import Misc

""" File Constants """

TSP_FILE_TYPE = ".tsp"
TSP_FIlE_HEADER_END = "NODE_COORD_SECTION\n"

""" General States of the program """
global file_loaded # File has been loaded, ready to process it
global file_previewed # File has been loaded, not yet processed but preview available
global file_processing # File is beeing processed
global file_processed # File has been processed, ready to graph it
global file_results # File has been processed 
global file_graphed # File has been graphed. 
file_loaded: bool = False
file_previewed: bool = False
file_processing: bool = False
file_processed: bool = False
file_results: dict[str, any] = None
file_graphed: bool = False

global file_path # File Path
file_path: pathlib.Path = None

def get_file_loaded () -> bool: return file_loaded
def set_file_loaded (status:bool=True, parent:Misc=None) -> bool:
    global file_loaded
    file_loaded = status

    if file_loaded:
        set_file_previewed(False)
        set_file_processing(False)
        set_file_processed(False)
        set_file_graphed(False)

    if parent != None:
        parent.event_generate("<<CheckStep>>")

    return True

def get_file_previewed () -> bool: return file_previewed
def set_file_previewed (status:bool=True, parent:Misc=None) -> bool:
    global file_previewed
    file_previewed = status

    return True

def get_file_processing () -> bool: return file_processing
def set_file_processing (val:bool=True, parent:Misc=None) -> bool:
    global file_processing

    if not get_file_loaded() or not get_file_previewed():
        file_graphed = False
        return False

    file_processing = val

    if file_processing:
        set_file_processed(False)

    if parent != None:
        parent.event_generate("<<CheckLoading>>")

    return True

def get_file_processed () -> bool: return file_processed
def set_file_processed (val:bool=True, parent:Misc=None) -> bool:
    global file_processed

    if not get_file_loaded():
        file_processed = False
        return False

    file_processed = val

    if file_processed:
        set_file_processing(False, parent=parent)

    set_file_graphed(False)

    if parent != None:
        parent.event_generate("<<CheckStep>>")

    return True

def get_file_results () -> dict[str, any]: return file_results
def set_file_results (val:dict[str, any], parent:Misc=None) -> bool:
    global file_results

    if not get_file_processed():
        return False

    file_results = val

    if (parent != None):
        parent.event_generate("<<CheckStep>>")

    return True

def get_file_graphed () -> bool: return file_graphed
def set_file_graphed (val:bool=True, parent:Misc=None) -> bool:
    global file_graphed

    if not get_file_loaded() or not get_file_processed():
        file_graphed = False
        return False

    file_graphed = val
    return True

def get_file_path () -> pathlib.Path: return file_path
def set_file_path (new_file_path: pathlib.Path, parent:Misc=None) -> bool:
    if not new_file_path.exists() or \
        new_file_path.is_dir() or \
        new_file_path.suffix != TSP_FILE_TYPE:
        return False

    global file_path
    file_path = new_file_path
    set_file_previewed(False)
    
    if not get_file_loaded():
        set_file_loaded(True)

    if parent != None:
        parent.event_generate("<<CheckStep>>")

    return True
