from pathlib import Path

import numpy as np
from graspologic.utils import import_edgelist, pass_to_ranks


def load_dataset(
    parcellation="Desikan",
    preprocess=None,
    ptr="simple-nonzero",
):
    """
    Parameters
    ----------
    parcellation : str
        Must be {AAL, CPAC200, DKT, Desikan, Glasser, Schaefer1000, Schaefer200,
        Schaefer300, Schaefer400, Slab1068, Slab907, Talairach, Yeo-17-liberal,
        Yeo-17, Yeo-7-liberal, Yeo-7}

    preprocess : str
        Removes edges such that all graphs have same number of edges

    method : {'simple-nonzero' (default), 'simple-all', 'zero-boost'} string, optional
        Pass to ranks method

    Returns
    -------
    graphs
    """
    PARCELLATIONS = [
        "AAL",
        "CPAC200",
        "DKT",
        "Desikan",
        "Glasser",
        "Schaefer1000",
        "Schaefer200",
        "Schaefer300",
        "Schaefer400",
        "Yeo-17-liberal",
        "Yeo-17",
        "Yeo-7-liberal",
        "Yeo-7",
    ]

    module_path = Path(__file__).absolute().parents[2]

    p = Path(module_path.parent / "data/graphs")

    if not p.exists():
        msg = "You must download the data using the script first."
        raise ValueError(msg)

    if parcellation not in PARCELLATIONS:
        msg = "You must pass valid parcellation name."
        raise ValueError(msg)

    # load all graphs
    p = sorted(list((p / f"{parcellation}_space-MNI152NLin6_res-1x1x1").glob("*.csv")))
    graphs = import_edgelist(p)

    if preprocess == "remove_edges":
        minimum_edges = np.min([np.count_nonzero(g) for g in graphs])
        graphs = [remove_edges(g, minimum_edges) for g in graphs]

    if ptr in ["simple-nonzero", "simple-all", "zero-boost"]:
        graphs = [pass_to_ranks(g, method=ptr) for g in graphs]

    graphs = {f.parts[-1].split("_")[0].split("-")[1]: g for (f, g) in zip(p, graphs)}

    return graphs


def remove_edges(graph, total_edges):
    graph = graph.copy()
    uniques, counts = np.unique(graph[graph > 0], return_counts=True)
    cum_sum = np.cumsum(counts[::-1])

    argmin = np.argmin(np.abs(cum_sum - total_edges))
    target_value = uniques[::-1][argmin]
    np.putmask(graph, graph < target_value, 0)

    return graph
