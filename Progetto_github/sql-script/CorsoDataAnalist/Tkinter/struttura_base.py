import tkinter as tk

root = tk.Tk()

root.title("la mia prima app")

root.geometry("500x350")

root.geometry("500x350+100+100")

root.configure(background='green')

root.resizable(0,0)

root.minsize(300,300)

root.maxsize(500,500)

root.mainloop()