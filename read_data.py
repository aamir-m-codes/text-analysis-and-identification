import pandas as pd

def read_csv():
    df = pd.read_csv('data/dataset02.csv')
    return df

def read_data_merged():
    df1 = pd.read_csv('data/dataset01.csv')
    df2 = pd.read_csv('data/dataset02.csv')
    df2['label'] = df2['label'].astype(int)

    merged_df = pd.concat([df1, df2], ignore_index=True)

    # print(df1.shape)
    # print(df2.shape)
    # print(merged_df.shape)
    # print(merged_df.columns)
    # print(merged_df['label'].unique())

read_data_merged()