import tkinter as tk
from tkinter import ttk

from controller.app_ctrl import AppController


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("La Mia App")
        self.geometry("900x600")
        self.minsize(700, 450)

        # Applica tema ttk
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self._configura_tema()

        # Crea controller (che crea la view)
        self.controller = AppController(self)

    def _configura_tema(self):
        self.style.configure(".",
            font=("Segoe UI", 10),
            background="#f0f2f5"
        )
        self.style.configure("TButton",
            padding=(10, 5),
            relief="flat",
            background="#1877f2",
            foreground="white"
        )
        self.style.map("TButton",
            background=[("active", "#166fe5"),
                        ("disabled", "#cccccc")]
        )

if __name__ == "__main__":
    app = Application()
    app.mainloop()