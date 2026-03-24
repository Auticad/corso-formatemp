class ContoBancario:
    def __init__(self, saldo):
        self._saldo = saldo
        
    def deposito(self, importo):
        self._saldo += importo
        
    def mostra_saldo(self):
        print(f"Il saldo attuale è: {self._saldo} euro")
        
        
conto = ContoBancario(1000)
conto.mostra_saldo()
conto.deposito(500)
conto.mostra_saldo() 