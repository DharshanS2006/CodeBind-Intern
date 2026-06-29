import pandas as pd

student_age = pd.Series(
    [20, 19, 18, 22],
    index=["John", "Alice", "Bob", "Emma"]
)

print(student_age)