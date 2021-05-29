import pandas as pd
import pathlib

from .db import (connection, verify_table)

def df_from_sql(table_name='spoonflower_links'):
    table_exists = verify_table(table_name)

    if not table_exists:
        df = pd.DataFrame()
    else:
        df = pd.read_sql_table(table_name, connection)

    return df

def df_to_sql(df, table_name:str='spoonflower_links', if_exists='replace'):
    df.to_sql(table_name, connection, if_exists=if_exists)
    return df

def list_to_sql(datas:list, table_name='spoonflower_links'):
    new_df = pd.DataFrame(datas)
    og_df = df_from_sql(table_name=table_name)

    if og_df.empty:
        df = new_df
    else:
        df = pd.concat([og_df, new_df])

    df.drop_duplicates(subset=['id'], inplace=True)

    df_to_sql(df, table_name=table_name)

def store_links_as_df_pickle(datas:list, path:str='links.pkl')-> pd.DataFrame:
    """Creates a Pandas DataFrame from the passed list, stores it in a pickle.
    attr:
        datas(list): List of dictionaries
        path(str)  : path of a pickle file if exists"""

    new_df = pd.DataFrame(datas, index='id')

    if pathlib.Path(path).exists():                     # if a previous dataframe pickle exists.
        og_df = pd.read_pickle(path)                    # get previous df
        df = pd.concat([og_df, new_df], sort=False)     # concatinate old & new df
        df.drop_duplicates(subset=['id'], inplace=True) # droping rows with same product id, avoid duplication.
        df.to_pickle(path)
        return df
    else:    
        new_df.to_pickle(path)
        return new_df
