import tkinter as tk

root = tk.Tk()
root.title("Check_box")

label_nom = tk.Label(root, text="Seleziona un software: ").pack(padx=10, pady=10)

root.geometry("400x350")

root.configure(bg="#504c2c")

scelta = tk.BooleanVar()
valoreScelta = tk.Checkbutton(
    root, 
    text="accedi ai termini", 
    variable=scelta
    ).pack(padx=10, pady=10)

radioB = tk.StringVar(value="Python")  # Imposta Python come valore predefinito

# tk.Radiobutton(root, text="Python", variable=variabile_radio, value="Python").pack()
# tk.Radiobutton(root, text="C++", variable=variabile_radio, value="C++").pack()  
# tk.Radiobutton(root, text="Java", variable=variabile_radio, value="Java").pack()
# tk.Radiobutton(root, text="C#", variable=variabile_radio, value="C#").pack()
# tk.Radiobutton(root, text="JavaScript", variable=variabile_radio, value="JavaScript").pack()
# tk.Radiobutton(root, text="HTML", variable=variabile_radio, value="HTML").pack()

software = (
    "Python",
    "C++",
    "Java",
    "C#",
    "JavaScript",
    "HTML"
    )

for s in software:
    tk.Radiobutton(
        root, 
        text=s, 
        variable = radioB, 
        value=s,
        width=10, anchor="w",
        bg="#504c2c"
        ).pack( ) #anchor=tk.W per allineare a sinistra, lanchor=tk.E per allineare a destra, anchor=tk.CENTER per allineare al centro

def mostra():
    print(scelta.get())
    print(radioB.get())

tk.Button(
    root, 
    text="Mostra selezione", 
    command=mostra).pack(padx=10, pady=10)


root.mainloop()