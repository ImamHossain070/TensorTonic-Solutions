import pandas as pd

def data_types_overview(data: dict) -> dict:
    """
    Returns a dictionary with dtypes, type_counts, and num_columns.
    """
    df = pd.DataFrame(data)
    return {
        "dtypes":{col:str(value) for col, value in df.dtypes.items()},
        "type_counts":{str(dtype):count for dtype, count in df.dtypes.value_counts().items()},
        "num_columns":len(df.columns)
    }
