import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df1 = views[(views['author_id']==views['viewer_id'])]
    df2 = df1.drop_duplicates(subset='author_id')
    df3 = df2[['author_id']]
    return df3.rename(columns={'author_id':'id'}).sort_values(by='id', ascending=True)
