import numpy as np
from graspologic.align import OrthogonalProcrustes, SeedlessProcrustes


def difference(
    X1: np.ndarray,
    X2: np.ndarray,
    test_case,
) -> float:
    if test_case == "exact":
        CX = compute_constant(X1)
        CY = compute_constant(X2)
        
        denom = CX + CY
        
        # X1 /= denom
        # X2 /= denom
    elif test_case == "global":
        CX = compute_constant(X1)
        CY = compute_constant(X2)
        
        normX1 = np.linalg.norm(X1, ord="fro")
        normX2 = np.linalg.norm(X2, ord="fro")
        X1 = X1 / normX1
        X2 = X2 / normX2
        
        denom = 2 * (CX / normX1 + CY / normX2)

        # X1 /= denom
        # X2 /= denom

    elif test_case == "vertex":
        normX1 = np.sum(X1**2, axis=1)
        normX2 = np.sum(X2**2, axis=1)
        normX1[normX1 <= 1e-15] = 1
        normX2[normX2 <= 1e-15] = 1
        X1 = X1 / np.sqrt(normX1[:, None])
        X2 = X2 / np.sqrt(normX2[:, None])

        denom = 2 * (1 / np.sqrt(normX1).min() + 1 / np.sqrt(normX2).min())
        # X1 /= denom
        # X2 /= denom
    else:
        raise ValueError()

    aligner = OrthogonalProcrustes()
    X1 = aligner.fit_transform(X1, X2)
    X1 /= denom
    X2 /= denom
    return X1 - X2


def compute_constant(X):
    P = X @ X.T
    D = np.sum(P - P**2, axis=1)
    D[D < 0] = 0
    D = D.reshape(-1, 1)

    S, U = np.linalg.eig(X.T @ X)
    C = U @ np.diag(1 / S**2) @ U.T
    CX = np.sum(np.diag(C @ (X * np.sqrt(D)).T @ (X * np.sqrt(D))))

    return np.sqrt(CX)


def difference_norm(
    X1: np.ndarray,
    X2: np.ndarray,
    test_case,
) -> float:
    X = difference(X1, X2, test_case)

    return np.linalg.norm(X) 
