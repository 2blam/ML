# multiple linear regression by 2blam

# import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import dataset
dataset = pd.read_csv("50_Startups.csv")
X = dataset.iloc[:, :-1].values #R&D Spend, Administration, Marketing Spend, State
y = dataset.iloc[:, 4].values #Profit

# encode categorical data ?
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
encodeColIdx = 3 # 3 == State column
X[:, encodeColIdx] = labelencoder_X.fit_transform(X[:, encodeColIdx]) # State--> 0, 1, 2
onehotencoder = OneHotEncoder(categorical_features=[encodeColIdx]) # create dummy variable representation, i.e. 0 --> 1 0 0; 1 --> 0 1 0; 2 --> 0 0 1
X = onehotencoder.fit_transform(X).toarray()

# avoid the dummy variable trap
X = X[:, 1:] # remove the 1st column (i.e. remove 1 dummy variable)
# NOTE:
#  even we don't not provide the above statement,
#  the library would handle about the dummy variable trap

# split into training and testing dataset
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0) # 20% for testing dataset

# multiple linear regression
# look for optimal model by backward elimination
import statsmodels.formula.api as sm
#  y = b_0 + b_1*x_1 + b_2*x_2 + ... + b_n*x_n
#  ==> 
#  y = b_0*x_0+ b_1*x_1 + b_2*x_2 + ... + b_n*x_n where x_0 = 1

# it is required to add an extra column with all values as 1 as the 1st column of X
X = np.append(arr=np.ones((X.shape[0], 1)).astype(int), values=X, axis=1) #X.shape[0] === num of rows in X; axis: 0 === row; 1 === col
X_opt = X[:, [0,1,2,3,4,5]] # consider all predictors at the beginning
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() #ordinary least square
regressor_OLS.summary()

#x2 with the highest p value as 0.990 , remove this predictor
X_opt = X[:, [0,1,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() #ordinary least square
regressor_OLS.summary()

#x1 with the highest p value as 0.940, remove this predictor
X_opt = X[:, [0,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() #ordinary least square
regressor_OLS.summary()

#x2 with the highest p value as 0.602, remove this predictor
X_opt = X[:, [0,3,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() #ordinary least square
regressor_OLS.summary()

#x2 with the highest p value as 0.060, remove this predictor
X_opt = X[:, [0,3]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() #ordinary least square
regressor_OLS.summary()

# the rest of the p-values are less than 0.05, the model is optimal now
# R&D Spend is the most powerful predictor for profit