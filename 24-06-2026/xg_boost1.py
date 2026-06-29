from xgboost import XGBClassifier

n = int(input("Enter number of samples: "))

X = []
y = []

for i in range(n):
    feature = float(input(f"Enter feature {i+1}: "))
    label = int(input("Enter class (0/1): "))
    X.append([feature])
    y.append(label)

model = XGBClassifier(
    use_label_encoder=False,
    eval_metric='logloss'
)

model.fit(X, y)

test = float(input("Enter test feature: "))
prediction = model.predict([[test]])

print("Predicted Class =", prediction[0])