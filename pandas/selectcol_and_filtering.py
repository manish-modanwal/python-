import pandas as pd

data={
    "Name": ["Alice", "Bob", "Charlie", "David","ram","shyam","manish","mohan"],
    "Age": [24, 30, 22, 35,45,50,29,33],
    "Salary": [50000, 60000, 55000, 70000,80000,90000,75000,72000],
    "Performance Score": [8, 7, 9, 6,7,8,9,6]
}

df = pd.DataFrame(data)

print("People older than 30:")
print(df[df["Age"] > 30], "\n")

print("People with salary > 60000 AND performance >= 7:")
print(df[(df["Salary"] > 60000) & (df["Performance Score"] >= 7)])
