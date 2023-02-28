import numpy as np


def expand_prob_matrix(data, comm_sizes):
    """Expects 2 block sbm matrix and returns a matrix of size (size, size)

    Parameters
    ----------
    data : _type_
        _description_
    comm_sizes : _type_
        _description_
    """

    n_blocks = data.shape[0]
    n_sizes = len(comm_sizes)

    if n_blocks != n_sizes:
        raise ValueError("Number of blocks must match number of community sizes")

    # do rows
    rows = np.vstack(
        [np.repeat(data[[idx], :], size, axis=0) for idx, size in enumerate(comm_sizes)]
    )

    # do columns
    out = np.hstack(
        [np.repeat(rows[:, [idx]], size, axis=1) for idx, size in enumerate(comm_sizes)]
    )

    return out
