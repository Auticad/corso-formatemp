# class Persone:
#     def saluto(self):
#         print("Ciao, sono una Pietro")


class Persone:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        
    def saluto(self):
        print(f"Ciao, sono {self.nome} e ho {self.eta} anni")
        
        
p1 = Persone("Pietro", 30)
p1.saluto()