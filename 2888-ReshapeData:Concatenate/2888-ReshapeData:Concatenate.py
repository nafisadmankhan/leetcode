import pandas

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pandas.concat([df1,df2],axis=0)