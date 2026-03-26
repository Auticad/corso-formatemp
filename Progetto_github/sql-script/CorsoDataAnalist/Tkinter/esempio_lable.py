import tkinter as tk

from numpy import pad

root = tk.Tk()

root.title("Hello Word")

root.geometry("500x350")

label = tk.Label(
    root, 
    text="Hello Word",
    background="red",
    foreground="blue",
    padx=10,
    pady=10,
    font=("Arial", 30, 'italic'),
    justify="center"
    )

label.pack()


root.mainloop()








root.title("la mia prima app")