class Saluta:
    def __init__(self, nome: str):
        self.nome = nome

    def messaggio(self) -> str:
        return f"Ciao, {self.nome}! Benvenuto."