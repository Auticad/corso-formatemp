import tkinter as tk

root = tk.Tk() 
root.title("Countdown") 
root.configure(bg="#1e1e2e") 
secondi = [10] 
timer_id = [None] 

lbl = tk.Label(root, text="10", font=("Consolas", 72, "bold"), fg="#a6e3a1", bg="#1e1e2e") 
lbl.pack(pady=30, padx=60) 

def tick(): 
    secondi[0] -= 1 
    lbl.config(text=str(secondi[0])) 
    if secondi[0] <= 3: 
        lbl.config(fg="#f38ba8") 
    
# rosso negli ultimi secondi 
    if secondi[0] > 0: 
        timer_id[0] = root.after(1000, tick) 
    else: 
        lbl.config(text="⏰ Fine!", fg="#f7a26a") 
        
def avvia(): 
    secondi[0] = 10 
    lbl.config(text="10", fg="#a6e3a1") 
    tick() 

def ferma(): 
    if timer_id[0]: 
        root.after_cancel(timer_id[0]) 
        # cancella il prossimo tick 
tk.Button(root, text="▶ Avvia", command=avvia, bg="#a6e3a1", fg="#1e1e2e", font=("Syne",12,"bold")).pack(side="left", padx=20, pady=10) 
tk.Button(root, text="⏹ Ferma", command=ferma, bg="#f38ba8", fg="#1e1e2e", font=("Syne",12,"bold")).pack(side="left", padx=4) 
        
root.mainloop()