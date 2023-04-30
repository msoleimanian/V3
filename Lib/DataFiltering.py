import pandas as pd


dataframe = pd.read_csv('../pages/dataset.csv')
sub = 1
subdataframe = dataframe.query(f'PotID == {sub}')
print(subdataframe)
X = subdataframe.iloc[:, 4:11].values
print(X)
