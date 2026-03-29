# Se lo lasci vuoto, nell'import userai from Models.saluto import Saluta.
# Se aggiungi la riga sotto, puoi scrivere direttamente from Models import Saluta.

from .saluto import Saluta

__all__ = ["Saluta"] # Questo fa in modo che import * importi solo Saluta


