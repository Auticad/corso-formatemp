import tkinter as tk

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = tk.Tk()
root.title("Istogramma - Distribuzione Età Utenti")
root.geometry("1000x700")

# Genera dati esempio: età di 1000 utenti (distribuzione normale)
np.random.seed(42)
eta_utenti = np.random.normal(loc=35, scale=12, size=1000)
eta_utenti = np.clip(eta_utenti, 18, 70)  # limita età tra 18-70

fig = Figure(figsize=(10, 6), dpi=100)
ax = fig.add_subplot(111)


# Crea istogramma
n, bins, patches = ax.hist(
    eta_utenti,
    bins=30,                 # numero di intervalli
    color='#8b5cf6',
    edgecolor='#6d28d9',
    alpha=0.7,
    linewidth=1.5
)

# Aggiungi linea di media
media = np.mean(eta_utenti)
ax.axvline(media, color='#ef4444', linestyle='--', linewidth=2.5,
            label=f'Media: {media:.1f} anni')


std   = np.std(eta_utenti)

ax.axvline(media - std, color="#5216f9", linestyle=':', linewidth=2,
           label=f'−1 std ({media - std:.1f})')
ax.axvline(media + std, color='#5216f9', linestyle=':', linewidth=2,
           label=f'+1 std ({media + std:.1f})')

# Aggiungi marcatori
for i in range(len(bins) - 1):
    x = (bins[i] + bins[i + 1]) / 2
    y = n[i]
    ax.text(x, y, y, ha='center', va='bottom', fontsize=10)

# Personalizzazione
ax.set_title('Distribuzione Età Utenti', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Età (anni)', fontsize=14, fontweight='bold')
ax.set_ylabel('Frequenza', fontsize=14, fontweight='bold')
ax.legend(fontsize=12)
ax.grid(alpha=0.3, linestyle='--')

# Statistiche aggiuntive
stats_text = f'N = {len(eta_utenti)}\nStd = {np.std(eta_utenti):.1f}'
ax.text(0.02, 0.95, stats_text,
        transform=ax.transAxes,
        fontsize=11,
        verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

fig.tight_layout()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

root.mainloop()