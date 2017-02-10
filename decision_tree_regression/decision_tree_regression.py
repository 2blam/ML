# decision tree regression by 2blam

# import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# import dataset
dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1:2].values # 2nd column
y = dataset.iloc[:, 2].values # 3rd column

# split into training and testing dataset
"""
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0) # 20% for testing dataset
"""

# re-scale feature values
"""
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test) #apply transform to test set as well
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)
"""

# fit the Decision tree regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0) #set the random seed value
regressor.fit(X, y)

# predict 
y_pred = regressor.predict(6.5) 

# smoother curve
X_grid = np.arange(min(X), max(X), 0.01) 
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color="red")
plt.plot(X_grid, regressor.predict(X_grid), color="blue")
plt.title("Position Level vs Salary (Decision tree regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()