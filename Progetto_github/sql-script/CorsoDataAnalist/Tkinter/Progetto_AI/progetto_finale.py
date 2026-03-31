"""
dashboard.py
Dashboard KPI e Tabella Dati — tkinter + ttk + matplotlib
Dipendenze : pip install matplotlib
Python     : 3.9+
"""
import random
import tkinter as tk
from datetime import date
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ══════════════════════════════════════════════════════════════
#  DATA LAYER
#  Sostituire con query reali (pandas, sqlite3, pyodbc, ecc.)
# ══════════════════════════════════════════════════════════════

SAMPLE_DATA = [
    {
        "id":         f"{i:04d}",
        "prodotto":   f"Prodotto {chr(65 + i % 8)}",
        "categoria":  ["Nord", "Sud", "Est", "Ovest"][i % 4],
        "q":          random.randint(10, 500),
        "fatturato":  round(random.uniform(1000, 50000), 2),
        "margine_%":  round(random.uniform(5, 40), 1),
    }
    for i in range(60)
]

YEARS = ["2022", "2023", "2024"]


def _filter(year: str, search: str) -> list[dict]:
    s = search.lower()
    return [
        r for r in SAMPLE_DATA
        if not s or s in r["prodotto"].lower() or s in r["categoria"].lower()
    ]


def get_kpis(year: str, search: str = "") -> dict:
    rows   = _filter(year, search)
    total  = sum(r["fatturato"] for r in rows)
    orders = len(rows)
    margin = round(sum(r["margine_%"] for r in rows) / max(orders, 1), 1)
    cats   = len({r["categoria"] for r in rows})
    return {
        "Fatturato":    (f"€ {total:,.0f}", "+4.1%"),
        "Ordini":       (str(orders),        "-1.2%"),
        "Margine med.": (f"{margin} %",      "+0.8%"),
        "Categorie":    (str(cats),          "stabile"),
    }


def get_by_category(year: str, search: str = "") -> tuple[list, list]:
    rows = _filter(year, search)
    cats: dict[str, float] = {}
    for r in rows:
        cats[r["categoria"]] = cats.get(r["categoria"], 0) + r["fatturato"]
    items = sorted(cats.items(), key=lambda x: x[1], reverse=True)
    return [c[0] for c in items], [c[1] for c in items]


def get_monthly(year: str) -> list[float]:
    base = random.uniform(80_000, 120_000)
    return [round(base + random.gauss(0, 15_000), 2) for _ in range(12)]


def get_rows(year: str, search: str = "") -> list[dict]:
    return _filter(year, search)


# ══════════════════════════════════════════════════════════════
#  WIDGET LAYER
# ══════════════════════════════════════════════════════════════

class KPICard(ttk.Frame):
    def __init__(self, parent, title: str, value: str, delta: str, **kwargs):
        super().__init__(parent, padding=14, **kwargs)
        self.configure(style="Card.TFrame")
        ttk.Label(self, text=title.upper(), style="CardTitle.TLabel").pack(anchor="w")
        self._val_var = tk.StringVar(value=value)
        ttk.Label(self, textvariable=self._val_var,
                  style="CardValue.TLabel").pack(anchor="w")
        color = "#2e7d32" if delta.startswith("+") else (
                "#c62828" if delta.startswith("-") else "#555555")
        tk.Label(self, text=delta, fg=color, bg="#ffffff",
                 font=("Segoe UI", 9)).pack(anchor="w")

    def set(self, value: str) -> None:
        self._val_var.set(value)


class BarChart(ttk.Frame):
    def __init__(self, parent, title: str, **kwargs):
        super().__init__(parent, **kwargs)
        self._fig, self._ax = plt.subplots(figsize=(4.8, 3), dpi=96)
        self._fig.patch.set_facecolor("#f4f6f9")
        self._ax.set_facecolor("#f4f6f9")
        self._ax.set_title(title, fontsize=10, fontweight="bold", pad=6)
        self._canvas = FigureCanvasTkAgg(self._fig, master=self)
        self._canvas.get_tk_widget().pack(fill="both", expand=True)

    def update(self, labels: list, values: list) -> None:
        self._ax.clear()
        bars = self._ax.barh(labels, values, color="#1a56db", edgecolor="white")
        self._ax.spines[["top", "right", "left"]].set_visible(False)
        self._ax.tick_params(left=False, labelsize=8)
        for bar, val in zip(bars, values):
            self._ax.text(
                val + max(values) * 0.01,
                bar.get_y() + bar.get_height() / 2,
                f"€ {val:,.0f}", va="center", fontsize=7.5)
        self._fig.tight_layout()
        self._canvas.draw()

    def destroy(self):
        plt.close(self._fig)
        super().destroy()


class LineChart(ttk.Frame):
    def __init__(self, parent, title: str, **kwargs):
        super().__init__(parent, **kwargs)
        self._fig, self._ax = plt.subplots(figsize=(4.8, 3), dpi=96)
        self._fig.patch.set_facecolor("#f4f6f9")
        self._ax.set_facecolor("#f4f6f9")
        self._ax.set_title(title, fontsize=10, fontweight="bold", pad=6)
        self._canvas = FigureCanvasTkAgg(self._fig, master=self)
        self._canvas.get_tk_widget().pack(fill="both", expand=True)

    def update(self, values: list) -> None:
        months = ["Gen","Feb","Mar","Apr","Mag","Giu",
                  "Lug","Ago","Set","Ott","Nov","Dic"]
        self._ax.clear()
        self._ax.plot(months, values, color="#1a56db",
                      linewidth=2, marker="o", markersize=4)
        self._ax.fill_between(months, values, alpha=0.10, color="#1a56db")
        self._ax.spines[["top", "right"]].set_visible(False)
        self._ax.tick_params(labelsize=7.5)
        self._fig.tight_layout()
        self._canvas.draw()

    def destroy(self):
        plt.close(self._fig)
        super().destroy()


class DataTable(ttk.Frame):
    COLUMNS = [
        {"id": "id",        "header": "ID",        "width": 55},
        {"id": "prodotto",  "header": "Prodotto",  "width": 140},
        {"id": "categoria", "header": "Categoria", "width": 90},
        {"id": "q",         "header": "Q.tà",      "width": 60,  "anchor": "e"},
        {"id": "fatturato", "header": "Fatturato", "width": 110, "anchor": "e"},
        {"id": "margine_%", "header": "Margine %", "width": 90,  "anchor": "e"},
    ]

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self._sort_asc: dict[str, bool] = {}
        col_ids = [c["id"] for c in self.COLUMNS]

        self._tree = ttk.Treeview(self, columns=col_ids,
                                   show="headings", height=10)
        for col in self.COLUMNS:
            cid = col["id"]
            self._tree.heading(cid, text=col["header"],
                               command=lambda c=cid: self._sort(c))
            self._tree.column(cid, width=col.get("width", 100),
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
        self._tree.delete(*self._tree.get_children())
        for row in rows:
            vals = list(row.get(c["id"]) for c in self.COLUMNS)
            vals[4] = f"€ {vals[4]:,.2f}" if isinstance(vals[4], float) else vals[4]
            vals[5] = f"{vals[5]} %"       if vals[5] is not None else ""
            self._tree.insert("", "end", values=vals)

    def _sort(self, col: str) -> None:
        reverse = self._sort_asc.get(col, False)
        items = [(self._tree.set(k, col), k) for k in self._tree.get_children("")]
        try:
            items.sort(
                key=lambda t: float(
                    t[0].replace("€", "").replace("%", "")
                        .replace(",", "").strip()),
                reverse=reverse)
        except ValueError:
            items.sort(key=lambda t: t[0].lower(), reverse=reverse)
        for idx, (_, k) in enumerate(items):
            self._tree.move(k, "", idx)
        self._sort_asc[col] = not reverse


# ══════════════════════════════════════════════════════════════
#  APPLICATION LAYER
# ══════════════════════════════════════════════════════════════

class DashboardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard Dati — Demo tkinter + ttk")
        self.geometry("1140x720")
        self.minsize(960, 600)
        self.configure(bg="#f4f6f9")

        self._year   = tk.StringVar(value="2024")
        self._search = ""

        self._apply_styles()
        self._build_ui()
        self.refresh()

    # ── stili ────────────────────────────────────────────────
    def _apply_styles(self) -> None:
        s = ttk.Style(self)
        s.theme_use("clam")
        s.configure("TFrame",             background="#f4f6f9")
        s.configure("Card.TFrame",        background="#ffffff", relief="flat")
        s.configure("TLabel",             background="#f4f6f9",
                    font=("Segoe UI", 9))
        s.configure("CardTitle.TLabel",   background="#ffffff",
                    font=("Segoe UI", 8, "bold"), foreground="#666666")
        s.configure("CardValue.TLabel",   background="#ffffff",
                    font=("Segoe UI", 20, "bold"), foreground="#0f0f0f")
        s.configure("AppTitle.TLabel",    background="#1e3a5f",
                    foreground="#ffffff", font=("Segoe UI", 12, "bold"))
        s.configure("Header.TFrame",      background="#1e3a5f")
        s.configure("Treeview",           rowheight=24, font=("Segoe UI", 9))
        s.configure("Treeview.Heading",   font=("Segoe UI", 9, "bold"))
        s.configure("TButton",            font=("Segoe UI", 9))

    # ── layout ───────────────────────────────────────────────
    def _build_ui(self) -> None:
        # — Header —
        header = ttk.Frame(self, style="Header.TFrame", padding=(20, 12))
        header.pack(fill="x")
        ttk.Label(header, text="Dashboard Dati",
                  style="AppTitle.TLabel").pack(side="left")
        ttk.Label(header, text=date.today().strftime("%d %B %Y"),
                  style="AppTitle.TLabel",
                  font=("Segoe UI", 9)).pack(side="right")

        # — Toolbar —
        toolbar = ttk.Frame(self, padding=(20, 8))
        toolbar.pack(fill="x")
        ttk.Label(toolbar, text="Anno:").pack(side="left", padx=(0, 4))
        cb = ttk.Combobox(toolbar, textvariable=self._year,
                          values=YEARS, state="readonly", width=8)
        cb.pack(side="left", padx=(0, 16))
        cb.bind("<<ComboboxSelected>>", lambda e: self.refresh())

        self._search_var = tk.StringVar()
        ttk.Label(toolbar, text="Cerca:").pack(side="left", padx=(0, 4))
        entry = ttk.Entry(toolbar, textvariable=self._search_var, width=22)
        entry.pack(side="left", padx=(0, 6))
        entry.bind("<Return>", lambda e: self._on_search())
        ttk.Button(toolbar, text="Cerca",  command=self._on_search).pack(side="left")
        ttk.Button(toolbar, text="Reset",  command=self._on_reset
                   ).pack(side="left", padx=(4, 0))

        # — KPI row —
        kpi_frame = ttk.Frame(self, padding=(20, 6, 20, 6))
        kpi_frame.pack(fill="x")
        for i in range(4):
            kpi_frame.columnconfigure(i, weight=1)
        self._kpi_cards: list[tuple[str, KPICard]] = []
        for i, (title, (val, delta)) in enumerate(get_kpis("2024").items()):
            card = KPICard(kpi_frame, title, val, delta)
            card.grid(row=0, column=i, sticky="ew", padx=6, pady=4, ipady=4)
            self._kpi_cards.append((title, card))

        # — Charts row —
        cf = ttk.Frame(self, padding=(20, 0, 20, 0))
        cf.pack(fill="x")
        cf.columnconfigure(0, weight=1)
        cf.columnconfigure(1, weight=1)
        self._bar_chart  = BarChart(cf,  title="Fatturato per Categoria")
        self._line_chart = LineChart(cf, title="Andamento Mensile")
        self._bar_chart .grid(row=0, column=0, sticky="nsew", padx=(0, 8), pady=4)
        self._line_chart.grid(row=0, column=1, sticky="nsew", pady=4)

        # — Table —
        tf = ttk.Frame(self, padding=(20, 4, 20, 16))
        tf.pack(fill="both", expand=True)
        ttk.Label(tf, text="Dettaglio Ordini",
                  font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(0, 6))
        self._table = DataTable(tf)
        self._table.pack(fill="both", expand=True)

    # ── logica ───────────────────────────────────────────────
    def _on_search(self) -> None:
        self._search = self._search_var.get().strip()
        self.refresh()

    def _on_reset(self) -> None:
        self._search = ""
        self._search_var.set("")
        self.refresh()

    def refresh(self) -> None:
        year, search = self._year.get(), self._search

        # KPI
        kpis = get_kpis(year, search)
        for (_, card), (__, (val, delta)) in zip(self._kpi_cards, kpis.items()):
            card.set(val)

        # Grafici
        labels, values = get_by_category(year, search)
        self._bar_chart.update(labels, values)
        self._line_chart.update(get_monthly(year))

        # Tabella
        self._table.load(get_rows(year, search))


# ══════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    
    DashboardApp().mainloop()   