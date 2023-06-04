
import pandas as pd
import os
from os.path import realpath, dirname
from pathlib import Path


# could be in config file
base_path = Path(dirname(realpath(__file__)))
data_folder_path = base_path/'data'
base_file_name = '2022_fantasy_pros_weekly_points_'

def process_fantasy_pros_data(scoring_type:str,**kwargs)->pd.DataFrame:
    file_path = data_folder_path/"".join([base_file_name,scoring_type,'.csv'])

    if not file_path.exists():
        raise FileNotFoundError()

    df = pd.read_csv(file_path,**kwargs)
    df = df.rename(
        
        {
             col:col.lower()

        for col in df.columns}
        
        ,axis=1)
    
    df = df.loc[df['#'].notnull()].reset_index(drop=True)

    return df


def main()->None:
    #print(dirname(realpath(__file__)))
    process_fantasy_pros_data('full')

if __name__ == '__main__':
    main()