import pandas as pd

df1 = pd.DataFrame({
    "ID":[1,2],
    "Name":["Arun","Bala"]
})

df2 = pd.DataFrame({
    "ID":[1,2],
    "Marks":[85,90]
})

print(pd.merge(df1,df2,on="ID"))