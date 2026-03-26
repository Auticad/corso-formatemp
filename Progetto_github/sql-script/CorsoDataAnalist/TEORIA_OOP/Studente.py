"""
Struttura del corso
    1 Cos’è la programmazione OOP
    2 Classi e oggetti
    3 Attributi e metodi
    4 Il costruttore (__init__)
    5 Incapsulamento
    6 Ereditarietà
    7 Polimorfismo
    8 Metodi speciali (dunder methods)
    9 Progetto finale guidato
"""

class Studente:
    def __init__(self, nome, cognome, email, data_nascita, codice_fiscale):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.data_nascita = data_nascita
        self.codice_fiscale = codice_fiscale
        
    def mostra_dati(self):
        print(f"Nome: {self.nome}")
        print(f"Cognome: {self.cognome}")
        print(f"Email: {self.email}")
        print(f"Data di nascita: {self.data_nascita}")
        print(f"Codice fiscale: {self.codice_fiscale}")
        
    def __str__(self):
        return f"Studente: {self.nome} {self.cognome} {self.email} {self.data_nascita} {self.codice_fiscale}"
        
s1 = Studente("Mario", "Rossi", "V0BtH@example.com", "1990-01-01", "RSSMRA80A01A123A")
#s1.mostra_dati()

#print(s1)

class RegistroStudenti:
    def __init__(self):
        self._ListaStudenti = []
        
    def aggiungi_studente(self, studente):
        self._ListaStudenti.append(studente)
        
    def mostra_studenti(self):
        for s in self._ListaStudenti:
            print(s)
            
    def cerca_per_email(self, email):
        for s in self._ListaStudenti:
            if s.email == email:
                return s
        return None
    
    def cerca_per_nome(self, nome):
        for s in self._ListaStudenti:
            if s.nome == nome:
                return s
        return None
    
    def cerca_per_cognome(self, cognome):
        for s in self._ListaStudenti:
            if s.cognome == cognome:
                return s
        return None
    
    def cerca_per_codice_fiscale(self, codice_fiscale):
        for s in self._ListaStudenti:
            if s.codice_fiscale == codice_fiscale:
                return s
        return None
    
    def elimina_studente(self, email):
        for s in self._ListaStudenti:
            if s.email == email:
                self._ListaStudenti.remove(s)
                return s
        return None
    
    def modifica_email(self, email, nuova_email):
       s = self.cerca_per_email(email)
       if s:
           s.email = nuova_email           
           return s
       return None
    

# rs = RegistroStudenti()
# rs.aggiungi_studente(s1)
# studenteP = Studente("Pietro", "Cammise", "pietro@gmail.com", "1970-01-01", "BIPPPP80A01A123A")
# rs.aggiungi_studente(studenteP)
# rs.mostra_studenti()
# print(rs.cerca_per_email("V0BtH@example.com"))
# print(rs.cerca_per_codice_fiscale("BIPPPP80A01A123A"))

# print(rs.elimina_studente("pietro@gmail.com"))

# print(rs.mostra_studenti)
# print(rs.modifica_email("V0BtH@example.com", "pietro@gmail.com"))


# ============================================
# TEST DI VERIFICA
# ============================================

print("=" * 60)
print("🧪 TEST: Sistema Registro Studenti")
print("=" * 60)

# 1. Creazione del registro
registro = RegistroStudenti()

# 2. Inserimento di 5 studenti
print("\n📝 Inserimento di 5 studenti...")
studenti_test = [
    Studente("Mario", "Rossi", "mario.rossi@example.com", "1990-01-01", "RSSMRA90A01H501A"),
    Studente("Luigi", "Bianchi", "luigi.bianchi@example.com", "1992-03-15", "BNCLGU92C15F205B"),
    Studente("Anna", "Verdi", "anna.verdi@example.com", "1995-07-22", "VRDNNA95L62L219C"),
    Studente("Giulia", "Neri", "giulia.neri@example.com", "1993-11-08", "NREG LI93S48H501D"),
    Studente("Marco", "Gialli", "marco.gialli@example.com", "1991-05-30", "GLLMRC91E30A123E")
]

for s in studenti_test:
    registro.aggiungi_studente(s)
    print(f"   ✅ Aggiunto: {s.nome} {s.cognome}")

# 3. Visualizzazione lista iniziale
print(f"\n📋 Lista studenti dopo inserimento (totale: {len(registro._ListaStudenti)}):")
registro.mostra_studenti()

# 4. Eliminazione di uno studente (es. Luigi Bianchi)
email_da_eliminare = "luigi.bianchi@example.com"
print(f"\n🗑️  Eliminazione studente con email: {email_da_eliminare}")
studente_eliminato = registro.elimina_studente(email_da_eliminare)

if studente_eliminato:
    print(f"   ✅ Eliminato: {studente_eliminato.nome} {studente_eliminato.cognome}")
else:
    print("   ❌ Studente non trovato!")

# 5. Visualizzazione lista dopo eliminazione
print(f"\n📋 Lista studenti dopo eliminazione (totale: {len(registro._ListaStudenti)}):")
registro.mostra_studenti()

# 6. Verifica finale
print("\n" + "=" * 60)
print("🔍 VERIFICA FINALE:")
print(f"   - Studenti iniziali: 5")
print(f"   - Studenti dopo eliminazione: {len(registro._ListaStudenti)}")
if len(registro._ListaStudenti) == 4:
    print("   ✅ TEST SUPERATO: La logica funziona correttamente!")
else:
    print("   ❌ TEST FALLITO: Qualcosa non ha funzionato.")
print("=" * 60)

# 7. Test aggiuntivi: ricerca e modifica
print("\n🔍 Test ricerca per email:")
risultato = registro.cerca_per_email("anna.verdi@example.com")
if risultato:
    print(f"   ✅ Trovato: {risultato}")
else:
    print("   ❌ Non trovato")

print("\n✏️  Test modifica email:")
registro.modifica_email("anna.verdi@example.com", "anna.verdi.nuova@example.com")
risultato = registro.cerca_per_email("anna.verdi.nuova@example.com")
if risultato:
    print(f"   ✅ Email modificata: {risultato.email}")
else:
    print("   ❌ Modifica fallita")

print("\n🎯 Tutti i test completati!")
            
    