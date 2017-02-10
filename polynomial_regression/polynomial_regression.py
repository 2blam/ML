# polynomial (linear) regression by 2blam

# import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# import dataset
dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1].values # Level column
y = dataset.iloc[:, 2].values # Salary column

# prefer using matrix representation, instead of vector (e.g. (10, ))
X = np.reshape(X, (X.shape[0], 1)) # e.g. (10, ) -> (10, 1)

#another approach - using 1:2 in the column index
# X = dataset.iloc[:, 1:2].values # Level column

# linear regression vs polynomial regression

# linear regression
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# polynomial regression
from sklearn.preprocessing import PolynomialFeatures
polyFeat = PolynomialFeatures(degree=2) #create the polynomial features with degree = 2
                                        # b_0*x_0 + b_1*x_1 + b_2*x_1^2
X_poly = polyFeat.fit_transform(X)

poly_reg = LinearRegression()
poly_reg.fit(X_poly, y)

# plot
plt.scatter(X, y, color="red")
plt.plot(X, lin_reg.predict(X), color="blue") #regression line
plt.title("Position Level vs Salary (Linear regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()

X_grid = np.arange(min(X), max(X), 0.1) 
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color="red")
plt.plot(X_grid, poly_reg.predict(polyFeat.fit_transform(X_grid)), color="blue") #smoother curve with more data point X_grid
plt.title("Position Level vs Salary (Polynomial regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()

# predict salary with position level 6.5
lin_reg.predict(6.5) 
poly_reg.predict(polyFeat.fit_transform(6.5)) #degree = 2; salary = 189498
               