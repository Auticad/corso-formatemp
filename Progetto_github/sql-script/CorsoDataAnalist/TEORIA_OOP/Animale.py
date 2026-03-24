class Animale:
    def __init__(self, nome, razza):
        self.nome = nome
        self.razza = razza
        
    def saluto(self):
        print(f"Ciao, sono {self.nome} e la mia razza e' {self.razza}")
        
a1 = Animale("Torakiki", "Gatto")
a1.saluto()