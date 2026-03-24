import pandas as pd

df = pd.read_csv("studente.csv")

print(df.head())
df.head()
# print(df)

# print("------------------------------")

# print(df[df["voto"] > 27])

# print("------------------------------")

# print(df["voto"].mean())

# print("------------------------------")

# print(df["corso"] == "Python")

# print("------------------------------")

#print(df.tail())

# max_voto = df.groupby('nome')['voto'].max().sort_values(ascending=False).reset_index()
# print(max_voto)



