# -----------------------
# IMPORT LIBRERIE
# -----------------------
import ttkbootstrap as ttk  # tkinter moderno

#from ttkbootstrap.constants import *  # stili (SUCCESS, INFO, ecc.)
from ttkbootstrap.constants import SUCCESS
from ttkbootstrap.tableview import Tableview as tb  # tabella avanzata

# -----------------------
# FINESTRA PRINCIPALE
# -----------------------
my_w = ttk.Window(themename="flatly")  # tema moderno
my_w.geometry("600x600")  # dimensione finestra
my_w.title("Gestione Studenti")  # titolo finestra

colors = my_w.style.colors  # colori del tema

# -----------------------
# VARIABILI (collegate ai campi input)
# -----------------------
id_var = ttk.StringVar()
nome_var = ttk.StringVar()
classe_var = ttk.StringVar()
altezza_var = ttk.StringVar(value="1.50")  # valore iniziale
genere_var = ttk.StringVar()

# -----------------------
# FUNZIONE AGGIUNTA DATI
# -----------------------
def aggiungi_dati():
    """
    Questa funzione:
    1. Legge i dati dagli input
    2. Li inserisce nella tabella
    3. Pulisce i campi
    """
    try:
        # converte altezza in numero float (decimale)
        altezza = float(altezza_var.get())

        # crea una tupla con tutti i dati
        dati = (
            id_var.get(),
            nome_var.get(),
            classe_var.get(),
            altezza,
            genere_var.get()
        )

        # inserisce una nuova riga nella tabella
        dv.insert_row(values=dati)

        # aggiorna la tabella
        dv.load_table_data()

        # pulisce i campi input
        id_var.set("")
        nome_var.set("")
        classe_var.set("")
        altezza_var.set("1.50")  # reset valore default
        genere_var.set("")

    except ValueError:
        # errore se altezza non è numero
        ttk.dialogs.Messagebox.show_error(
            "Inserisci un numero valido per l'altezza!",
            title="Errore"
        )

# -----------------------
# TITOLO + DESCRIZIONE
# -----------------------
ttk.Label(
    my_w,
    text="Gestione Studenti",
    font=("Segoe UI", 18, "bold"),
    bootstyle="primary"
).pack(pady=(10, 5))

ttk.Label(
    my_w,
    text="Inserisci i dati e premi il bottone per aggiungerli alla tabella.\n"
         "Altezza usa uno Spinbox (⬆️⬇️) e Genere una Combobox.",
    justify="center",
    bootstyle="secondary"
).pack(pady=(0, 15))

# -----------------------
# FRAME INPUT
# -----------------------
frame = ttk.Frame(my_w, padding=10)
frame.pack(fill="x", padx=20)

# -----------------------
# ID (sopra)
# -----------------------
ttk.Label(frame, text="ID").grid(row=0, column=0, sticky="w")

ttk.Entry(
    frame,
    textvariable=id_var,
    bootstyle="info"
).grid(row=1, column=0, columnspan=2, sticky="ew", pady=5)

# -----------------------
# RIGA 1 → Nome e Classe
# -----------------------
ttk.Label(frame, text="Nome").grid(row=2, column=0, sticky="w")
ttk.Label(frame, text="Classe").grid(row=2, column=1, sticky="w")

ttk.Entry(frame, textvariable=nome_var, bootstyle="info").grid(row=3, column=0, padx=5, pady=5, sticky="ew")
ttk.Entry(frame, textvariable=classe_var, bootstyle="info").grid(row=3, column=1, padx=5, pady=5, sticky="ew")

# -----------------------
# RIGA 2 → Altezza e Genere
# -----------------------
ttk.Label(frame, text="Altezza (m)").grid(row=4, column=0, sticky="w")
ttk.Label(frame, text="Genere").grid(row=4, column=1, sticky="w")

# 🔢 Spinbox (input numerico con ⬆️⬇️)
altezza_spin = ttk.Spinbox(
    frame,
    from_=0.50,          # valore minimo
    to=2.50,             # valore massimo
    increment=0.01,      # incremento decimale
    textvariable=altezza_var,
    format="%.2f",       # 2 cifre decimali
    bootstyle="info"
)
altezza_spin.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

# 👤 Combobox (menu a tendina)
genere_combo = ttk.Combobox(
    frame,
    textvariable=genere_var,
    values=["Maschio", "Femmina"],
    state="readonly",  # non scrivibile manualmente
    bootstyle="info"
)
genere_combo.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

# rende le colonne espandibili
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# -----------------------
# BOTTONE
# -----------------------
ttk.Button(
    my_w,
    text="Aggiungi alla Tabella",
    bootstyle=SUCCESS,
    command=aggiungi_dati
).pack(pady=15)

# -----------------------
# TABLEVIEW
# -----------------------
colonne = [
    {"text": "ID", "stretch": False},
    {"text": "Nome", "stretch": True},
    "Classe",
    {"text": "Altezza"},
    {"text": "Genere"}
]

dati_iniziali = [
    (1, "Alessio", "Four", 1.90, "Maschio"),
    (2, "Rosanna", "Five", 1.80, "Femmina"),
    (3, "Pablo", 'Four', 1.70, "Masschio"), 
    (4, "Moussa", 'Four', 1.83, "Maschio"), 
    (5, "Mirabelle", 'Fiv', 1.80, "Femmina"), 
    (6, "Paolo", 'Four', 1.70, "Masschio")
]

# creazione tabella
dv = tb(
    master=my_w,
    coldata=colonne,
    rowdata=dati_iniziali,
    paginated=True,        # pagine automatiche
    searchable=True,       # barra ricerca
    bootstyle=SUCCESS,     # colore
    pagesize=5,            # righe per pagina
    stripecolor=(colors.light, None)  # righe alternate
)

dv.pack(fill="both", expand=True, padx=20, pady=10)

# adatta colonne al contenuto
dv.autofit_columns()

# -----------------------
# AVVIO APP
# -----------------------
my_w.mainloop()