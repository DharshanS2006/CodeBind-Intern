from sklearn.tree import DecisionTreeClassifier

n = int(input("Enter number of samples: "))

X = []
y = []

for i in range(n):
    feature = float(input(f"Enter feature {i+1}: "))
    label = int(input("Enter class: "))
    X.append([feature])
    y.append(label)

model = DecisionTreeClassifier()
model.fit(X, y)

test = float(input("Enter test feature: "))
prediction = model.predict([[test]])

print("Predicted Class =", prediction[0])