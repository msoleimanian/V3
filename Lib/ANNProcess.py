# Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Load dataset
df = pd.read_csv('../pages/dataset.csv')
df = pd.read_csv('../pages/dataset.csv')
sub = 1
subdataframe = df.query(f'PotID == {sub}')
print(subdataframe)
# Preprocess data
X = subdataframe.iloc[:, 4:11].values # Input features (excluding PotID, Crop ID, Crop Name, EC Setting, Has Harvest, and Timestamp)
y = subdataframe.iloc[:, 13:20].values # Output variables (Height, Width, Leaves Count, Longest Leaf, Shortest Leaf, Yield per Plant, Yield per Land)

# Split dataset
X_train, X_val_test, y_train, y_val_test = train_test_split(X, y, test_size=0.4, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_val_test, y_val_test, test_size=0.5, random_state=42)

# Define model
model = Sequential()
model.add(Dense(64, input_shape=(X_train.shape[1],), activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(7)) # Output layer

# Compile model
model.compile(loss='mean_squared_error', optimizer=Adam(lr=0.001))

# Train model
history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=100, batch_size=32)

# Evaluate model on test set
results = model.evaluate(X_test, y_test)
print('Test loss:', results)

# Make predictions on new data
new_data = np.array([[3, 7, 2, 10, 5, 0.8, 25, 80, 8, 12, 10, 'oblong', 'white', 0.3, 'no', 0.5, 0.4, 0.2]])
predictions = model.predict(new_data)
print('Predictions:', predictions)