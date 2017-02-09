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

# multiple linear regression
regressor = lm(formula = Profit ~ ., data=training_set) #use . to represent using the rest of the predictors
summary(regressor)

#Note:
# In Coefficients, 
# 1) it always shows (Intercept) and R.D.Spend with "***". 
#    In other words, R.D.Spend is the most powerful predictor for profit
# 2) lm auto remove 1 dummy variable, i.e. avoid dummy variable trap

# predict
y_pred =predict(regressor, newdata=test_set)
