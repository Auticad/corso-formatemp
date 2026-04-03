
import ttkbootstrap as ttk

#from ttkbootstrap.constants import *
# Importa solo quelle che ti servono
#from ttkbootstrap.constants import PRIMARY, SUCCESS, DARK, LIGHT, TABLE, STRIPED
from ttkbootstrap.constants import SUCCESS
from ttkbootstrap.tableview import Tableview

my_w = ttk.Window(themename="superhero")
my_w.geometry("500x500")
my_w.title("Esempio ttkbootstrap")

my_w.columnconfigure(0, weight=1)
my_w.rowconfigure(3, weight=1)  # solo la tabella si espande

colors = my_w.style.colors
print(colors.dark)

label =ttk.Label(my_w, text="Ciao, benvenuto in ttkbootstrap!", font=("Arial", 16), bootstyle=SUCCESS)
label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")
label =ttk.Label(my_w, text="Inserisci il tuo nome cognome altezza e genere", font=("Arial", 16), bootstyle=SUCCESS)
label.grid(row=1, column=0, padx=10, pady=(10, 5), sticky="ew")

entry = ttk.Entry(my_w, bootstyle=SUCCESS)
entry.grid(row=2, column=0, padx=10, pady=(5, 10), sticky="ew")



#bottone per inserire il testo dell'entry nella tabella
def inserisci_nella_tabella():
    testo = entry.get().split()  # es: "Luca Five 85 Maschio"
    
    if len(testo) >= 4:  # servono almeno 4 campi (nome, class, altezza, genere)
        
        nuovo_id = len(r_set) + 1
        nuova_riga = [nuovo_id, testo[0], testo[1], testo[2], testo[3]]
        
        r_set.append(nuova_riga)
          
        dv.build_table_data(coldata=li, rowdata=r_set)
        dv.autofit_columns()
        
        entry.delete(0, 'end')  # pulisce l'entry dopo l'inserimento
    else:
        print("Inserisci almeno 4 valori: nome class altezza genere")


button = ttk.Button(my_w, text="Inserisci", bootstyle=SUCCESS, command=inserisci_nella_tabella)
button.grid(row=4, column=0, padx=10, pady=(10, 5), sticky="ew")


li = [ # lista di dizionari per definire le colonne
    {"text": "id",      "stretch": False},  # stretch: se True, la colonna si espande per occupare lo spazio disponibile
    {"text": "nome",    "stretch": False},  
    {"text": "class",   "stretch": False}, 
    {"text": "Altezza", "stretch": False},  
    {"text": "Genere",  "stretch": False}
]

r_set = [
    (1, "Mario", 'Four', 90, "Maschio"),
    (2, "Luigi", 'Five', 80, "Maschio"),
    (3, "Peach", 'Six',  85, "Femmina"),
    (4, "Bowser", 'Seven', 70, "Maschio"),
    (5, "Donkey Kong", 'Eight', 75, "Maschio"),
    (6, "Yoshi", 'Nine', 80, "Maschio")
    
]


dv = Tableview(
    master=my_w, 
    coldata=li, # lista di dizionari
    rowdata=r_set, #
    paginated=True, 
    searchable=True, # abilita la ricerca nella tabella
    bootstyle=SUCCESS, # stile del widget
    pagesize=10, # numero di righe per pagina
    stripecolor=colors.light   # colore delle righe alternate 
)

dv.grid(row=5, column=0, padx=10, pady=(10, 5), sticky="ew") #sticky: espande il widget in entrambe le direzioni

dv.autofit_columns() # adatta la larghezza delle colonne al contenuto

my_w.mainloop()