import pandas as pd

df = pd.read_csv("studenti.csv")

print(df)

print("_________Stampare le prime 5 righe.________________")
print(df.head())

print("_________Stampare solo la colonna nome.________________")
print(df["nome"])

print("_________Mostrare solo gli studenti con voto maggiore di 27.________________")
print(df[df["voto"] > 27])

print("________Calcolare la media dei voti._________________")
print(df["voto"].mean())

print("________Mostrare solo gli studenti del corso Python._________________")
print(df[df["corso"] == "Python"])

print("________Trovare il voto massimo_________________")

max_voto = df.groupby("nome")["voto"].max().sort_value(ascinding=False).reset_index()
print(max_voto)

print("_________________________")
