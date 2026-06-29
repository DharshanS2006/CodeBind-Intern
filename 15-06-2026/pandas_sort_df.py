import pandas as pd

data = {
    "Name":["Arun","Bala","Charan"],
    "Age":[20,18,19]
}

df = pd.DataFrame(data)

print(df.sort_values("Age"))