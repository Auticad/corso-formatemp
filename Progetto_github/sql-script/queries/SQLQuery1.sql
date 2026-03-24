create table Studente (
	
	StudenteId INT PRIMARY KEY IDENTITY(1,1) NOT NULL, 
	Nome NVARCHAR(100) NOT NULL,
	Cognome NVARCHAR(100) NOT NULL,
	DataNascita DATE ,
	Email NVARCHAR(150) UNIQUE,
	CodiceFiscale CHAR(16) UNIQUE NOT NULL

);

SELECT * FROM Studente;

INSERT INTO Studente (Nome, Cognome, DataNascita, Email, CodiceFiscale)
VALUES 
('Mario', 'Rossi', '2005-03-12', 'mario.rossi@email.it', 'RSSMRA05C12H501A'),
('Laura', 'Bianchi', '2004-07-25', 'laura.bianchi@email.it', 'BNCVRA04L65F205Z'),
('Luca', 'Verdi', '2005-01-15', 'luca.verdi@email.it', 'VRDLUC05A15H501U'),
('Giulia', 'Neri', '2004-11-30', 'giulia.neri@email.it', 'NREGLI04S70L219X'),
('Alessandro', 'Ferrari', '2005-05-20', 'a.ferrari@email.it', 'FRRLSN05E20F205O'),
('Sofia', 'Russo', '2006-02-10', 'sofia.russo@email.it', 'RSSSFO06B50H501C'),
('Francesco', 'Gallo', '2005-09-05', 'f.gallo@email.it', 'GLLFNC05P05L219Q'),
('Marta', 'Fontana', '2004-04-18', 'marta.fontana@email.it', 'FNTMRT04D58F205R'),
('Davide', 'Romano', '2005-12-22', 'd.romano@email.it', 'RMNDVD05T22H501I'),
('Elena', 'Ricci', '2006-01-08', 'elena.ricci@email.it', 'RCCLNE06A48L219B');


IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Studente')
BEGIN
    CREATE TABLE Studente (
        StudenteId INT PRIMARY KEY IDENTITY(1,1) NOT NULL, 
		Nome NVARCHAR(100) NOT NULL,
		Cognome NVARCHAR(100) NOT NULL,
		DataNascita DATE ,
		Email NVARCHAR(150) UNIQUE,
		CodiceFiscale CHAR(16) UNIQUE NOT NULL
    );
END


create table Corso (
	CorsoId INT PRIMARY KEY IDENTITY(1,1) NOT NULL, 
	NomeCorso NVARCHAR(100) NOT NULL,
	Crediti INT NOT NULL,
);

SELECT * FROM Corso;


INSERT INTO Corso (NomeCorso, Crediti)
VALUES 
('Analisi Matematica I', 12),
('Basi di Dati', 9),
('Sistemi Operativi', 6),
('Programmazione a Oggetti', 9),
('Reti di Calcolatori', 6),
('Intelligenza Artificiale', 9),
('Sicurezza Informatica', 6),
('Algoritmi e Strutture Dati', 12),
('Sviluppo Web Mobile', 6),
('Economia e Gestione Aziendale', 9);


-- SVUOTARE TABELLE
TRUNCATE TABLE Studente;

-- RESET INCREMENT
DBCC CHECKIDENT ('Studente', RESEED,1);


create table Docente (
	
	DocenteId INT PRIMARY KEY IDENTITY(1,1) NOT NULL, 
	Nome NVARCHAR(100) NOT NULL,
	Cognome NVARCHAR(100) NOT NULL,
	Email NVARCHAR(100) UNIQUE NOT NULL,
	Telefono CHAR(13) UNIQUE NOT NULL

);

SELECT * FROM Docente;

INSERT INTO Docente (Nome, Cognome, Email, Telefono)
VALUES 
('Alessandro', 'Manzoni', 'a.manzoni@scuola.it', '+393331234567'),
('Giacomo', 'Leopardi', 'g.leopardi@scuola.it', '+393332345678'),
('Italo', 'Svevo', 'i.svevo@scuola.it', '+393333456789'),
('Grazia', 'Deledda', 'g.deledda@scuola.it', '+393334567890'),
('Beppe', 'Fenoglio', 'b.fenoglio@scuola.it', '+393335678901'),
('Elsa', 'Morante', 'e.morante@scuola.it', '+393336789012'),
('Dante', 'Alighieri', 'd.alighieri@scuola.it', '+393337890123'),
('Giovanni', 'Boccaccio', 'g.boccaccio@scuola.it', '+393338901234'),
('Umberto', 'Eco', 'u.eco@scuola.it', '+393339012345'),
('Rita', 'Levi', 'r.levi@scuola.it', '+393330123456');


-- USO LE [ ] E DENTRO POSSO INSERIRE TUTTI I CARATTERI
SELECT (Nome + ' ' + Cognome) as [Nome ebcvbcvbcv564668i79ì""" Cognome], CodiceFiscale FROM Studente;  


CREATE TABLE Iscrizione (

	IscrizioneID INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
	StudenteId INT NOT NULL,
	CorsoId INT NOT NULL,
	DataIscrizione DATE,

	FOREIGN KEY (StudenteId) REFERENCES Studente(StudenteId),
	FOREIGN KEY (CorsoId) REFERENCES Corso(CorsoId)


);

SELECT * FROM Iscrizione;


INSERT INTO Iscrizione(StudenteId, CorsoId, DataIscrizione)
VALUES 
(1, 1, '2026-02-01'), -- Mario Rossi -> Analisi Matematica I
(1, 2, '2026-02-01'), -- Mario Rossi -> Basi di Dati
(2, 2, '2026-02-05'), -- Laura Bianchi -> Basi di Dati
(3, 3, '2026-02-10'), -- Luca Verdi -> Sistemi Operativi
(4, 1, '2026-02-12'), -- Giulia Neri -> Analisi Matematica I
(5, 4, '2026-02-15'), -- Alessandro Ferrari -> Programmazione a Oggetti
(6, 6, '2026-02-20'), -- Sofia Russo -> Intelligenza Artificiale
(7, 8, '2026-02-22'), -- Francesco Gallo -> Algoritmi e Strutture Dati
(8, 5, '2026-02-25'), -- Marta Fontana -> Reti di Calcolatori
(9, 10, '2026-03-01'); -- Davide Romano -> Economia e Gestione Aziendale



