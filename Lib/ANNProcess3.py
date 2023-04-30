import pandas as pd

# Load the dataset into a Pandas dataframe
df = pd.read_csv('../pages/dataset.csv')

# Select the columns of interest
columns_of_interest = ['Initial pH' , 'Leaves Count']

# Calculate the correlation matrix
corr_matrix = df[columns_of_interest].corr()

# Print the correlation matrix
print(corr_matrix)

