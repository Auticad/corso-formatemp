EXEC sp_GetAlStudenti;

EXEC sp_GetStudenteById 2;

EXEC sp_GetStudenteByName 'Pietro';

EXEC sp_GetInsertStudenti
    @Nome          = 'Pietro',
    @Cognome       = 'Cam',
    @DataNascita   = '1970-01-01',
    @Email         = 'pietro_cam@hotmail.com',
    @CodiceFiscale = 'ASDFGH15H47H155L';

EXEC sp_ModificaMail
    @EmailVecchia = 'pietro_cam@hotmail.com',
    @EmailNuova   = 'HELLO@WORD.IT';

EXEC sp_ListaStudentiSpraMediaId;

EXEC sp_VotiSporaMedia;

	-- LIKE

	SELECT * FROM Studente
	WHERE Nome LIKE 'P%';



SELECT @@VERSION     --Microsoft SQL Server 2022  
SELECT @@SERVERNAME  --DESKTOP-H94GPH9