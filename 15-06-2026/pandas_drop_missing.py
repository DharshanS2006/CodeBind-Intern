import pandas as pd

df = pd.read_csv(r"C:\Users\VUPIND\Downloads\organizations-100.csv")

df.dropna(inplace=True)

print(df)