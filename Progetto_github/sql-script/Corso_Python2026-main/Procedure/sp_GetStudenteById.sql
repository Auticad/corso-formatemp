-- =============================================
-- Author:		MOUSSA
-- Create date: 19/03/2026
-- Description:	RESTITUISCE LO STUDENTE CON L'ID PASSATO
-- =============================================
CREATE PROCEDURE sp_GetStudenteById
	-- Add the parameters for the stored procedure here
	@StudenteId INT 
AS
BEGIN
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT * from Studente where StudenteId = @StudenteId
END
GO
