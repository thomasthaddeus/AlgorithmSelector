"""
loaded a modified version of FiveThirtyEight’s Candy Power Ranking data. Here, we have a rating column that’s binary and indicates whether or not a candy had a winning percentage >= 50% (1) or not (0). Using the rating column as the target variable and the rest of the columns (barring winpercent and competitorname) as the predictor variables, we’ve trained and tested a decision tree model. Calculate the following characteristics of this classifier:

Depth of the decision tree and save your answer as depth_dtree
Precision score on test data and save your answer as precision_dtree
F1 score on test data and save your answer as f1_dtree
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, precision_score

df = pd.read_csv('candy_rating_binary.csv')
#print(df.head())

#Define target and predictor variables
y = df.rating
X = df[['chocolate', 'fruity', 'caramel', 'peanutyalmondy',
       'nougat', 'crispedricewafer', 'hard', 'bar', 'pluribus', 'sugarpercent',
       'pricepercent']]

# Build a Decision Tree Classifier
x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.2)
dtree = DecisionTreeClassifier()
print(f'Decision Tree parameters: {dtree.get_params()}')
dtree.fit(x_train, y_train)


# Get the depth of the decision tree
depth_dtree = dtree.get_depth()
print(f'Depth of the decision tree: {depth_dtree}')

# Predict on the test data
y_pred = dtree.predict(x_test)

# Get the precision score on the test data
precision_dtree = precision_score(y_test, y_pred)
print(f'Precision score on test data: {precision_dtree}')

# Get the F1 score on the test data
f1_dtree = f1_score(y_test, y_pred)
print(f'F1 score on test data: {f1_dtree}')

