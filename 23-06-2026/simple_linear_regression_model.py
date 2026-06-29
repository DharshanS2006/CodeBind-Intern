# Simple Employee Salary Prediction using Linear Regression

import numpy as np
from sklearn.linear_model import LinearRegression

# x = years of experience
# y = employee salary
x = [[1], [2], [3], [4], [5]]
y = [25000, 30000, 35000, 40000, 45000]

# Create linear regression model
model = LinearRegression()

# Train the model
model.fit(x, y)

print("Employee Salary Prediction Model")
print("-" * 40)
print("Years of Experience =", x)
print("Employee Salaries =", y)
print()

# Predict salary for a new employee
user_experience = float(input("Enter employee years of experience: "))
experience = np.array([[user_experience]])
predicted_salary = model.predict(experience)

print("New Employee Experience =", experience[0][0], "years")
print("Predicted Salary =", predicted_salary[0])
