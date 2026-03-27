import tkinter as tk

root = tk.Tk()
root.title("Esempio pack")

root.geometry("300x350")

root.configure(bg="#2c3e50")


tk.Label(root, text = "in alto", bg = "red", fg = "blue", padx = 20, pady = 20).pack(side = tk.TOP) 

tk.Label(root, text = "in basso", bg = "red", fg = "blue", padx = 20, pady = 20).pack(side = tk.BOTTOM)

tk.Label(root, text = "in sinistra", bg = "red", fg = "blue", padx = 20, pady = 20).pack(side = tk.LEFT)

tk.Label(root, text = "in destra", bg = "red", fg = "blue", padx = 20, pady = 20).pack(side = tk.RIGHT)



root.mainloop()