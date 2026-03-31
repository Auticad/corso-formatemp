import tkinter as tk
from tkinter import ttk


class DataTable(ttk.Frame):
    """
    Tabella dati riutilizzabile.
    columns: lista di dict {"id", "header", "width" (opt), "anchor" (opt)}
    Esempio:
      [{"id": "nome", "header": "Nome", "width": 150},
       {"id": "val",  "header": "Valore", "width": 100, "anchor": "e"}]
    """
    def __init__(self, parent, columns: list[dict], **kwargs):
        super().__init__(parent, **kwargs)
        self._sort_state: dict[str, bool] = {}
        col_ids = [c["id"] for c in columns]

        self._tree = ttk.Treeview(self, columns=col_ids, show="headings")
        for col in columns:
            cid = col["id"]
            self._tree.heading(cid, text=col["header"],
                               command=lambda c=cid: self._sort(c))
            self._tree.column(cid, width=col.get("width", 120),
                              anchor=col.get("anchor", "w"))

        vsb = ttk.Scrollbar(self, orient="vertical",   command=self._tree.yview)
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self._tree.xview)
        self._tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        self._tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def load(self, rows: list[dict]) -> None:
        """Sostituisce i dati nella tabella."""
        self._tree.delete(*self._tree.get_children())
        for row in rows:
            values = [row.get(col) for col in self._tree["columns"]]
            self._tree.insert("", "end", values=values)

    def _sort(self, col: str) -> None:
        """Ordina la colonna cliccata, alternando crescente/decrescente."""
        reverse = self._sort_state.get(col, False)
        items = [(self._tree.set(k, col), k) for k in self._tree.get_children("")]
        try:
            items.sort(
                key=lambda t: float(t[0].replace(",", ".")), reverse=reverse)
        except ValueError:
            items.sort(key=lambda t: t[0].lower(), reverse=reverse)
        for idx, (_, k) in enumerate(items):
            self._tree.move(k, "", idx)
        self._sort_state[col] = not reverse
        
root = tk.Tk()
root.title("Esempio scrollable DataTable")    
root.geometry("300x200")
root.config(bg="#CEA1A1")    

data_table = DataTable(root, columns=[
    {"id": "nome", "header": "Nome", "width": 150},
    {"id": "val",  "header": "Valore", "width": 100, "anchor": "e"}         
    
])
data_table.pack(fill="both", expand=True, padx=10, pady=10)
data_table.load([   
    {"nome": "Mario", "val": 10},   
    {"nome": "Luigi", "val": 20},   
    {"nome": "Peach", "val": 15},   
    {"nome": "Bowser", "val": 5},   
    {"nome": "Donkey Kong", "val": 30},   
    {"nome": "Yoshi", "val": 25},   
    {"nome": "Toad", "val": 10},   
    {"nome": "Wario", "val": 20}
])

root.mainloop()