import pandas as pd

def my_duplicateDataBase(file_name):
    df = pd.read_csv(file_name, sep=',')
    df.drop_duplicates(subset=None, inplace=True)
    df.to_csv(file_name, index=False)