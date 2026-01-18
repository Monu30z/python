import pandas as pd

df = pd.read_csv("data.csv")
# print(df.head())

# print(df[['Name','Sex','Age']])

# print(df.iloc[: , : 2])

print(df[df['Age']<=25 ])
