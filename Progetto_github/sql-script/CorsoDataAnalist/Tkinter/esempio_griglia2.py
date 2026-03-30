import tkinter as tk

root = tk.Tk()
root.title("Form con Grid")
root.geometry("300x250")
root.configure(bg="#2c3e50")

# ── Helper placeholder ────────────────────────────────────────
def add_placeholder(entry: tk.Entry, placeholder: str) -> None:
    """
    Associa un placeholder a un Entry.
    - FocusIn  → cancella il testo se è ancora il placeholder
    - FocusOut → rimette il placeholder se il campo è vuoto
    """
    entry.insert(0, placeholder)

    entry.bind("<FocusIn>",
        lambda e: entry.delete(0, tk.END) if entry.get() == placeholder else None)
    entry.bind("<FocusOut>",
        lambda e: entry.insert(0, placeholder) if entry.get() == "" else None)

# ── Etichette ─────────────────────────────────────────────────
tk.Label(root, text="Nome:" ).grid(row=0, column=0, sticky="e", padx=20, pady=8)
tk.Label(root, text="Email:").grid(row=1, column=0, sticky="e", padx=20, pady=8)
tk.Label(root, text="Età:"  ).grid(row=2, column=0, sticky="e", padx=20, pady=8)

# ── Entry con placeholder ─────────────────────────────────────
nome  = tk.Entry(root, width=35)
email = tk.Entry(root, width=35)
eta   = tk.Entry(root, width=35)

add_placeholder(nome,  "Inserisci il nome")
add_placeholder(email, "Inserisci l'email")
add_placeholder(eta,   "Inserisci l'età")

nome .grid(row=0, column=1, pady=8)
email.grid(row=1, column=1, pady=8)
eta  .grid(row=2, column=1, pady=8)

# ── Lettura dati ──────────────────────────────────────────────
PLACEHOLDERS = {
    "nome":  "Inserisci il nome",
    "email": "Inserisci l'email",
    "eta":   "Inserisci l'età",
}

def leggi_testo():
    n = nome.get()
    m = email.get()
    e = eta.get()

    # Ignora i campi ancora al placeholder
    if n == PLACEHOLDERS["nome"]:
        n = ""
    if m == PLACEHOLDERS["email"]:
        m = ""
    if e == PLACEHOLDERS["eta"]:
        e = ""

    print(f"Nome: {n} | Email: {m} | Età: {e}")
    
    nome.delete(0, tk.END)
    email.delete(0, tk.END)
    eta.delete(0, tk.END)

# ── Bottone ───────────────────────────────────────────────────
tk.Button(root, text="Invia", command=leggi_testo).grid(
    row=3, column=0, columnspan=2, pady=12)

root.mainloop()