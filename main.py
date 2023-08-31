# Importing the required libraries
from re import X
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from new_func import new_func

# Load the dataset
data = pd.read_csv('marketing_dataset.csv')

X_train, X_test, y_train, y_test = train_test_split(X, new_func(), test_size=0.2, random_state=42)

# Building the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Making predictions on the test set
y_pred = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
