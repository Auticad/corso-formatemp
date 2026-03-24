--======================================================
-- ESERCIZIO 1: AGGIUNGERE LA COLONNA DocenteId 
--		        come chiave esterna nella tabelle Corso
--======================================================
ALTER TABLE Corso
ADD DocenteId INT NULL;


ALTER TABLE Corso
ADD CONSTRAINT FK_Corso_Docente
FOREIGN KEY (DocenteId) REFERENCES Docente(DocenteId);
--======================================================
-- ESERCIZIO 2: ASEGNATE UN COSO AD UN DOCENTE
--======================================================
Select * from Docente
Select * from Corso

UPDATE Corso SET DocenteId = 1 WHERE CorsoId = 1
UPDATE Corso SET DocenteId = 5 WHERE CorsoId = 6

--======================================================
-- ESERCIZIO 3: restiture la lista dei docenti asegnati ai corsi
-- Campi da visualizzare
-- (Nome completo del docente, nome del corso, crediti, telefono)
--======================================================
select 
	d.Nome + ' ' + d.cognome AS 'Nome completo del docente',
	c.NomeCorso, 
	c.Crediti, 
	d.Telefono
from Docente d
INNER JOIN Corso c ON c.DocenteId = d.DocenteId




select 
	d.Nome + ' ' + d.cognome AS 'Nome completo del docente',
	c.NomeCorso, 
	c.Crediti, 
	d.Telefono
from Docente d
left JOIN Corso c ON c.DocenteId = d.DocenteId
Where c.DocenteId Is NULL


--======================================================
/*
Mostrare le informazione complete di un esame, includendo
	Dati dello studente
	corso
	docente 
	voto e data 
*/
--======================================================
SELECT DISTINCT -- Distinct ci permette di rimuovere i dupplicati
	s.Nome + ' ' + s.Cognome AS Studente,
	s.CodiceFiscale,
	dc.Nome + ' ' + dc.Cognome AS Docente,
	c.NomeCorso as Corso,
	e.Voto,
	e.DataEsame As Data
FROM Esame as e
INNER JOIN Studente AS s On s.StudenteId = e.StudenteId 
INNER JOIN Corso AS c On c.CorsoId = e.CorsoId
INNER JOIN Docente AS dc On dc.DocenteId = c.DocenteId 
INNER JOIN Iscrizione AS i ON i.StudenteId = s.StudenteId



--======================================================
-- ESERCIZIO 4: 
	-- CREARE LA TABELLA Esame (EsameId,  StudenteId(Fk), CorsoId (Fk), Voto CHECK (Voto BETWEEN 18 AND 30), DataEsame) 
--======================================================

CREATE TABLE Esame
(
	EsameId Int Primary key Identity(1,1),
	StudenteId int,
	CorsoId Int,
	Voto int CHECK (Voto BETWEEN 18 AND 30),
	DataEsame Date NOT NULL,

	FOREIGN KEY (StudenteId) REFERENCES Studente(StudenteId),
	FOREIGN KEY (CorsoId) REFERENCES Corso(CorsoId)
);

--======================================================
-- ESERCIZIO 5:
-- AGGIUNGERE UNA COLONNA STATO COME DEFAULT 'Superato' nella tabella Esame
--======================================================
ALTER TABLE Esame ADD Stato NVARCHAR(20) DEFAULT 'Superato';

ALTER TABLE Esame
ADD CONSTRAINT CK_Stato 
CHECK (Stato IN ('Superato', 'Bocciato'));

Select * from Esame

-- Aggiunta della colonna Lode nella tabella Esame con un valore di default di tipo booleano (vero/falso)  
/*
	| Valore | Significato |   Imposta un valore automatico
	| ------ | ----------- |	👉 Se non inserisci nulla:
	| 0      | NO          |	Lode = 0
	| 1      | SI          |

	La colonna Lode serve per indicare:
	1 → lo studente ha preso 30 e lode 🏆
	0 → voto normale

*/
ALTER TABLE Esame ADD Lode BIT DEFAULT 0;