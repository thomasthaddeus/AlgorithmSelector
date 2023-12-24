import numpy as np

class LinearRegression:
    def __init__(self):
        self.coefficients = None
        self.intercept = None

    def fit(self, X, y):
        """Fit the linear regression model to the training data."""
        if len(X.shape) == 1:
            X = X.reshape(-1, 1)
        X = np.insert(X, 0, 1, axis=1)  # Adding a column of ones for intercept
        X_transpose = np.transpose(X)
        self.coefficients = np.linalg.inv(X_transpose.dot(X)).dot(X_transpose).dot(y)
        self.intercept = self.coefficients[0]
        self.coefficients = self.coefficients[1:]

    def predict(self, X):
        """Make predictions using the linear regression model."""
        if len(X.shape) == 1:
            X = X.reshape(-1, 1)
        return np.dot(X, self.coefficients) + self.intercept

# Example usage
X = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 2, 4, 6, 8, 10])  # Example data

model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X)

print("Coefficients:", model.coefficients)
print("Intercept:", model.intercept)
print("Predictions:", predictions)
