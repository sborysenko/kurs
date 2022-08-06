import pandas as pd

data = pd.read_csv("dataframe.csv")
corr_matrix = data.corr().round(2)

print(corr_matrix)
