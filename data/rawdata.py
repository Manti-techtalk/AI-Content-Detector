import pandas as pd
import matplotlib.pyplot as plt


#load the data

df = pd.read_csv("data/AI_Human.csv")
for i in df.columns:
    print(i)
print(df.head(n = 10))

# check for null values and duplicates

print(df.isnull().sum())
print(df.duplicated().sum())

# check the data types of the columns
print(df.dtypes)

#save the data
df.to_csv('cleaned.csv', index=False)