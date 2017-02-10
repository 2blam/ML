# polynomial regression by 2blam
#setwd("~/Documents/Git/ML/polynomial_regression")

# import dataset
dataset = read.csv("Position_Salaries.csv")
dataset = dataset[, 2:3] #exclude the 1st column

# split into training and testing dataset
#install.packages("caTools") - first time installation
# library(caTools) # for splitting dataset
# set.seed(123)
# split = sample.split(dataset$Purchased, SplitRatio = 0.8)
# training_set = subset(dataset, split)
# test_set = subset(dataset, !split)

# rescale feature values
# training_set[, 2:3] = scale(training_set[, 2:3]) #only rescale Age and Salary columns
# test_set[, 2:3] = scale(test_set[, 2:3])

# fit the regression model to the dataset

# create regressor here

#predict
y_pred = predict(regressor, data.frame(Level=6.5))

# plot
library(ggplot2)
ggplot() + 
  geom_point(aes(x=dataset$Level, y=dataset$Salary), 
             colour="red") +
  geom_line(aes(x=dataset$Level, y=predict(regressor, newdata=dataset)),
            colour="blue") +
  ggtitle("Position Level vs Salary (Regression Model)") +
  xlab("Position Level") + 
  ylab("Salary")

# plot smoother curve
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() + 
  geom_point(aes(x=dataset$Level, y=dataset$Salary), 
             colour="red") +
  geom_line(aes(x=x_grid, y=predict(regressor, newdata=data.frame(Level=x_grid))),
            colour="blue") +
  ggtitle("Position Level vs Salary (Regression Model)") +
  xlab("Position Level") + 
  ylab("Salary")
