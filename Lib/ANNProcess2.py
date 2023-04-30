# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.neural_network import MLPRegressor

# Load data into a pandas dataframe
df = pd.read_csv("your_dataset.csv")

# Select the input features and target
X = df.iloc[:, 4:12].values
y = df.iloc[:, 12:24].values

# Encode the "Has Harvest" column
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
X = ct.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Scale the input features
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Train the neural network
regressor = MLPRegressor(hidden_layer_sizes=(10, 10), max_iter=1000)
regressor.fit(X_train, y_train)

# Make predictions on the test set
y_pred = regressor.predict(X_test)

# Evaluate the performance of the neural network
score = regressor.score(X_test, y_test)
print("R^2 score:", score)