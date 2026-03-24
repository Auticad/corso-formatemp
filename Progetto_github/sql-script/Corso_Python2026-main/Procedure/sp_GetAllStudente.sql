SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Moussa
-- Create date: 19/0326
-- Description:	Visualizza tutta la lista degli studenti
-- =============================================
CREATE PROCEDURE sp_GetAllStudeni
AS
BEGIN
	SET NOCOUNT ON;
	SELECT * FROM Studente
END
GO
