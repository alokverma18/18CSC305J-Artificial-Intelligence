from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=42)

# Create Logistic Regression model
logistic_regression = LogisticRegression(max_iter=1000, random_state=42)

# Train Logistic Regression model
logistic_regression.fit(X_train, y_train)

# Predict using Logistic Regression model
y_pred = logistic_regression.predict(X_test)

# Calculate accuracy score
accuracy = accuracy_score(y_test, y_pred)

# Print accuracy score
print('Accuracy:', accuracy) 
