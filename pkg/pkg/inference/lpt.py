import numpy as np
from graspologic.align import OrthogonalProcrustes


def difference_norm(
    X1: np.ndarray,
    X2: np.ndarray,
    test_case,
) -> float:
    if test_case == "exact":
        denom=1.
    elif test_case == "global":
        normX1 = np.linalg.norm(X1, ord="fro")
        normX2 = np.linalg.norm(X2, ord="fro")
        X1 = X1 / normX1
        X2 = X2 / normX2
        denom = 1/normX1 + 1/normX2
        
        X1 /= denom
        X2 /= denom
        
    elif test_case == "vertex":
        normX1 = np.linalg.norm(X1, axis=1)
        normX2 = np.linalg.norm(X2, axis=1)
        X1 = X1 / np.sqrt(normX1[:, None])
        X2 = X2 / np.sqrt(normX2[:, None])
        
        denom = 1/normX1.min() +1/normX2.min()
        X1 /= denom
        X2 /= denom
    else:
        raise ValueError()
        
    aligner = OrthogonalProcrustes()
    X1 = aligner.fit_transform(X1, X2)
    return X1 - X2
