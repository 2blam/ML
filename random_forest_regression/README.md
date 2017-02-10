### Description

Topic: Regression

Mission: A new employee is working as a region manager for about 2 years,HR would like to check how much salary they should offer to this new employee. For the region manager with 2 years experience, refer to the dataset, the position level should be between 6 and 7. Suppose the positon level is 6.5, help the HR to predict the salary for this new employee.

Model: Random Forest Regression
- discrete

Idea:
1. pick a random k data points from the training data
2. build the decision tree by using these k data points
3. repeat step 1 and 2 until created N number of trees
4. for the new data point, predict the value by using N trees. Return the average value of the predicted values from those trees.

