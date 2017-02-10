# data preprocessing

# import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# import dataset
dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:, :-1].values #first 3 columns
y = dataset.iloc[:, 3].values #last column

# Consideration: 
# missing data - fill in mean value  ?
# encode categorical data ?

# split into training and testing dataset
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0) # 20% for testing dataset

# re-scale feature values
"""
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test) #apply transform to test set as well
"""