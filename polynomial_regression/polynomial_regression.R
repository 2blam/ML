# polynomial regression by 2blam
setwd("~/Documents/Git/ML/polynomial_regression")

# import dataset
dataset = read.csv("Position_Salaries.csv")
dataset = dataset[, 2:3] #exclude the 1st column

# linear regression
lin_reg = lm(formula = Salary ~ ., data = dataset)

# polynomial regression
dataset$LevelSquare = dataset$Level^2
dataset$LevelCube = dataset$Level^3
poly_reg = lm(formula = Salary ~ ., data = dataset)

# plot
library(ggplot2)
ggplot() + 
  geom_point(aes(x=dataset$Level, y=dataset$Salary), 
             colour="red") +
  geom_line(aes(x=dataset$Level, y=predict(lin_reg, newdata=dataset)),
            colour="blue") +
  ggtitle("Position Level vs Salary (Linear regression)") +
  xlab("Position Level") + 
  ylab("Salary")

ggplot() + 
  geom_point(aes(x=dataset$Level, y=dataset$Salary), 
             colour="red") +
  geom_line(aes(x=dataset$Level, y=predict(poly_reg, newdata=dataset)),
            colour="blue") +
  ggtitle("Position Level vs Salary (Polynomial regression; degree = 3)") +
  xlab("Position Level") + 
  ylab("Salary")

#predict
# linear regression - salary = 330378
y_pred_lin_reg = predict(lin_reg, data.frame(Level=6.5)) 
# polynomial regression (degree=3)- salary = 133259
y_pred_poly_reg = predict(poly_reg, data.frame(Level=6.5, LevelSquare=6.5^2, LevelCube=6.5^3)) 