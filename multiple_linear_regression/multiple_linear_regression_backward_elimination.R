# multiple linear regression (by 2blam)

setwd("~/Documents/Git/ML/multiple_linear_regression")

# import dataset
dataset = read.csv("50_Startups.csv")

# encode categorical data
dataset$State = factor(dataset$State, 
                         levels=unique(dataset$State),
                         labels=c(1, 2, 3))

# split into training and testing dataset
#install.packages("caTools") - first time installation
library(caTools) # for splitting dataset
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split)
test_set = subset(dataset, !split)

# build the optimal model using Backward Elimination
regressor = lm(formula = Profit ~ R.D.Spend+Administration+Marketing.Spend+State, data=training_set) 

summary(regressor)

#State2 and State3 with the highest p-value as 0.974 and 0.954 respectively, remove these 2 predictors
regressor = lm(formula = Profit ~ R.D.Spend+Administration+Marketing.Spend, data=training_set) 
summary(regressor)

#Administration with the highest p-value as 0.609 , remove this
regressor = lm(formula = Profit ~ R.D.Spend+Marketing.Spend, data=training_set) 
summary(regressor)

#Marketing.Spend with the highest p-value as 0.0713 , remove this
regressor = lm(formula = Profit ~ R.D.Spend, data=training_set) 
summary(regressor)

# we now get the optimal model
# R.D.Spend is the most powerful predictor for profit

