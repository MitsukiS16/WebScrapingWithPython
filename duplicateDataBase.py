import pandas as pd

def my_duplicateDataBase():
    file_name = "cardDBaz.csv"
    file_name_output = "cardDBaz.csv"

    df = pd.read_csv(file_name, sep=',')
 
    df.drop_duplicates(subset=None, inplace=True)

    df.to_csv(file_name_output, index=False)