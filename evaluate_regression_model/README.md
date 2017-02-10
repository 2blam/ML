## R-squared

SS_res = SUM(y_i - y_i_hat)^2
SS_tot = SUM(y_i - y_avg)^2
R^2 = 1 - (SS_res / SS_tot)

R-squared / R^2 
- Goodness of fit
- the closer the value to 1, the model is better; the greater is better
- try to mininize the sum of square residuals SS_res
- Problem: adding new predictor / variable => R^2 will never decrease
- Reason: Refer to the R^2 formula, 1 and SS_tot is fixed (constant), when adding a new predict, SS_res would be increased!
- Solution: Adjusted R-squared

## Adjusted R-squared

Adj R^2 = 1 - (1 - R^2)* (n - 1) / (n - p - 1)

where 
p - number of regressors (independent variables/predictors)
n - sample size



