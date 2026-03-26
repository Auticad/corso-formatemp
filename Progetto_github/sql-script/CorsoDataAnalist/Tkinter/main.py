# main.py
import tkinter as tk
from tkinter import messagebox

# Importiamo la classe dalla cartella Models
from Models.saluto import Salutatore


def on_button_click():
    """Funzione chiamata quando si preme il bottone"""
    # Creiamo un'istanza della classe
    salutatore = Salutatore()
    
    # Chiamiamo il metodo saluta
    messaggio = salutatore.saluta("Utente")
    
    # Mostriamo il messaggio in una finestra popup
    messagebox.showinfo("Saluto dalla classe", messaggio)


# ====================== INTERFACCIA TKINTER ======================
root = tk.Tk()
root.title("Progetto Base Tkinter + Models")
root.geometry("400x200")
root.resizable(False, False)

# Label di titolo
label = tk.Label(root, 
                 text="Premi il pulsante per chiamare\nil metodo saluta() della classe",
                 font=("Arial", 12))
label.pack(pady=20)

# Bottone
btn = tk.Button(root, 
                text="✨ Saluta ✨", 
                font=("Arial", 14, "bold"),
                bg="#4CAF50",
                fg="white",
                width=20,
                height=2,
                command=on_button_click)
btn.pack(pady=10)

# Avvio dell'applicazione
root.mainloop()