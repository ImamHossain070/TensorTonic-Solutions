import pandas as pd

def inspect_dataframe(data: dict) -> dict:
    """
    Returns rows, cols, columns, dtypes, and total_values in a dictionary.
    """
    df = pd.DataFrame(data)

    return {
        "rows":df.shape[0],
        "cols":df.shape[1],
        "columns":df.columns.tolist(),
        "dtypes":{col:str(value)  for col, value in df.dtypes.items()},
        "total_values":df.size
    }
