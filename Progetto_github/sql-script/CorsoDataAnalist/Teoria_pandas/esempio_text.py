import tkinter as tk


class text_widget: 
    def __init__(self, root):
        self.root = root
        self.root.title("Struttura base")

        self.root.geometry("500x350")

        self.txt = tk.Text(self.root, width=30, height=10, font=("Arial", 12))
        self.txt.pack()

         # Inserisci testo iniziale anche tk.INSERT?????
        self.txt.insert("1.0", "Prima riga\nSeconda riga\n") # tk.END o "end" indica di apperire il testo dopo l'ultimo carattere esistente.

        # Bottone per leggere tutto il contenuto
        self.btn_leggi = tk.Button(self.root, text="Leggi contenuto", command=self.leggi_contenuto)
        self.btn_leggi.pack(pady=5)

        # Bottone per cancellare tutto
        self.btn_cancella = tk.Button(self.root, text="Cancella tutto", command=self.cancella_testo)
        self.btn_cancella.pack(pady=5)

        # Bottone per rendere il Text di sola lettura
        self.btn_readonly = tk.Button(self.root, text="Sola lettura", command=self.sola_lettura)
        self.btn_readonly.pack(pady=5)

    def leggi_contenuto(self):
        riga1 = self.txt.get("1.0", "1.end") # fine riga siscrive 1.end
        print("Riga1:")
        print(riga1)

        # Leggi una riga specifica (riga 2)
        riga2 = self.txt.get("2.0", "2.end") # fine riga siscrive 2.end
        print("Riga 2:")
        print(riga2)



    def cancella_testo(self):
        # Se il Text è disabilitato, abilitalo temporaneamente
        self.txt.config(state=tk.NORMAL)
        self.txt.delete("1.0", tk.END)
        # Se vuoi, puoi rimetterlo in sola lettura qui
        # self.txt.config(state=tk.DISABLED)

    def sola_lettura(self):
        self.txt.config(state=tk.DISABLED)
        
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("TEXT_WIDGET")

    text_widget(root)


    root.mainloop()
