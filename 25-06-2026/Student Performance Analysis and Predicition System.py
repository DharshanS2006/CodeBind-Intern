#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Object - Oriented Programming
#Class Creation
class Student:
    #Constructor
    def __init__(self, name, hours_studied, attendance, marks):
        self.name = name
        self.hours_studied = hours_studied
        self.attendance = attendance
        self.marks = marks

    #Display Method
    def display(self):
        print(f"Name: {self.name}")
        print(f"Hours Studied: {self.hours_studied}")
        print(f"Attendance: {self.attendance}%")
        print(f"Marks: {self.marks}")

    #File Handling + Exception Handling
try:
    df = pd.read_csv("students.csv")
    print("Dataset Loaded Successfully!")

except FileNotFoundError:
    print("students.csv not found!")
    print("Creating sample dataset...\n")

    #Sample dataset creation
    data = {
        "Hours_Studied": [2, 3, 4, 5, 6],
        "Attendance": [70, 75, 80, 85, 90],
        "Marks": [45, 50, 60, 70, 80]
    }

    #Convert to DataFrame
    df = pd.DataFrame(data)
        
    #Save dataset
    df.to_csv("studens.csv", index=False)

    #Print the dataset
    print("Sample dataset created!\n")

    #Pandas Operations
    print("Dataset")
    print(df)
    print("\nDataset Information", df.info())
    print("\nDataset Statistical Summary", df.describe())
    
    #Numpy Analysis
    
    #Average Marks
    avg_marks = np.mean(df["Marks"])

    #Maximum Marks
    max_marks = np.max(df["Marks"])

    #Minimum Marks
    min_marks = np.min(df["Marks"])

    print("\nNumPy Analysis")
    print("Average Marks:", avg_marks)
    print("Maximum Marks:", max_marks)
    print("Minimum Marks:", min_marks)

    #Object Creation 
    student1 = Student("Karthik", 5, 85, 70)

    print("\nStudent Details")
    #Calling method
    student1.display()

#Data Visualization using Matplotlib

# Scatter Plot
plt.scatter(df["Hours_Studied"], df["Marks"]) 

# Chart Lables
plt.title("Hours Studied vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()

#Machine Learning Section

#Feature Selection
X = df[["Hours_Studied", "Attendance"]]

#Target Variable
y = df["Marks"]

#Create Linear Regression Model
model = LinearRegression()

#Train the model
model.fit(X, y)

#Prediction
new_data = pd.DataFrame({ "Hours_Studied":[7], "Attendance":[95]})
prediction = model.predict(new_data)

print("Machine Learning Prediction")
print("Predicted Marks:", round(prediction[0], 2))