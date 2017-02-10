# decision tree regression by 2blam

setwd("~/Documents/Git/ML/decision_tree_regression")

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

# fit the decision tree regression to the dataset
#install.packages("rpart") #install for the first time
library(rpart)
# it is better to provide the minsplit, otherwise the decision tree only with only 1 rule
# i.e. taking the mean value of Salary and then return
regressor = rpart(formula = Salary ~ ., data=dataset, control=rpart.control(minsplit = 1)) 

#predict
y_pred = predict(regressor, data.frame(Level=6.5))

# plot
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() + 
  geom_point(aes(x=dataset$Level, y=dataset$Salary), 
             colour="red") +
  geom_line(aes(x=x_grid, y=predict(regressor, newdata=data.frame(Level=x_grid))),
            colour="blue") +
  ggtitle("Position Level vs Salary (Decision tree regression)") +
  xlab("Position Level") + 
  ylab("Salary")
