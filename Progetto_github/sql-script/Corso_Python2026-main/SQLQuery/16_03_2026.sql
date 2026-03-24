-- =========================================================
-- 📌 1. CREAZIONE DATABASE
-- =========================================================
CREATE DATABASE ScuolaDb;
GO

-- Selezioniamo il database
USE ScuolaDb;
GO


-- =========================================================
-- 📌 2. TABELLA STUDENTE
-- =========================================================
CREATE TABLE Studente
(
    -- ID univoco auto incrementale
    StudenteId INT PRIMARY KEY IDENTITY(1,1) NOT NULL, 
    
    -- Nome e cognome obbligatori
    Nome NVARCHAR(100) NOT NULL,
    Cognome NVARCHAR(100) NOT NULL,
    
    -- Data di nascita opzionale
    DataNascita DATE,
    
    -- Email unica (non duplicabile)
    Email NVARCHAR(150) UNIQUE,
    
    -- Codice fiscale: lunghezza fissa 16 caratteri
    CodiceFiscale CHAR(16) UNIQUE NOT NULL
);


-- =========================================================
-- 📌 3. TABELLA CORSO
-- =========================================================
CREATE TABLE Corso
(
    CorsoId INT PRIMARY KEY IDENTITY(1,1),
    
    NomeCorso NVARCHAR(100) NOT NULL,
    
    -- Numero di crediti del corso
    Crediti INT NOT NULL
);


-- =========================================================
-- 📌 4. TABELLA DOCENTE
-- =========================================================
CREATE TABLE Docente
(
    DocenteId INT PRIMARY KEY IDENTITY(1,1),
    
    Nome NVARCHAR(100) NOT NULL,
    Cognome NVARCHAR(100) NOT NULL,
    
    -- Email obbligatoria e unica
    Email NVARCHAR(256) UNIQUE NOT NULL,
    
    -- Telefono opzionale ma unico
    Telefono CHAR(13) UNIQUE NULL
);


-- =========================================================
-- 📌 5. TABELLA ISCRIZIONE (RELATIONSHIP)
-- =========================================================
-- Questa tabella collega Studente e Corso (molti-a-molti)
CREATE TABLE Iscrizione
(
    IscrizioneId INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    
    -- Chiavi esterne
    StudenteId INT NOT NULL,
    CorsoId INT NOT NULL,
    
    -- Data iscrizione
    DataIscrizione DATE NOT NULL,

    -- Vincoli di integrità referenziale
    FOREIGN KEY (StudenteId) REFERENCES Studente(StudenteId),
    FOREIGN KEY (CorsoId) REFERENCES Corso(CorsoId)
);<


-- =========================================================
-- 📌 6. INSERIMENTO DATI STUDENTI
-- =========================================================
INSERT INTO Studente 
(Nome, Cognome, DataNascita, Email, CodiceFiscale)
VALUES 
('Mario', 'Rossi', '2000-05-12', 'mario.rossi@email.com', 'RSSMRA00E12H501Z'),
('Luca', 'Bianchi', '1999-11-03', 'luca.bianchi@email.com', 'BNCLCU99S03F205X'),
('Giulia', 'Verdi', '2001-02-20', 'giulia.verdi@email.com', 'VRDGLI01B60H501Y'),
('Anna', 'Ferrari', '2002-07-15', 'anna.ferrari@email.com', 'FRRNNA02L55D612T'),
('Marco', 'Romano', '1998-09-28', 'marco.romano@email.com', 'RMNMRC98P28H501U');


-- =========================================================
-- 📌 7. INSERIMENTO DATI CORSI
-- =========================================================
INSERT INTO Corso (NomeCorso, Crediti) 
VALUES
('Matematica', 6),  
('Informatica', 8),
('Fisica', 6),
('Database', 7),
('Programmazione', 9);


-- =========================================================
-- 📌 8. INSERIMENTO DOCENTI
-- =========================================================
INSERT INTO Docente 
(Nome, Cognome, Email, Telefono)
VALUES
('Paola', 'Sarta', 's.paola@gmail.com', '+39321000000'),
('Michele', 'Pugliese', 'm.pugliese@gmail.com', '+39356048565');


-- =========================================================
-- 📌 9. INSERIMENTO ISCRIZIONI
-- =========================================================
INSERT INTO Iscrizione (StudenteId, CorsoId, Dat)
VALUES
(1, 1, '2024-01-10'),
(1, 2, '2024-01-12'),
(2, 3, '2024-01-15'),
(3, 4, '2024-01-20'),
(4, 5, '2024-01-22');


-- =========================================================
-- 📌 10. QUERY BASE
-- =========================================================

-- Visualizza tutti gli studenti
SELECT * FROM Studente;

-- Visualizza tutti i corsi
SELECT * FROM Corso;

-- Visualizza tutti i docenti
SELECT * FROM Docente;

SELECT * FROM Iscrizione 

-- =========================================================
-- 📌 11. CONCATENAZIONE
-- =========================================================
SELECT 
    Nome + ' ' + Cognome AS NomeCompleto,
    CodiceFiscale
FROM Studente;


-- =========================================================
-- 📌 12. PULIZIA DATI
-- =========================================================

-- Cancella tutti i dati
TRUNCATE TABLE Studente;

-- Reset IDENTITY
DBCC CHECKIDENT ('Studente', RESEED, 1);