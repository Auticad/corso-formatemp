import tkinter as tk

root = tk.Tk()
root.geometry("500x350")
root.title("Esempio Variabili")
root.config(bg="#0C883C")

tk.Label(root, text="Inserisci una frase", font=("Arial", 14), bg="#71880C", fg="white").pack(pady=10)
# StringVar collegata all'Entry
nome_var = tk.StringVar()
entry = tk.Entry(root, textvariable=nome_var)
entry.pack(pady=10)

# Label che mostra il valore automaticamente
lbl = tk.Label(root, textvariable=nome_var, fg="blue")
lbl.pack()

# Modificare la variabile da codice
def imposta():
    nome_var.set("Mario Rossi")  # aggiorna entry e label!

def leggi():
    print(nome_var.get())         # legge il valore
    
#frame = tk.Frame(root, bg="#0C883C") # 1. Creo un frame/container per i bottoni

# 2. Impacchetto il frame con expand=True
# Questo dice a pack di dare spazio extra attorno al frame, centrandolo
#frame.pack(expand=True) 


frame1 = tk.LabelFrame(root, bg="#F3F732", padx=10, pady=10)
frame1.pack(padx=20, pady=20)


# 3. Creo i bottoni DENTRO il container (non dentro root)
tasto1 = tk.Button(frame1, text="Imposta", command=imposta, bg="lightblue")
tasto2 = tk.Button(frame1, text="Leggi",   command=leggi, bg="lightgreen")


# 4. Affianco i bottoni dentro il container
tasto1.pack(side=tk.LEFT, padx=10, ipady=10) #ipady per aumentare l'altezza del bottone
tasto2.pack(side=tk.LEFT, padx=10, ipady=10)

#tk.Button(root, text="Imposta", command=imposta).pack(side=tk.LEFT, padx=10, pady=10) #left per affiancare i bottoni,c
#tk.Button(root, text="Leggi",   command=leggi).pack(side=tk.LEFT, padx=10, pady=10) #padding per distanziare i bottoni a sx 
root.mainloop()