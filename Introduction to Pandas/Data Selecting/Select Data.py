import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    info = students.loc[students['student_id'] == 101,['name','age']]
    return info