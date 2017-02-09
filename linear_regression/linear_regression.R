# linear regression

# set working directory
setwd("~/Documents/Git/ML/linear_regression")

# import dataset
dataset = read.csv("Salary_Data.csv")

library(caTools) # for splitting dataset
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3) # 2/3 of data for training
training_set = subset(dataset, split)
test_set = subset(dataset, !split)

# linear regression
regressor = lm(formula = Salary ~ YearsExperience, data=training_set)
summary(regressor) 
# In Coefficients section, we can check that there is "***" symbols on the left hand size, 
#  it means that YearsExperience (independent variable) is highly statistical significance.
#  If there is no star, it means that there is no statistical significance.
# 
#  Pr(>|t|) === p-value
#   The lower the p-value is, the more significant in the independent variable.
#   The good threshold value for the p-value is 5%.
#   i.e. if the p-value is lower than 5%, then the independent variable is highly significance.
#        Otherwise, the independent variable is less significance.

# predict
y_pred = predict(regressor, newdata=test_set)

# plot
#install.packages("ggplot2") #first time installation
library(ggplot2)
ggplot() + 
  geom_point(aes(x=training_set$YearsExperience, y=training_set$Salary), 
             colour="red") +
  geom_line(aes(x=training_set$YearsExperience, y=predict(regressor, newdata=training_set)),
            colour="blue") +
  ggtitle("Salary vs Years of Experience (Training set)") +
  xlab("Years of Experience") + 
  ylab("Salary")

ggplot() + 
  geom_point(aes(x=test_set$YearsExperience, y=test_set$Salary), 
             colour="red") +
  geom_line(aes(x=training_set$YearsExperience, y=predict(regressor, newdata=training_set)),
            colour="blue") +
  ggtitle("Salary vs Years of Experience (Test set)") +
  xlab("Years of Experience") + 
  ylab("Salary")

