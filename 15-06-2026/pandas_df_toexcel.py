import pandas as pd

data = {
    "Name":["Arun","Bala"],
    "Age":[18,19]
}

df = pd.DataFrame(data)

df.to_excel("student.xlsx",index=False)

print("Excel file created")