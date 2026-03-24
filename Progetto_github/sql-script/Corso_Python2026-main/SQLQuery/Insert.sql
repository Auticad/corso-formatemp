INSERT INTO Studente (Nome, Cognome, DataNascita, Email, CodiceFiscale)
VALUES
('Mario','Rossi','2000-01-10','mario1@email.com','RSSMRA00A10H501A'),
('Luca','Bianchi','1999-02-11','luca2@email.com','BNCLCU99B11H501B'),
('Giulia','Verdi','2001-03-12','giulia3@email.com','VRDGLI01C12H501C'),
('Anna','Ferrari','2002-04-13','anna4@email.com','FRRNNA02D13H501D'),
('Marco','Romano','1998-05-14','marco5@email.com','RMNMRC98E14H501E'),
('Paolo','Ricci','2000-06-15','paolo6@email.com','RCCPLA00F15H501F'),
('Sara','Gallo','2001-07-16','sara7@email.com','GLLSRA01G16H501G'),
('Davide','Costa','1999-08-17','davide8@email.com','CSTDVD99H17H501H'),
('Elena','Fontana','2002-09-18','elena9@email.com','FNTLNE02I18H501I'),
('Simone','Greco','2000-10-19','simone10@email.com','GRCSMN00L19H501L'),
('Francesca','Conti','2001-11-20','francesca11@email.com','CNTFNC01M20H501M'),
('Andrea','DeLuca','1999-12-21','andrea12@email.com','DLCNDR99N21H501N'),
('Chiara','Marino','2002-01-22','chiara13@email.com','MRNCHR02A22H501O'),
('Alessio','Riva','2000-02-23','alessio14@email.com','RVALSS00B23H501P'),
('Valentina','Lombardi','2001-03-24','valentina15@email.com','LMBVLT01C24H501Q'),
('Giorgio','Barbieri','1998-04-25','giorgio16@email.com','BRBGRG98D25H501R'),
('Martina','Moretti','2002-05-26','martina17@email.com','MRTMTN02E26H501S'),
('Stefano','Ferraro','2000-06-27','stefano18@email.com','FRRSTF00F27H501T'),
('Roberta','Caruso','1999-07-28','roberta19@email.com','CRSRRT99G28H501U'),
('Alberto','Giordano','2001-08-29','alberto20@email.com','GRDLRT01H29H501V'),
('Federica','Colombo','2002-09-30','federica21@email.com','CLMFRC02I30H501W'),
('Claudio','Silvestri','2000-10-01','claudio22@email.com','SLVCLD00L01H501X'),
('Marta','Testa','2001-11-02','marta23@email.com','TSTMRT01M02H501Y'),
('Daniele','Villa','1999-12-03','daniele24@email.com','VLLDNL99N03H501Z'),
('Silvia','Serra','2002-01-04','silvia25@email.com','SRRSVL02A04H501A'),
('Emanuele','Leone','2000-02-05','emanuele26@email.com','LNEEMN00B05H501B'),
('Ilaria','Santoro','2001-03-06','ilaria27@email.com','SNTLRI01C06H501C'),
('Matteo','Fiore','1998-04-07','matteo28@email.com','FRIMTT98D07H501D'),
('Noemi','Ruggiero','2002-05-08','noemi29@email.com','RGGNMI02E08H501E'),
('Fabio','Pellegrini','2000-06-09','fabio30@email.com','PLLFBI00F09H501F');


---==================================================================================

INSERT INTO Corso (NomeCorso, Crediti)
VALUES
('Matematica',6),('Fisica',6),('Informatica',8),('Database',7),
('Programmazione',9),('Reti',6),('Sistemi',7),('Algoritmi',8),
('Statistica',6),('Chimica',5),('Biologia',5),('Elettronica',7),
('Automazione',6),('AI',9),('Machine Learning',9),
('Cybersecurity',8),('Web Dev',7),('Mobile Dev',7),
('Cloud Computing',8),('Big Data',8),('UX Design',6),
('Project Management',5),('Economia',6),('Marketing',5),
('Diritto',5),('Inglese',4),('Francese',4),('Spagnolo',4),
('Storia',5),('Geografia',5);

--==================================================================================
INSERT INTO Docente (Nome, Cognome, Email, Telefono)
VALUES
('Paola','Sarta','doc1@email.com','+393200000001'),
('Michele','Pugliese','doc2@email.com','+393200000002'),
('Laura','Rossi','doc3@email.com','+393200000003'),
('Gianni','Bianchi','doc4@email.com','+393200000004'),
('Franco','Verdi','doc5@email.com','+393200000005'),
('Elisa','Neri','doc6@email.com','+393200000006'),
('Marco','Gialli','doc7@email.com','+393200000007'),
('Anna','Blu','doc8@email.com','+393200000008'),
('Luca','Viola','doc9@email.com','+393200000009'),
('Sara','Rosa','doc10@email.com','+393200000010'),
('Davide','Marrone','doc11@email.com','+393200000011'),
('Chiara','Grigio','doc12@email.com','+393200000012'),
('Alberto','Nero','doc13@email.com','+393200000013'),
('Stefania','Oro','doc14@email.com','+393200000014'),
('Claudio','Argento','doc15@email.com','+393200000015'),
('Martina','Bronzo','doc16@email.com','+393200000016'),
('Simone','Bianco','doc17@email.com','+393200000017'),
('Valeria','Celeste','doc18@email.com','+393200000018'),
('Giorgio','Indaco','doc19@email.com','+393200000019'),
('Roberto','Turchese','doc20@email.com','+393200000020'),
('Federica','Corallo','doc21@email.com','+393200000021'),
('Marta','Ambra','doc22@email.com','+393200000022'),
('Daniele','Perla','doc23@email.com','+393200000023'),
('Silvia','Smeraldo','doc24@email.com','+393200000024'),
('Emanuele','Zaffiro','doc25@email.com','+393200000025'),
('Ilaria','Topazio','doc26@email.com','+393200000026'),
('Matteo','Rubino','doc27@email.com','+393200000027'),
('Noemi','Onice','doc28@email.com','+393200000028'),
('Fabio','Opale','doc29@email.com','+393200000029'),
('Andrea','Diaspro','doc30@email.com','+393200000030');

--==========================================================
INSERT INTO Iscrizione (StudenteId, CorsoId, DataIscrizione)
VALUES
(1,1,'2024-01-01'),(2,2,'2024-01-02'),(3,3,'2024-01-03'),
(4,4,'2024-01-04'),(5,5,'2024-01-05'),(6,6,'2024-01-06'),
(7,7,'2024-01-07'),(8,8,'2024-01-08'),(9,9,'2024-01-09'),
(10,10,'2024-01-10'),(11,11,'2024-01-11'),(12,12,'2024-01-12'),
(13,13,'2024-01-13'),(14,14,'2024-01-14'),(15,15,'2024-01-15'),
(16,16,'2024-01-16'),(17,17,'2024-01-17'),(18,18,'2024-01-18'),
(19,19,'2024-01-19'),(20,20,'2024-01-20'),(21,21,'2024-01-21'),
(22,22,'2024-01-22'),(23,23,'2024-01-23'),(24,24,'2024-01-24'),
(25,25,'2024-01-25'),(26,26,'2024-01-26'),(27,27,'2024-01-27'),
(28,28,'2024-01-28'),(29,29,'2024-01-29'),(30,30,'2024-01-30');


--===========================================================
INSERT INTO Esame (StudenteId, CorsoId, Voto, DataEsame)
VALUES
(1,1,28,'2024-02-01'),
(2,2,30,'2024-02-02'),
(3,3,25,'2024-02-03'),
(4,4,27,'2024-02-04'),
(5,5,29,'2024-02-05'),
(6,6,24,'2024-02-06'),
(7,7,26,'2024-02-07'),
(8,8,30,'2024-02-08'),
(9,9,22,'2024-02-09'),
(10,10,28,'2024-02-10'),
(11,11,21,'2024-02-11'),
(12,12,23,'2024-02-12'),
(13,13,30,'2024-02-13'),
(14,14,27,'2024-02-14'),
(15,15,29,'2024-02-15'),
(16,16,18,'2024-02-16'),
(17,17,24,'2024-02-17'),
(18,18,26,'2024-02-18'),
(19,19,28,'2024-02-19'),
(20,20,30,'2024-02-20'),
(21,21,25,'2024-02-21'),
(22,22,27,'2024-02-22'),
(23,23,29,'2024-02-23'),
(24,24,30,'2024-02-24'),
(25,25,22,'2024-02-25'),
(26,26,24,'2024-02-26'),
(27,27,26,'2024-02-27'),
(28,28,28,'2024-02-28'),
(29,29,30,'2024-02-29'),
(30,30,27,'2024-03-01');