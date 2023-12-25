import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score

#Loading the dataset
df = pd.read_csv("data.csv")
feature_cols = list(df.columns[:-1])  # assuming the class column is the last one in your dataset
X = pd.get_dummies(df[feature_cols])
y = df["class"]
x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.25)

# 1. Create a Random Forest Classifier and print its parameters
rf = RandomForestClassifier()
print('Random Forest base parameters', rf.get_params())

# 2. Fit the Random Forest Classifier to training data and calculate accuracy score on the test data
rf.fit(x_train, y_train)
y_pred = rf.predict(x_test)
print('Test set accuracy', accuracy_score(y_test, y_pred))

# 3. Calculate Precision score and the Confusion Matrix
print('Test set precision', precision_score(y_test, y_pred))
print('Test set confusion matrix', confusion_matrix(y_test, y_pred))


"""
# choices
----------
params()
evaluation
ensemble
precision_score
metrics
get_params()
tree
(y_test, y_pred)
(x_test,y_test)
precision
"""