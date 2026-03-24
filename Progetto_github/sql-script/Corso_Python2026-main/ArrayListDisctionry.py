"""
    | Funzione   | Serve per           |
    | ---------- | ------------------- |
    | `len()`    | contare elementi    |
    | `append()` | aggiungere elemento |
    | `remove()` | eliminare elemento  |
    | `sort()`   | ordinare lista      |
    | `keys()`   | chiavi dictionary   |
    | `values()` | valori dictionary   |
    | `items()`  | chiave + valore     |
    | `get()`    | leggere valore      |
    | `count()`  | contare valore      |
    | `index()`  | trovare posizione   |
"""


stato = {"Lombardia" : "Milano", 
         "Lazio" : "Roma", 
         "Campania" : "Napoli", 
         "Piemonte" : "Torino",
         "Sicilia" : "Palermo",
         "Puglia" : "Bari",
         "Veneto" : "Venezia",
         "Marche" : "Ancona",
         "Toscana" : "Firenze",
         "Umbria" : "Perugia",
         "Liguria" : "Genova",
         "Emilia Romagna" : "Bologna",
         "Friuli Venezia Giulia" : "Trieste"}

for chiave, valore in stato.items():
    print(f"La capitale della regione {chiave} è {valore}")


print("________________Modifica del valore_______________________")


print("__________________________________________________________")

regione = input("Inserisci una regione: ")
capitale = stato.get(regione, "Regione non presente nel dizionario")
print("La capitale è:", capitale)

print("__________________________________________________________")
print("__________________________________________________________")
print("__________________________________________________________")
print("__________________________________________________________")
print("__________________________________________________________")
print("__________________________________________________________")
