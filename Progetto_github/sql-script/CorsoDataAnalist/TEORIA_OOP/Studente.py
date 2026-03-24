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
    
    def modifia_email(self, email, nuova_email):
       s = self.cerca_per_email(email)
       if s:
           s.email = nuova_email           
           return s
       return None
    
#CREARE UN REGISTRO DI STUDENTI
rs = RegistroStudenti()
rs.aggiungi_studente(s1)
studenteP = Studente("Pietro", "Cammise", "pietro@gmail.com", "1970-01-01", "BIPPPP80A01A123A")
rs.aggiungi_studente(studenteP)
rs.mostra_studenti()
print(rs.cerca_per_email("V0BtH@example.com"))
print(rs.cerca_per_codice_fiscale("BIPPPP80A01A123A"))

print(rs.elimina_studente("pietro@gmail.com"))


print(rs.modifia_email("V0BtH@example.com", "pietro@gmail.com"))


            
    