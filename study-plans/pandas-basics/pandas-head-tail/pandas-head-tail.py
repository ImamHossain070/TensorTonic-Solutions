import pandas as pd

def head_tail(data: dict, n: int) -> dict:
    """
    Returns head and tail as dictionaries mapping columns to value lists.
    """
    df = pd.DataFrame(data)

    return {
        "head":{col:list(df[col].head(n)) for col in df.columns.tolist()},
        "tail":{col:list(df[col].tail(n)) for col in df.columns.tolist()}
    }
