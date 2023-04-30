import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the dataset into a Pandas dataframe
df = pd.read_csv('../pages/dataset.csv')

# Select the columns of interest
columns_of_interest = ['Final pH', 'Yield per Plant']

# Create a scatter plot of pH vs yield
x = df['Final pH']
y = df['Yield per Plant']
plt.scatter(x, y)
plt.xlabel('Final pH')
plt.ylabel('Yield per Plant')
plt.show()

# Perform linear regression between pH and yield
slope, intercept, r_value, p_value, std_err = linregress(x, y)
print('Slope:', slope)
print('Intercept:', intercept)
print('R-squared:', r_value**2)