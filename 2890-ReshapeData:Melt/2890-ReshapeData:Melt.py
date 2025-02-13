import pandas

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pandas.melt(report, id_vars='product', var_name='quarter', value_name='sales')