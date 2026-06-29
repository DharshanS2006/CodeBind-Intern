# Simple Student Pass or Fail Prediction using Logistic Regression

import numpy as np
from sklearn.linear_model import LogisticRegression

# x = hours studied
# y = result, where 0 = fail and 1 = pass
x = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [0, 0, 0, 0, 1, 1, 1, 1]

# Create logistic regression model
model = LogisticRegression()

# Train the model
model.fit(x, y)

print("Student Pass or Fail Prediction Model")
print("-" * 45)
print("Hours Studied =", x)
print("Results =", y)
print()

# Predict result for a new student
user_hours = float(input("Enter student study hours: "))
hours_studied = [[user_hours]]
predicted_result = model.predict(hours_studied)
pass_probability = model.predict_proba(np.array(hours_studied))

print("New Student Study Hours =", hours_studied[0][0])

if predicted_result[0] == 1:
    print("Predicted Result = Pass")
else:
    print("Predicted Result = Fail")

