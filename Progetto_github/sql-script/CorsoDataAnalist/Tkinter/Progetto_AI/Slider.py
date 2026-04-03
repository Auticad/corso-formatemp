import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)

year       = ['2002', '2004', '2006', '2008', '2010']
production = [25, 15, 35, 30, 10]

r, g, b = 0.6, 0.2, 0.5
bars = ax.bar(year, production, color=(r, g, b), edgecolor="black")

axred   = plt.axes([0.25, 0.20, 0.65, 0.03])
axgreen = plt.axes([0.25, 0.15, 0.65, 0.03])
axblue  = plt.axes([0.25, 0.10, 0.65, 0.03])

red   = Slider(axred,   'Red',   0.0, 1.0, valinit=0.6)
green = Slider(axgreen, 'Green', 0.0, 1.0, valinit=0.2)
blue  = Slider(axblue,  'Blue',  0.0, 1.0, valinit=0.5)

def update(val):
    color = (red.val, green.val, blue.val)
    for bar in bars:
        bar.set_facecolor(color)
    fig.canvas.draw_idle()  # più efficiente di ridisegnare i bar da zero

red.on_changed(update)
green.on_changed(update)
blue.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button  = Button(resetax, 'Reset', color='gold', hovercolor='skyblue')

def resetSlider(event):
    red.reset()
    green.reset()
    blue.reset()

button.on_clicked(resetSlider)

plt.show()