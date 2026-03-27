import tkinter as tk

root = tk.Tk()
root.title("Form con Grid")

root.geometry("400x250")

root.configure(bg="#2c3e50")


# Etichette — colonna 0
tk.Label(root, text = "Inserisci il nome").grid(row=0, column=0, sticky="e", padx=20, pady=8)
tk.Label(root, text = "Inserisci il cognome").grid(row=1, column=0, sticky="e", padx=20, pady=8)#sticky="e" allinea a destra
tk.Label(root, text="Inserisci  l'email:").grid(row=2, column=0, sticky="e", padx=20, pady=8) #allinea a sinistra con sticky="w"
tk.Label(root, text="inserisci l'età:").grid(row=3, column=0,  sticky="e", padx=20, pady=8) #allinea sopra con sticky="n", allinea sotto con sticky="s"

# Entry — colonna 1
nome  = tk.Entry(root, width=35)
cognome = tk.Entry(root, width=35)
email = tk.Entry(root, width=35)
eta   = tk.Entry(root, width=35)


nome.grid(row=0, column=1, pady=8)
cognome.grid(row=1, column=1, pady=8)
email.grid(row=2, column=1, pady=8)
eta.grid(row=3,  column=1, pady=8)

def leggi_testo():
    print(f"Nome: {nome.get()}, Cognome: {cognome.get()}, Email: {email.get()}, Età: {eta.get()}")
    nome.delete(0, tk.END)
    cognome.delete(0, tk.END)
    email.delete(0, tk.END)
    eta.delete(0, tk.END)

# Bottone su 2 colonne
tk.Button(root, text="Invia", command=leggi_testo).grid(row=4, column=0, columnspan=2, pady=12)

root.mainloop()