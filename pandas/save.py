import pandas as pd

data= {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 22, 35],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df=pd.DataFrame(data)
print(df)
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)
