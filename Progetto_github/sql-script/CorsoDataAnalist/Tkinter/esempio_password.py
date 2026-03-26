import tkinter as tk


root = tk.Tk()
root.title("Password")

root.geometry("500x350")

root.configure(bg="#2c3e50")  # Sfondo del pack grigio bluastro scuro 

label_nom = tk.Label(root, text="Inserisci la password: ").pack(padx=10, pady=10)

nome_password = tk.StringVar()
entry = tk.Entry(root, width=30, textvariable=nome_password, show="*", font=("Arial", 20), justify="center")
entry.pack(padx=10, pady=10)
entry.focus_set() # Imposta il focus sul widget

entry.insert(0, "Inserisci qui")

def leggi_testo():
    test = entry.get()
    print(f"La password inserita è: {test}")
    
def svuota():
    entry.delete(0, tk.END)

tk.Button(root, text="Leggi il testo", command=leggi_testo).pack(padx=10, pady=20)

tk.Button(root, text="Svuota", command=svuota).pack(padx=10, pady=20)

root.mainloop()





root.mainloop()