import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    resp = weather.pivot_table(index='month',columns='city',values ='temperature',  aggfunc='max')
    return resp