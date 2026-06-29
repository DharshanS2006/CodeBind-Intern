import pandas as pd

data = {
    "Name":["Arun"],
    "Age":[18],
    "Marks":[90]
}

df = pd.DataFrame(data)

df.drop("Marks",axis=1,inplace=True)

print(df)