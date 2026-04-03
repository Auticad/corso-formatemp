from tkinter import HORIZONTAL, Button, Label, Scale, Tk

root = Tk()
root.title("Slider Demo")
root.geometry("400x400")
root.resizable(False, False)

#imposta percorso assoluto dell'icona
root.iconbitmap("G:\AMBIENTE_VIRTUALE_PYTHON\FLASK\Corso Formatemp\Progetto_github\sql-script\CorsoDataAnalist\Tkinter\Progetto_AI\icons\image.ico")

my_label = Label(root, text="Slider verticale")
my_label.pack()

verticale = Scale(root, from_=0, to=200)
verticale.pack()

my_label = Label(
    root, 
    text= "Slider orizzontale"
    )
my_label.pack()

orizzontale = Scale(root, from_=0, to=400, orient=HORIZONTAL)
orizzontale.pack()

def slider():
    my_label = Label(
        root, 
        text= orizzontale.get() 
        )
    my_label.pack()
    root.geometry(str(orizzontale.get()) + "x350")
    
btn_salva = Button(root, text="Salva", command=slider).pack(padx=10, pady=20)

root.mainloop()

