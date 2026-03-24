-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	RESTITUIRE LISTA DEGLI STUDENTI sopra la media
-- =============================================
CREATE PROCEDURE sp_ListaStudentiSpraMediaId
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT 
		StudenteId,
		Nome + ' ' + Cognome as [Nome Studente]
	FROM Studente
	WHERE StudenteId IN (
		SELECT StudenteId
		FROM Esame
		GROUP BY StudenteId
		HAVING AVG(Voto) > (
			SELECT AVG(Voto) FROM Esame
		)
	);
END;
GO
