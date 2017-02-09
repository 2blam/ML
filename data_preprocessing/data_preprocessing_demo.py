# data preprocessing

# import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# import dataset
dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:, :-1].values #first 3 columns
y = dataset.iloc[:, 3].values #last column

# missing data - fill in mean value 
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer = imputer.fit(X[:, 1:3]) #1:3 <-- upper bound excluded, i.e. extract column idx 1 and 2
X[:, 1:3] = imputer.transform(X[:, 1:3])

# encode categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0]) # name --> 0 or 1 or 2
onehotencoder = OneHotEncoder(categorical_features=[0]) # create dummy variable representation, i.e. 0 --> 1 0 0; 1 --> 0 1 0
X = onehotencoder.fit_transform(X).toarray()

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y) # Purchased (Yes/No)  --> 0 or 1

# split into training and testing dataset
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0) # 20% for testing dataset

# re-scale feature values
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test) #apply transform to test set as well

