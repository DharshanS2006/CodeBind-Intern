from sklearn.ensemble import RandomForestClassifier

n = int(input("Enter number of samples: "))

X = []
y = []

for i in range(n):
    feature = float(input(f"Enter feature {i+1}: "))
    label = int(input("Enter class: "))
    X.append([feature])
    y.append(label)

model = RandomForestClassifier(n_estimators=10)
model.fit(X, y)

test = float(input("Enter test feature: "))
prediction = model.predict([[test]])

print("Predicted Class =", prediction[0])