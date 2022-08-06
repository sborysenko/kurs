import pandas as pd
from numpy import NaN
import os


def fill_nan_column(df, col):
    val = NaN
    for i, r in df.iterrows():
        if pd.isna(r[col]):
            if not pd.isna(val):
                df.iloc[[i], [col]] = val
        else:
            val = r[col]
    return df


def convert_room_num(df):
    for i, r in df.iterrows():
        if r[1].find('1-') == 0:
            df.iloc[[i], [1]] = 1
        elif r[1].find('2-') == 0:
            df.iloc[[i], [1]] = 2
        elif r[1].find('3-') == 0:
            df.iloc[[i], [1]] = 3
        elif r[1].find('4-') == 0:
            df.iloc[[i], [1]] = 4
    return df


def convert_district(df):
    for i, r in df.iterrows():
        if r[0] == 'Голосіївський':
            df.iloc[[i], [0]] = 1
        elif r[0] == 'Дарницький':
            df.iloc[[i], [0]] = 2
        elif r[0] == 'Деснянський':
            df.iloc[[i], [0]] = 3
        elif r[0] == 'Дніпровський':
            df.iloc[[i], [0]] = 4
        elif r[0] == 'Оболонський':
            df.iloc[[i], [0]] = 5
        elif r[0] == 'Печерський':
            df.iloc[[i], [0]] = 6
        elif r[0] == 'Подільський':
            df.iloc[[i], [0]] = 7
        elif r[0] == 'Святошинський':
            df.iloc[[i], [0]] = 8
        elif r[0] == "Солом'янський":
            df.iloc[[i], [0]] = 9
        elif r[0] == 'Шевченківський':
            df.iloc[[i], [0]] = 10
    return df


def rename_columns(df):
    df.columns.values[0] = "district"
    df.columns.values[1] = "rooms"
    df.columns.values[2] = "average_area"
    df.columns.values[3] = "average_price"
    return df


def convert_column_to_int(df, col):
    for i, r in df.iterrows():
        df.iloc[[i], [col]] = r[col].replace(" ", "")
    df[df.columns.values[col]] = pd.to_numeric(df[df.columns.values[col]])
    return df


def read_dataset(folder, filename):
    df = pd.read_csv(folder + "/" + filename)
    df = df.drop([0, 1, 2, 3, 4]).reset_index(drop=True)
    df = df.drop(df.columns[[3, 4, 5, 6, 7, 9]], axis=1)
    df = fill_nan_column(df, 0)
    df = df.dropna().reset_index(drop=True)
    df = convert_district(df)
    df = convert_room_num(df)
    df = rename_columns(df)
    df = convert_column_to_int(df, 2)
    df = convert_column_to_int(df, 3)

    tokens = filename.split(".")
    df.insert(0, 'year', int(tokens[0]))
    df.insert(1, 'month', int(tokens[1]))
    return df


files = os.listdir("data")
files.sort()
print(files)
if len(files) > 0:
    data = read_dataset("data", files[0])
    for i in range(1, len(files)):
        data = pd.concat([data, read_dataset("data", files[i])])
    data = data.reset_index(drop=True)

print(data)
print(data.dtypes)
data.to_csv("dataframe.csv", index=False)
