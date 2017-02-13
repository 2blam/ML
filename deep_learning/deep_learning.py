# deep learning / artifical neural network by 2blam

# import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# import dataset
dataset = pd.read_csv("Churn_Modelling.csv")
X = dataset.iloc[:, 3:13].values  #column index 3 - 12 
y = dataset.iloc[:, 13].values #Exited? 1 - true; 0 - false

# encode categorical data 
# country
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
# gender
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])

# create dummy variables for country X X X
onehotencoder = OneHotEncoder(categorical_features=[1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:] # avoid dummy variable trap, remove 1 dummy variable column

# split into training and testing dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state=0) # 25% for testing dataset

# re-scale feature values
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test) 

# create neural network
import keras
from keras.models import Sequential
from keras.layers import Dense

# initalize neural network; 
# NOTE: more than 1 hidden layers, in theory, we call it deep neural network
classifier = Sequential()

# add the input layer & 1st hidden layer
classifier.add(Dense(output_dim=6,
                     init="uniform",
                     activation="relu",
                     input_dim=11)) #set input_dim for the 1st layer only

# add 2nd hidden layer
classifier.add(Dense(output_dim=6,
                     init="uniform",
                     activation="relu"))
                     
# add output layer
# 1 class (e.g. yes vs no): output_dim = 1 AND activation = sigmoid
# n classes (one hot encode): output_dim = n AND activation = softmax
classifier.add(Dense(output_dim=1,
                     init="uniform",
                     activation="sigmoid"))
# compile neural network
# adam - Adaptive Moment Estimation 
# binary_crossentropy - https://keras.io/objectives/
classifier.compile(optimizer="adam",
                   loss="binary_crossentropy",
                   metrics=["accuracy"])

# fit training data to neural network
# batch_size - update the weight only after finish a batch of records
# epoch - 1 epoch is equal to the whole training set passed through the neural network
classifier.fit(X_train, y_train, batch_size=10, nb_epoch=100)

# save the model
from keras.models import load_model
classifier.save("nn_model.h5")
# load the model
del classifier
classifier = load_model("nn_model.h5")

# predict
y_pred = classifier.predict(X_test) #probabilty
y_pred = (y_pred > 0.5)

# confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

accuracy = 1.0*(cm[0,0] + cm[1,1]) / (cm[0,0]+cm[0,1]+cm[1,0]+cm[1,1])
