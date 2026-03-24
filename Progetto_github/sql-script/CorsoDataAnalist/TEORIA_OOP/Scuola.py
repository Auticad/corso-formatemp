# Importazione corretta dal file Persona.py
from Persona import Persone

class Scuola:
    def __init__(self):
        # L'istanza va creata preferibilmente dentro il costruttore
        self.p1 = Persone()
    
    def avvia_saluto(self):
        # Il metodo viene richiamato su un'istanza specifica
        self.p1.saluto()

# Esempio di utilizzo razionale
if __name__ == "__main__":
    mia_scuola = Scuola()
    mia_scuola.avvia_saluto()