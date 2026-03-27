import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Modulo Scolastico")
root.configure(bg="#e5e7eb")
root.geometry("700x300")


def set_placeholder(entry, testo):
    # Inserisce il placeholder e colora di grigio
    entry.insert(0, testo)
    entry.config(fg="gray")

    def on_focus_in(event):
        # Cancella il placeholder al primo click
        if entry.get() == testo:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(event):
        # Rimette il placeholder se il campo è vuoto
        if entry.get() == "":
            entry.insert(0, testo)
            entry.config(fg="gray")

    entry.bind("<FocusIn>",  on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


def crea_campo(testo, placeholder, riga, colonna):
    label = tk.Label(root, text=testo, bg="#e5e7eb", font=("Arial", 11))
    label.grid(row=riga, column=colonna, sticky="w", padx=20, pady=(10, 2))

    entry = tk.Entry(
        root,
        font=("Arial", 12),
        bg="#cbd5e1",
        relief="flat",
        width=25
    )
    entry.grid(row=riga+1, column=colonna, padx=20, pady=(0, 10), ipady=8)
    set_placeholder(entry, placeholder)
    return entry


# Campi
nome    = crea_campo("Nome",            "Inserisci il Nome",           0, 0)
cognome = crea_campo("Cognome",         "Inserisci il Cognome",        0, 1)
email   = crea_campo("Email",           "Inserisci la mail",           2, 0)
data    = crea_campo("Data di Nascita", "Inserisci la data di nascita",2, 1)


def salva_dati():
    campi = [nome, cognome, email, data]
    valori = []

    for campo in campi:
        testo = campo.get()
        # Se il colore è grigio il campo contiene ancora il placeholder
        if campo.cget("fg") == "gray":
            testo = ""
        valori.append(testo)

    # Costruisce il messaggio DOPO il ciclo (no virgole = no tupla)
    messaggio = (
        f"Nome: {valori[0]}\n"
        f"Cognome: {valori[1]}\n"
        f"Email: {valori[2]}\n"
        f"Data di nascita: {valori[3]}"
    )

    # Mostra il popup UNA SOLA VOLTA
    messagebox.showinfo("Dati inseriti", messaggio)


btn = tk.Button(
    root,
    text="Salva",
    bg="#94a3b8",
    font=("Arial", 11),
    command=salva_dati,
    width=20,
    height=2
)
btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20, sticky="w")

root.mainloop()