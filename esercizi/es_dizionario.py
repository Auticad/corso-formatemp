# %%


"""
| Funzione   | Serve per           |
| ---------- | ------------------- |
| len()    | contare elementi    |
| append() | aggiungere elemento |
| remove() | eliminare elemento  |
| sort()   | ordinare lista      |
| keys()   | chiavi dictionary   |
| values() | valori dictionary   |
| items()  | chiave + valore     |
| get()    | leggere valore      |
| count()  | contare valore      |
| index()  | trovare posizione   |

"""
#studente = {"chiave" : "valore"}

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

#print(stato)

# for chiave, valore in stato.items():
#     print(f"La capitale della regione {chiave} è {valore}")
    
    
# print("------------------------------")


# stato["Toscana"] = "Bergamo"


# print(stato["Toscana"])

# for chiave, valore in stato.items():
#     print(f"La capitale della regione {chiave} è {valore}")
    

# print("------------------------------")

# print(stato.keys())

# print("------------------------------")

# print(stato.values())

# print("------------------------------")

#chiedere di inserire una regine e restituire la capitale corrispondente se non esiste restituire un messaggio di errore
# regione = input("Inserisci il nome della regione: ")

# capitale = stato.get(regione, "La regione inserita non esiste")

# print(f"La capitale della regione {regione} è {capitale}")


stato.update({"Sicilia" : "Catanzaro"})
    
    
for chiave, valore in stato.items():
    print(f"La capitale della regione {chiave} è {valore}")
    
    
    

# %%
