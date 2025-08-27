# head() tail()
# head()-->5 rows
# tail()-->last 5 rows

import pandas as pd
df=pd.read_csv("data.csv")
print(df.head(3))
print(df.tail(3))