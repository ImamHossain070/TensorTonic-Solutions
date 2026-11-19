import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.asarray(a, dtype = float)
    a = np.asarray(a, dtype = float)
    if np.all(a == 0) or np.all(b == 0):
        return 0.0
    return float(np.dot(a, b)/(np.linalg.norm(a) * np.linalg.norm(b)))