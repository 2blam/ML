# data proprocessing

# set working directory
setwd("~/Documents/Git/ML/data_preprocessing")

# import dataset
dataset = read.csv("Data.csv")

# missing data - mean value
dataset$Age = ifelse(is.na(dataset$Age), 
                      ave(dataset$Age, FUN= function(x) mean(x, na.rm=TRUE)), 
                      dataset$Age
                     )
dataset$Salary = ifelse(is.na(dataset$Salary), 
                     ave(dataset$Salary, FUN= function(x) mean(x, na.rm=TRUE)), 
                     dataset$Salary
)

# encode categorical data
dataset$Country = factor(dataset$Country, 
                         levels=c("France", "Spain", "Germany"),
                         labels=c(1, 2, 3))

dataset$Purchased = factor(dataset$Purchased, 
                         levels=c("No", "Yes"),
                         labels=c(0, 1))

# split into training and testing dataset
#install.packages("caTools")
library(caTools) # for splitting dataset
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)

training_set = subset(dataset, split)
test_set = subset(dataset, !split)

# rescale feature values
training_set[, 2:3] = scale(training_set[, 2:3]) #only rescale Age and Salary columns
test_set[, 2:3] = scale(test_set[, 2:3])