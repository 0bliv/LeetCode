import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    x = 100
    resp = animals[animals['weight'] > x].sort_values(by='weight',ascending = False)[['name']]
    return resp

