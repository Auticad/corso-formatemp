class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return f"{self.nome} {self.cognome}"

    def saluto(self):
        print(f"Ciao, sono {self.nome} {self.cognome}")
        
p1 = Persona("Mario", "Rossi")
print(p1)