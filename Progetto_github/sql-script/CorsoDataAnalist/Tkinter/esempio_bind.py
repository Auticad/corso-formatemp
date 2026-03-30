import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Esempio Bind")
root.config(bg="#470707")
lbl = tk.Label(root, text="Interagisci!", font=("Arial", 14))
lbl.pack(pady=30, padx=30)

# Evento click sinistro del mouse
def al_click(event):
    lbl.config(text=f"Click su ({event.x}, {event.y})")

# Tasto premuto sulla tastiera
def al_tasto(event):
    lbl.config(text=f"Tasto: {event.keysym}")

# Mouse sopra il widget
def al_hover(event):
    lbl.config(bg="#dbeafe")

def al_leave(event):
    lbl.config(bg="SystemButtonFace")

root.bind("<Button-1>", al_click)   # click sinistro
root.bind("<Key>",      al_tasto)   # qualsiasi tasto
lbl.bind("<Enter>",   al_hover)   # mouse entra
lbl.bind("<Leave>",   al_leave)   # mouse esce

root.mainloop()