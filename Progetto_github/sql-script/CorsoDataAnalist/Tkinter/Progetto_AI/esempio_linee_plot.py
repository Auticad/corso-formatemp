import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = tk.Tk()
root.title("Line Plot - Temperatura Mensile")
root.geometry("1000x700")
root.configure(bg="#f5f5f5")

# Dati esempio: temperatura media mensile
mesi = ['Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu', 
        'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic']
temp_2023 = [5, 7, 12, 15, 20, 25, 28, 27, 22, 16, 10, 6]
temp_2024 = [4, 6, 11, 16, 21, 26, 30, 29, 24, 17, 11, 7]
temp_2025 = [3, 20, -10, 14, 30, 24, -5, 26, 0, 15, -25, 5]    

# Crea figura
fig = Figure(figsize=(10, 6), dpi=100)
ax = fig.add_subplot(111)

# Plot di due linee con stili diversi
ax.plot(mesi, temp_2023, 
         marker='o',            # marcatori cerchio
         linestyle='-',          # linea continua
         linewidth=2.5,         # spessore linea
         color='#3b82f6',       # blu
         label='2023',
         markersize=8)

ax.plot(mesi, temp_2024,
         marker='s',            # marcatori quadrati
         linestyle=':',         # linea tratteggiata
         linewidth=2.5,
         color='#ef4444',       # rosso
         label='2024',
         markersize=8)

ax.plot(mesi, temp_2025,
         marker='^',            # marcatori triangoli
         linestyle='-.',        # linea punto e linea
         linewidth=4.5,
         color="#94b910",       # verde
         label='2025',
         markersize=8)

# Personalizzazione grafico
ax.set_title('Temperatura Media Mensile', 
              fontsize=18, 
              fontweight='bold',
              pad=20)
ax.set_xlabel('Mese', fontsize=14, fontweight='bold')
ax.set_ylabel('Temperatura (°C)', fontsize=14, fontweight='bold')
ax.legend(loc='upper left', fontsize=12, framealpha=0.9)
ax.grid(True, alpha=0.3, linestyle='--')

# Migliora l'aspetto
fig.tight_layout()

# Incorpora in Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

root.mainloop()