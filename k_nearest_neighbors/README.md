### Description

Topic: Classification

Mission: 

The dataset contains the information about the customers in social network.
Car company would like to check which customer(s) in the social network would like to buy their new SUV.

Consider the column about Age and EstimatedSalary in the dataset, create the model to predict if a customer would purchase the new SUV.

Model: k nearest neighbors (knn)

Idea:
1) choose the number k of the neighbors; (k is better to be odd number)
2) take the k nearest neighbors of the new data point by using Euclidean distance
3) among these k neighbors, count the number of data points in each class
4) for the class with the most number of data points, assign the new data point to such class

