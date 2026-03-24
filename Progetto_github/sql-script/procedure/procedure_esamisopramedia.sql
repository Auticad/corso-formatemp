-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	CONTARE ESAMI SOPRA LA MEDIA
-- =============================================
CREATE PROCEDURE sp_VotiSporaMedia
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT
		e.StudenteId,
	COUNT(*)    as [Esami sopra media],
	AVG(e.Voto) as [Media Voti]
	FROM Esame AS e
	GROUP BY e.StudenteId
	HAVING AVG(e.Voto) > (SELECT AVG(Voto) FROM Esame);
END;
GO

