### Description

Topic: Classification

Mission: 

The dataset contains the information about the customers in social network.
Car company would like to check which customer(s) in the social network would like to buy their new SUV.

Consider the column about Age and EstimatedSalary in the dataset, create the model to predict if a customer would purchase the new SUV.

Model: Naive Bayes

Bayes Thm.
P(A|B) = P(B|A) * P(A) / P(B)

P(A) - prior probability
P(B) - marginal likelihood
P(B|A) - likelihood
P(A|B) - posterior probability

1) Assumption: Features are independent (that's reason call naive)
2) E.g.
Compare P(class1 | features) vs P(class2 | features)
==>
P(features | class1) * P(class1) / P(features) vs P(features | class2) * P(class2) / P(features)
==> [both side divided with the same factor P(features), we would eliminate it]
P(features | class1) * P(class1) vs P(features | class2 ) * P(class2)




