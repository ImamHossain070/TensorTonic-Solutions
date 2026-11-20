from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    originalArray = np.asarray(x)
    vals, counts = np.unique(originalArray, return_counts=True)
    mode = vals[counts.argmax()]   
    results = {
        "mean":float(np.mean(originalArray, dtype = float)),
        "median":float(np.median(originalArray)), 
        "mode":float(mode)
    }

    return results