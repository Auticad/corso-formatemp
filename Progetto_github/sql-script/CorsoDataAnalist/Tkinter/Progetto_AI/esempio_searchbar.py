import tkinter as tk
from tkinter import ttk


class SearchBar(ttk.Frame):
    """
    Barra di ricerca con callback on_search(str) chiamato
    alla pressione di Invio o del pulsante Cerca.
    """
    def __init__(self, parent, on_search, placeholder="Cerca…", **kwargs):
        super().__init__(parent, **kwargs)
        self._callback = on_search
        self._var = tk.StringVar()

        entry = ttk.Entry(self, textvariable=self._var, width=30)
        entry.pack(side="left", padx=(0, 6))
        entry.bind("<Return>", lambda e: self._fire())

        # Placeholder manuale (tkinter non lo supporta nativamente)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>",
            lambda e: entry.delete(0, "end") if entry.get() == placeholder else None)

        ttk.Button(self, text="Cerca", command=self._fire).pack(side="left")

    def _fire(self):
        self._callback(self._var.get().strip())
        
root = tk.Tk()
root.title("Esempio SearchBar")
root.geometry("300x200")
root.config(bg="#CEA1A1")

search_bar = SearchBar(root, on_search=lambda query: print(f"Ricerca per: {query}"))
search_bar.pack(pady=20)    

root.mainloop()