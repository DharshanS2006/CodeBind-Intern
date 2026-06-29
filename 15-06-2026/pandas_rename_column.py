import pandas as pd

df = pd.DataFrame({"Name":["Arun"]})

df.rename(columns={"Name":"Student_Name"},inplace=True)

print(df)