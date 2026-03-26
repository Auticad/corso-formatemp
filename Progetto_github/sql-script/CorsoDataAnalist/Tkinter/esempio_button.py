import tkinter as tk
#import Models.GestioneWiget as saluta

def saluta():
     print("ciao")

root = tk.Tk()
root.title("Button")

root.geometry("500x350")

button = tk.Button(
    root, 
    text="Click me",
    command = saluta,
    bg = "red",
    fg = "white",
    activebackground="blue",
    activeforeground="black",
    cursor="hand2",   # Cambia il cursore del mouse in maniera dinamica
    padx=10,
    pady=10
    )

button.pack()

root.mainloop()