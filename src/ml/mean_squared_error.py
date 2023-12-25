"""mean_squared_error.py
A script that uses scikit-learn's multiple linear regression implementation to
build a model that predicts the rent of apartments in Manhattan. Evaluate this
model’s performance by calculating the Mean Squared Error (MSE) on training and
test data using the .score() method.

Save the training and test scores as train_score and test_score respectively
and print them.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# Load the dataset
streeteasy = pd.read_csv(
    "https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv"
)
df = pd.DataFrame(streeteasy)
# print(df.head())

# Define predictor and target variables
x = df[[
        "bedrooms",
        "bathrooms",
        "size_sqft",
        "min_to_subway",
        "floor",
        "building_age_yrs",
        "no_fee",
        "has_roofdeck",
        "has_washer_dryer",
        "has_doorman",
        "has_elevator",
        "has_dishwasher",
        "has_patio",
        "has_gym",
    ]]
y = df[["rent"]]

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, train_size=0.8, test_size=0.2, random_state=6
)

# Fit and Predict on test data
mlr = LinearRegression()
model = mlr.fit(x_train, y_train)
y_predict = mlr.predict(x_test)

# Calculate mse for train and test data
# Predicting on the training data
y_train_predict = mlr.predict(x_train)

# Calculate MSE for the training data
train_mse = mean_squared_error(y_train, y_train_predict)

# Calculate MSE for the test data
test_mse = mean_squared_error(y_test, y_predict)

print("Train MSE:", train_mse)
print("Test MSE:", test_mse)

# Calculate R^2 for the training data
train_score = mlr.score(x_train, y_train)

# Calculate R^2 for the test data
test_score = mlr.score(x_test, y_test)

print("Train R^2 Score:", train_score)
print("Test R^2 Score:", test_score)
