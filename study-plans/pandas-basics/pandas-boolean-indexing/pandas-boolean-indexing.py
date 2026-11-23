import pandas as pd

def boolean_filter(data: dict, column: str, threshold: float) -> dict:
    """
    Returns filtered_data as a dictionary of lists and count as an integer.
    """
    df = pd.DataFrame(data)
    
    con_data = df[df[column]>threshold]

    count = con_data.shape[0]

    return {
        "filtered_data":con_data.to_dict("list"),"count":int(count)
    }
