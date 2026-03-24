--========= MAX, MIN, AVG, COUNT, SUM, HANVING
--========= Condizione if => Case When Then Else END Alias

--=====================AVG============================
-- 1 Restuire: la media dei voti per corso
--====================================================
Select 
	c.NomeCorso,
	AVG(e.Voto) AS 'la media dei voti' -- => Calcola la media dei voti usando la funzione AVG()
From Esame e 
Join Corso c ON c.CorsoId = e.CorsoId
GROUP BY c.NomeCorso
ORDER BY AVG(e.Voto) ASC

--===============Con il nome completo dello studente
Select 
	s.Nome + ' ' + s.Cognome AS 'Nome completo dello studente',
	c.NomeCorso,
	AVG(e.Voto) AS 'la media dei voti'
From Esame e 
Join Corso c ON c.CorsoId = e.CorsoId
JOIN Studente s On s.StudenteId = e.StudenteId
GROUP BY c.NomeCorso, s.Nome, s.Cognome
ORDER BY AVG(e.Voto) DESC

--==============Studenti senza esami
SELECT 
    s.Nome,
    s.Cognome
FROM Studente s
LEFT JOIN Esame e ON s.StudenteId = e.StudenteId
WHERE e.EsameId IS NULL;

--=====================COUNT==========================
SELECT COUNT(*) AS NRigheStudente FROM Studente
SELECT Count(*) AS NRigheEsame From Esame
SELECT Count(*) AS NRigheIscrizione From Iscrizione
SELECT Count(*) AS NRigheCorso From Corso
SELECT Count(*) AS NRigheDocente From Docente

--========= NUMERO STUDENTI PER CORSO

SELECT 
    s.Nome AS Studente,
    c.NomeCorso,
    COUNT(e.StudenteId) AS NumeroStudenti
FROM Esame e
JOIN Corso c ON c.CorsoId = e.CorsoId
JOIN Studente s ON e.CorsoId = e.StudenteId
GROUP BY s.Nome, c.NomeCorso;


--====================================================

--=====================MIN============================
SELECT 
    c.NomeCorso AS [nome del Corsp],
    MIN(e.Voto) AS VotoMinmo
FROM Esame e
join Corso c On c.CorsoId = e.CorsoId
GROUP BY c.NomeCorso
ORDER BY VotoMinmo
--====================================================

--=====================MAX============================
SELECT 
    c.NomeCorso AS [nome del Corsp],
    MAX(e.Voto) AS VotoMassimo
FROM Esame e
join Corso c On c.CorsoId = e.CorsoId
GROUP BY c.NomeCorso
ORDER BY VotoMassimo
--====================================================

--=====================SUM============================
--====== Restituire: Somma dei voti per corso
SELECT 
    c.NomeCorso AS [nome del Corsp],
    SUM(e.Voto) AS SommaVoto
FROM Esame e
join Corso c On c.CorsoId = e.CorsoId
GROUP BY c.SommaVoto

--==================Having=============================
--=== Corsi con media > 25
SELECT 
    c.NomeCorso AS [nome del Corsp],
    AVG(e.Voto) AS Media
FROM Esame e
join Corso c On c.CorsoId = e.CorsoId
GROUP BY c.NomeCorso
HAVING AVG(e.Voto) > 25


--=====================================================
-- RESTITUIRE LA LISTA DEGLI STUDENTI CONTANDO:
    -- 1 NUMERO TOTALE DEGLI STUDENTI
    -- 2 MEDIA
    -- 3 IL VOTO MASSIMO
    -- 4 IL VOTO MINIMO
    -- 5 IL TOTALE DEI VOTI


SELECT 
   c.NomeCorso,
   COUNT(*) as STUDENTI,
   AVG(e.Voto) as MEDIA,
   MAX(e.Voto) as MASSIMO,
   MIN(e.Voto) as MINIMO,
   SUM(e.Voto) as TotaleVoti
FROM Esame e
JOIN Corso c ON c.corsoid = e.corsoId
GROUP BY C.NomeCorso
HAVING AVG(e.Voto) >= 25
ORDER BY MEDIA desc
--====================================================

--=============================================================
-- Restituire la lista degli Studenti sopra la media generale
--=============================================================

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

--====================================================
-- STORE PROCEDURE
--====================================================

EXEC sp_GetAllStudeni

EXEC sp_GetStudenteById 30
