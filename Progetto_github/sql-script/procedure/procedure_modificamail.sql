-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	MODIFICA MAIL DI UNO STUDENTE
-- =============================================
CREATE PROCEDURE SP_ModificaMail 
	-- Add the parameters for the stored procedure here
		@EmailVecchia  nvarchar(150),
		@EmailNuova    nvarchar(150)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	UPDATE [dbo].[Studente]
		   SET    Email = @EmailNuova
		 WHERE  Email = @EmailVecchia;
END;
GO
