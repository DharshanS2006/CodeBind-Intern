import pandas as pd

data = {
    "Name":["Arun","Bala","Charan"],
    "Age":[18,19,20]
}

df = pd.DataFrame(data)

print(df[df["Age"]>18])