# linear regression

# import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# import dataset
dataset = pd.read_csv("Salary_Data.csv")

dataset.shape # dimension of the data: (# of row, # of columns)
dataset.columns # column names

X = dataset.iloc[:, :-1].values # get YearExperience column
y = dataset.iloc[:, 1].values # get Salary column (DV - dependent variable)

# split into training and testing dataset
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state=0) # 1/3 of the data for testing


# linear regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predict the result
y_pred = regressor.predict(X_test)

# plot
plt.scatter(X_train, y_train, color="red") #data point
plt.plot(X_train, regressor.predict(X_train), color="blue") #regression line
plt.title("Salary vs Years of Experience (Training Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

plt.scatter(X_test, y_test, color="red") #data point
plt.plot(X_train, regressor.predict(X_train), color="blue") #regression line
plt.title("Salary vs Years of Experience (Test Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()