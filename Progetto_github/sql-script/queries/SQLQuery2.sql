SELECT * FROM ISCRIZIONE;

EXEC sp_rename 'Iscrizione.DaraIscrizione', 'DataIscrizione', 'COLUMN';

--PRIMA MODIFICHIAMO TIPO COLONNA

ALTER TABLE Iscrizione
ALTER COLUMN DATAiSCRIZIONE DATE NOT NULL;

--POI PASSIAMO IL VALORE DI DEFAULT

ALTER TABLE Iscrizione
ADD CONSTRAINT DF_Iscrizione 
DEFAULT GETDATE() FOR DATAiSCRIZIONE;

--INSERIAMO COLONNA STATO, IL VALORE DI DEFAUL è SOLO PER I NUOVI VALORI

ALTER TABLE Iscrizione
ADD Stato NVARCHAR(50) DEFAULT 'Attivo';

--AGGIORNO VALORE DELLA COLONNA sTATO

UPDATE Iscrizione	
SET Stato = 'Attivo'
WHERE StudenteId = 1;


SELECT * FROM Iscrizione;
SELECT * FROM Corso;
SELECT * FROM Studente; 

SELECT s.Nome + ' ' + s.CodiceFiscale as [Nome completo dello studente],
		s.CodiceFiscale
FROM Studente AS s
JOIN Iscrizione AS i ON s.StudenteId = i.StudenteId 
JOIN Corso AS c ON C.CorsoId = i.CorsoId
WHERE i.Stato = 'Attivo';


--AGGIUNGERE COLONNA DOCENTEID A CORSO CORSO COME FORENKEY

ALTER TABLE Corso
ADD DocenteId int,
FOREIGN KEY (DocenteId) REFERENCES Docente(DocenteId);


--ASSEGNARE UN CORSO AD UN DOCENTE

SELECT TOP 10 * FROM Corso;
SELECT TOP 10 * FROM Docente;


UPDATE Corso SET DocenteId =1 WHERE CorsoId =1 
UPDATE Corso SET DocenteId =2 WHERE CorsoId =2 
UPDATE Corso SET DocenteId =3 WHERE CorsoId =3 
UPDATE Corso SET DocenteId =4 WHERE CorsoId =4 
UPDATE Corso SET DocenteId =5 WHERE CorsoId =5 
UPDATE Corso SET DocenteId =6 WHERE CorsoId =6 

SELECT @@ROWCOUNT AS RigheAggiornate;  -- Ti dice quante righe ha modificato


--RESTITUIRE LA LISTA DEI DOCENTI ASSEGNATI AI CORSI, MOSTRA NOME COMPLET DOCENTE, NOME DEL CORSO, I CREDITI, NUMERO TELEFONO

SELECT
	d.Nome + ' ' + d.Cognome as [Nome docente ],
	c.NomeCorso, c.Crediti, d.Telefono
FROM Docente d
LEFT JOIN Corso c ON c.DocenteId = d.DocenteId
WHERE c.DocenteId is null;

--CREA LA TABELLA ESAME, EsameiD, StudenteID(fk), CorsoId (FK) Voto CHECK ( Voto BETWEEN 18 AND 30 ) , DataEsame

CREATE TABLE Esame (
    EsameID INT PRIMARY KEY IDENTITY(1,1),
    StudenteId INT NOT NULL,
    CorsoId INT NOT NULL,
    Voto INT,
    DataEsame DATE,
    
    -- Vincolo CHECK per il voto
    CONSTRAINT CK_Esame_Voto CHECK (Voto BETWEEN 18 AND 30),
    
    -- Foreign Key
    FOREIGN KEY (StudenteId) REFERENCES Studente(StudenteId),
    FOREIGN KEY (CorsoId) REFERENCES Corso(CorsoId)
);

-- AGGIUNGERE UNA COLONNA Stato COME DEFAULT 'Superato' nella tabella Esame

ALTER TABLE Esame
ADD Stato NVARCHAR(50) DEFAULT 'Superato';


ALTER TABLE Esame
ADD CONSTRAINT CK_Stato 
CHECK (Stato IN ('Superato', 'Bocciato'));


--Restituire informazioni complete di un esame, dati dello studente, nome corso, nome docente, voto e data
	
SELECT DISTINCT
	s.Nome + ' ' + s.Cognome as [Nome Studente],
	S.CodiceFiscale,
	d.Nome + ' ' + d.Cognome as [Nome Docente],
	e.Voto, e.DataEsame,
	c.NomeCorso	
FROM Esame as e	
INNER JOIN Studente as s on s.StudenteId = e.StudenteId
INNER JOIN Corso c on c.CorsoId = e.CorsoId 
INNER JOIN Docente d ON d.DocenteId = c.DocenteId
INNER JOIN Iscrizione as i on i.StudenteId = s.StudenteId


--restituire la media dei voti per corso, e il nome completo dello studente

SELECT
	s.Nome + ' ' + s.Cognome as [Nome Studente],
	c.NomeCorso, 
	AVG(e.Voto) as [Media dei voti]
FROM Esame as e
JOIN Corso as c on c.CorsoId = e.CorsoId
JOIN Studente AS s on s.StudenteId = e.StudenteId
GROUP BY s.Nome, s.Cognome, c.NomeCorso 
ORDER BY [Media dei voti] ASC


--lista studenti senza esame

SELECT
	s.Nome + ' ' + s.Cognome as [Nome Studente]
FROM Studente as s 
LEFT JOIN Esame as e ON e.StudenteId = s.StudenteId
WHERE e.EsameID IS NULL;

--  COUNT

SELECT COUNT(*) as NRighe FROM Studente;
SELECT COUNT(*) as NRighe FROM Esame;

-- MIN

SELECT 
	c.NomeCorso as [nome del corso],
	MIN(e.Voto) as VotoMinimo
FROM Esame as e
JOIN Corso as c on c.CorsoId = e.CorsoId
GROUP BY c.NomeCorso
ORDER BY VotoMinimo


-- NUMERO STUDENTI PER CORSO

SELECT TOP 10
	s.Nome as Studenrte,
	c.NomeCorso,
	COUNT(e.StudenteId) as [Numero Studenti del Corso]
FROM Studente as s
JOIN Esame as e on e.StudenteId = s.StudenteId
JOIN Corso as c ON c.CorsoId = e.CorsoId
GROUP BY s.Nome, c.NomeCorso;


-- SUM DEI VOTI PER CORSO

SELECT 
	c.NomeCorso as [nome del corso],
	SUM(e.Voto) as SommaVoti
FROM Esame as e
JOIN Corso as c on c.CorsoId = e.CorsoId
GROUP BY c.NomeCorso;


-- HAVING CORSSI CON MEDI > 25

SELECT 
	c.NomeCorso as [nome del corso],
	AVG(e.Voto) as Media
FROM Esame as e
JOIN Corso as c on c.CorsoId = e.CorsoId
GROUP BY c.NomeCorso
HAVING AVG(e.Voto) > 25;




SELECT * FROM Esame
WHERE Voto > 25;


-- LISTA DEGLI STUDENTI CONTNTDNDO: NUMERO TOTALE DEGLI STUDENTI, MEDIA DEI VOTI, IL VOTO MASSIMO, IL VOTO MINIMO, IL TOTALE DEI VOTI

SELECT
	c.NomeCorso,
	COUNT(*) AS STUDENTI,
	AVG(e.Voto) as MediaVoti,
	MAX(e.Voto) as Massimo,
	MIN(e.Voto) as Minimo,
	SUM(e.Voto) as TotaleVoti
FROM  Esame as e
JOIN Corso as c on c.CorsoId = e.CorsoId
GROUP BY C.NomeCorso
HAVING AVG(e.Voto) >= 25
ORDER BY MediaVoti DESC;


-- Restituire la lista degli Studenti sopra la media generale


SELECT 
    Nome,
    Cognome
FROM Studente
WHERE StudenteId IN (
    SELECT StudenteId
    FROM Esame
    GROUP BY StudenteId
    HAVING AVG(Voto) > (
        SELECT AVG(Voto) FROM Esame
    )
);




