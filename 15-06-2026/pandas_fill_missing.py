import pandas as pd

df = pd.read_csv(r"C:\Users\VUPIND\Downloads\organizations-100.csv")

df.fillna(0,inplace=True)

print(df)