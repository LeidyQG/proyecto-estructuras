
from .christofides import christofides_algorithm
from .two_opt import two_opt_algorithm
from .neighbor_delta import neighbor_delta_algorithm
from .neighbor_2otp import neighbor_opt_algorithm

ALGORITHMS_LIST: list[dict[str, any]] = [
    {
        "uid": 0,
        "name": "Christofides",
        "info_file": "christofides.json",
        "function": christofides_algorithm,
        "icon": "",
        "fg": "",
        "bg": ""
    },
    {
        "uid": 1,
        "name": "2-OPT",
        "info_file": "single_opt.json",
        "function": two_opt_algorithm,
        "icon": "",
        "fg": "",
        "bg": ""
    },
    {
        "uid": 2,
        "name": "Vecino (Delta)",
        "info_file": "neighbor_delta.json",
        "function": neighbor_delta_algorithm,
        "icon": "",
        "fg": "",
        "bg": ""
    },
    {
        "uid": 3,
        "name": "Vecino (2-OPT)",
        "info_file": "neighbor_opt.json",
        "function": neighbor_opt_algorithm,
        "icon": "",
        "fg": "",
        "bg": ""
    },
    # {
        # "uid": 4,
        # "name": "Matriz de Distancias",
        # "info_file": "distance_matrix.json",
        # "function": None,
        # "icon": "",
        # "fg": "",
        # "bg": ""
    # },
]

