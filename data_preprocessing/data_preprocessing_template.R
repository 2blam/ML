# data proprocessing

# set working directory
setwd("~/Documents/Git/ML/data_preprocessing")

# import dataset
dataset = read.csv("Data.csv")
#dataset = dataset[, 2:3]

# Consideration:
# missing data - mean value ?
# encode categorical data ?

# split into training and testing dataset
#install.packages("caTools") - first time installation
library(caTools) # for splitting dataset
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split)
test_set = subset(dataset, !split)

# rescale feature values
# training_set[, 2:3] = scale(training_set[, 2:3]) #only rescale Age and Salary columns
# test_set[, 2:3] = scale(test_set[, 2:3])