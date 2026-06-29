import pandas as pd

data = {
    "Name":["Arun","Bala"],
    "Age":[18,19]
}

df = pd.DataFrame(data)

df["Marks"]=[85,90]

print(df)