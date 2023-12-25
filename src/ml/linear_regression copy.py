"""
_summary_

_extended_summary_
"""

# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Read in the data
# Three headers: score, completed, lesson
content = pd.read_csv('../../data/content.csv')

def show_clr():
    plt.show()
    plt.clf()
    return

# Print the first five rows
print(content.head())

# Create a scatter plot of score vs completed
plt.scatter(content.completed, content.score)
plt.xlabel('Completed')
plt.ylabel('Score')
plt.title('Score vs Completed')

show_clr()

# Fit a linear regression to predict score based on prior lessons completed
X = sm.add_constant(content.completed)
y = content.score

model = sm.OLS(y, X).fit()

# Intercept interpretation:
intercept = model.params[0]
print(f'Intercept: {intercept}')

# Slope interpretation:
slope = model.params[1]
print(f'Slope: {slope}')

# Plot the scatter plot with the line on top
plt.scatter(content.completed, content.score)
plt.plot(content.completed, model.predict(), color='red')
plt.xlabel('Completed')
plt.ylabel('Score')
plt.title('Score vs Completed with Regression Line')

show_clr()

# Predict score for learner who has completed 20 prior lessons
new_completed = 20
new_completed_with_constant = sm.add_constant(new_completed)

predicted_score = model.predict(new_completed_with_constant)
print(f'Predicted score for 20 completed lessons: {predicted_score}')

# Calculate fitted values
fitted_values = model.fittedvalues
print(f'Fitted values: {fitted_values}')

# Calculate residuals
residuals = model.resid
print(f'Residuals: {residuals}')

# Check normality assumption
sm.qqplot(residuals, line='s')

show_clr()

# Check homoscedasticity assumption
plt.scatter(fitted_values, residuals)
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs Fitted Values')

show_clr()

# Create a boxplot of score vs lesson
sns.boxplot(x=content.lesson, y=content.score)
plt.xlabel('Lesson')
plt.ylabel('Score')
plt.title('Score vs Lesson')

show_clr()

# Fit a linear regression to predict score based on which lesson they took
X_lesson = pd.get_dummies(content.lesson, drop_first=True)
X_lesson = sm.add_constant(X_lesson)

model_lesson = sm.OLS(y, X_lesson).fit()

# Calculate and print the group means and mean difference (for comparison)
group_means = content.groupby('lesson').mean()['score']
mean_difference = group_means[1] - group_means[0]
print(f'Mean difference: {mean_difference}')

# Use `sns.lmplot()` to plot `score` vs. `completed` colored by `lesson`
sns.lmplot(x='completed', y='score', data=content, hue='lesson')

plt.show()