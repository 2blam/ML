## False Positives & Negatives

Type I Error - False Positive (less dangerous ~ like warning)
Type II Error - False Negative (more dangerous)

|		|Predicted Positive	|Predicted Negative	|
|---------------|-----------------------|-----------------------|
|Actual Positive|True Positive		|False Negative (Type II)|
|Actual Negative|False Positive (Type I)|True Negative		|

Accuracy Rate 
= Correct / Total
= (True Positive + True Negative) / Total

Error Rate
= Incorrect / Total
= (False Negative + False Positive) / Total

## Cumulative Accuracy Profile (CAP) Curve

- namely, gain chart
- straight line - random model
- the curve under the straight line, bad model (works worst than the random model) 
- the more the area between the curve and the straight line, the better the model is

Note:
- ROC - Receiver Operating Characteristic 
- ROC is not the same as CAP!

## CAP Analysis

- check the 50% of the x-axis, and then check the projected value in y-axis
- if the projected value in y-axis is
  < 60%  - dump it..
  between 60% and 70% - poor
  between 70% and 80% - good
  between 80% and 90% - v. good
  between 90% and 100% - too good (overfitting ?)


