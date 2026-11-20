import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    originalArray = np.asarray(A)

    resultArray = np.zeros((originalArray.shape[1], originalArray.shape[0]), dtype = float)
    r = 0
    c = 0
    for row in originalArray:
        for value in row:
            resultArray[r, c] = value
            r +=1
        c += 1
        r = 0
    return resultArray