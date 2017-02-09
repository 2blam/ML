### Description

Topic: Regression

In the dataset, there are five columns:
- R & D Spend
- Administration
- Marketing Spend
- State
- Profit

Q: Which type of company should be invested ?

In this demo, I will show how to use multiple linear regression to find out solution.

## IMPORTANT
- dummy variables trap (always omit one dummy variable)

## Different approaches in building a model
** All-in **
1. use all the predictors to create the model (maybe not useful, hard to explain)

** Backward Elimination (fast) **
1. select a significance level to stay in the model (e.g. sl = 0.05)
2. fit the full model with all possible predictors
3. consider the predictor with the highest p-value. If P > SL, go to step 4, otherwise, FINISH (model is finished).
4. remove the predictor
5. fit the model without this variable, go back to step 3.

** Forward Selection **
1. select a significance level to stay in the model (e.g. sl = 0.05)
2. fit all simple regression models y ~ x_n ; select the one with the lowest p-value
3. keep this variable and fit all possible models with one extra predictor added to the one(s) you already have
4. consider the predictor with the lowest p-value. If P < SL, go to step 3, otherwise, FINISH (the previous model is the best).

** Bidirectional Elimination **
1. select a significance level to enter and to stay in the model (e.g. sl_enter = 0.05; sl_stay = 0.05)
2. perform the next step of Forward Selection (new variables must have: P < sl_enter to enter)
3. perform ALL steps of Backward Elimination (old variables must be P < sl_stay to stay)
4. move back to step 2
5. if no new variables can enter and no old variables can exit, FINISH (the model is ready).

** All Possible Models / Score Comparsion (time consuming) **
1. select a criterion of goodness of fit (e.g. Akaike criterion)
2. construct all possible regression models: 2^n -1 total combinations where n is the number of predictors
3. select the one with the best criterion 
