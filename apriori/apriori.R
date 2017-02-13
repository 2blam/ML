# apriori by 2blam

# set working directory
setwd("~/Documents/Git/ML/apriori")

#read the dataset
#install.packages("arules")
library(arules)
#dataset = read.csv("Market_Basket_Optimisation.csv", header=FALSE)
dataset = read.transactions("Market_Basket_Optimisation.csv", sep=",", rm.duplicates=TRUE)
summary(dataset)
itemFrequencyPlot(dataset, topN=10)

#training apriori
rules = apriori(data=dataset, parameter=list(support=0.004, confidence=0.2))
# support: 
# purchase 3 time per day * 7 / 7500 ~ 0.0028 ~0.003
# purchase 4 time per day * 7 / 7500 ~ 0.004
# confidence: 0.8 (0 rule) -> 0.4 (281 rules) -> 0.2 (1348 rules)

#visualize
inspect(sort(rules, by="lift")[1:10])
