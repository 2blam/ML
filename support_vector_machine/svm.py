# svm by 2blam

# import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# import dataset
dataset = pd.read_csv("Social_Network_Ads.csv")
X = dataset.iloc[:, [2, 3]].values  #Age, EstimatedSalary
y = dataset.iloc[:, 4].values #Purchased

# split into training and testing dataset
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state=0) # 25% for testing dataset

# re-scale feature values
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test) 

# fit the svm to the training dataset
from sklearn.svm import SVC
classifier = SVC(kernel="linear", random_state=0) #linear 
classifier.fit(X_train, y_train)

# predict
y_pred = classifier.predict(X_test)

# confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# visualize training result
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start =X_set[:, 0].min()-1, stop=X_set[:, 0].max()+1, step = 0.01),
                     np.arange(start =X_set[:, 1].min()-1, stop=X_set[:, 1].max()+1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), alpha=0.75, cmap=ListedColormap(("red", "green")))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c=ListedColormap(("red", "green"))(i), label = j)
plt.title("SVM (Training set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()
plt.show()

# visualize test result
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start =X_set[:, 0].min()-1, stop=X_set[:, 0].max()+1, step = 0.01),
                     np.arange(start =X_set[:, 1].min()-1, stop=X_set[:, 1].max()+1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), alpha=0.75, cmap=ListedColormap(("red", "green")))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c=ListedColormap(("red", "green"))(i), label = j)
plt.title("SVM (Test set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()
plt.show()