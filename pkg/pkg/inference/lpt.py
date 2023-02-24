import numpy as np
from graspologic.align import OrthogonalProcrustes


def difference_norm(
    X1: np.ndarray,
    X2: np.ndarray,
    test_case,
) -> float:
    if test_case == "exact":
        pass
    elif test_case == "global":
        X1 = X1 / np.linalg.norm(X1, ord="fro")
        X2 = X2 / np.linalg.norm(X2, ord="fro")
    elif test_case == "diagonal":
        normX1 = np.sum(X1**2, axis=1)
        normX2 = np.sum(X2**2, axis=1)
        normX1[normX1 <= 1e-15] = 1
        normX2[normX2 <= 1e-15] = 1
        X1 = X1 / np.sqrt(normX1[:, None])
        X2 = X2 / np.sqrt(normX2[:, None])
    aligner = OrthogonalProcrustes()
    X1 = aligner.fit_transform(X1, X2)
    return X1 - X2
