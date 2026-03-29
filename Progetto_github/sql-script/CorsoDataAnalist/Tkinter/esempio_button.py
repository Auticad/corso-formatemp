import tkinter as tk
from tkinter import messagebox

from Models import Saluta

#import Models.GestioneWiget as saluta


def mostra_saluto():
    obj = Saluta("Pietro")
    messaggio = obj.messaggio()  # Chiamiamo il metodo messaggio di Saluta
    messagebox.showinfo("Saluto", messaggio)
    

root = tk.Tk()
root.title("Button")

root.geometry("500x350")

button = tk.Button(
    root, 
    text="Mostra saluto",
    command = mostra_saluto,
    bg = "red",
    fg = "white",
    activebackground="blue",
    activeforeground="black",
    cursor="hand2",   # Cambia il cursore del mouse in maniera dinamica
    padx=10,
    pady=10
    )

button.pack(expand=True)  # Espande il pulsante per riempire la finestra

root.mainloop()