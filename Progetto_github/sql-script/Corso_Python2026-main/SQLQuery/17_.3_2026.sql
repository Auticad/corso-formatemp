--===============================================
-- 📌 1. MODIFICA IL NOME DI UNA COLONNA
--===============================================
SELECT * FROM Iscrizione;

EXEC sp_rename 'Iscrizione.DtatIscrizione', 'DataIscrizione';

--===============================================
-- 📌 2. MODIFICA IL TIPO DI UNA COLONNA
--===============================================
-- Cambia il tipo o la proprietà (es: rendere NOT NULL)
ALTER TABLE Iscrizione
ALTER COLUMN DataIscrizione DATE NOT NULL;


-- DEFINIZIONE DEL VALORE DI DEFAULT
ALTER TABLE Iscrizione
ADD CONSTRAINT DF_Iscrizione
Default Getdate() for DataIscrizione;

--===============================================
-- 📌 3. AGGIUTA DI UNA COLONNA
--===============================================
ALTER TABLE Iscrizione
ADD Stato NVARCHAR(50) DEFAULT 'Attiva';

--===============================================
-- 📌 4. MODIFICA IL VALORE DI UNA COLONNA
--===============================================
UPDATE Iscrizione
SET Stato = 'Complettata'
where StudenteId = 2;


UPDATE Iscrizione
SET Stato = 'Attiva'
where CorsoId = 2;

--===============================================
-- 📌 5. LIMITARE IL RECORD
--===============================================
SELECT TOP 2 * FROM Studente -- RESTITUISCE SOLO I PRIMI 2 STUDENTI
SELECT TOP 2 Nome, CodiceFiscale FROM Studente -- RESTITUISCE SOLO I PRIMI 2 STUDENTI

--===============================================
-- 📌 5. ELIMINA LA RIGA DI UNA TABELLA
--===============================================

DELETE FROM Studente WHERE StudenteId = 0

--===============================================
-- 📌 6. JOIN -> (INNER JOIN), LEFT JOIN, RIGTH JOIN, FULL JOIN 
--===============================================
SELECT * FROM Studente  --  nome completo e codice fiscale dello studente attiva
SELECT * FROM Iscrizione 
SELECT * FROM Corso -- nome del corso

SELECT
	s.Nome + ' ' + s.Cognome AS 'Nome completo dello studente',
	s.CodiceFiscale,
	c.NomeCorso AS 'Nome del corso'
FROM Studente AS s
JOIN Iscrizione AS i ON s.StudenteId = i.StudenteId --AND i.Stato = 'Attiva' 
JOIN Corso AS c ON i.CorsoId = c.CorsoId
 
