# decision tree (classification) by 2blam

# set working directory
setwd("~/Documents/GitHub/ML/decision_tree_classification")

# import dataset
dataset = read.csv("Social_Network_Ads.csv")
dataset = dataset[, 3:5]

# encode features as factor
dataset$Purchased = factor(dataset$Purchased, levels=c(0,1))

# split into training and testing dataset
#install.packages("caTools") - first time installation
library(caTools) # for splitting dataset
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.75)
training_set = subset(dataset, split)
test_set = subset(dataset, !split)

# # rescale feature values
# training_set[, 1:2] = scale(training_set[, 1:2]) 
# test_set[, 1:2] = scale(test_set[, 1:2])

# fit decision tree (classification) classifier
library(rpart)
classifier = rpart(formula = Purchased ~ ., data = training_set)

# predict 
y_pred = predict(classifier, newdata=test_set[-3], type="class") 

# confusion matrix
cm = table(test_set[, 3], y_pred)

# plot decision tree
plot(classifier)
text(classifier)