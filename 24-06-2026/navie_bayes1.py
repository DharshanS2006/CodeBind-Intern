from sklearn.naive_bayes import GaussianNB
import numpy as np

n = int(input("Enter number of samples: "))

X = []
y = []

for i in range(n):
    feature = float(input(f"Enter feature {i+1}: "))
    label = int(input("Enter class: "))
    X.append([feature])
    y.append(label)

model = GaussianNB()
model.fit(np.array(X), np.array(y))

test = float(input("Enter test feature: "))
prediction = model.predict(np.array([[test]]))

print("Predicted Class =", prediction[0])