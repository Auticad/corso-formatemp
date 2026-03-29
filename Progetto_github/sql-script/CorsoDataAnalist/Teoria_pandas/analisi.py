import ast

import pandas as pd


def calcola_media(valori: list) -> float:
    if not valori:
        raise ValueError("Lista vuota — impossibile calcolare la media.")
    return sum(valori) / len(valori)

def processa_dataset(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df['media'] = df['numeri'].apply(
        lambda row: calcola_media(ast.literal_eval(row))  # ← parse stringa → lista
    )
    return df

if __name__ == "__main__":
    risultato = processa_dataset(r"G:\AMBIENTE_VIRTUALE_PYTHON\FLASK\Corso Formatemp\Progetto_github\sql-script\CorsoDataAnalist\Teoria_pandas\dati.csv")
    print(risultato.head())
    
    