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
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predict
y_pred = regressor.predict(X_test)