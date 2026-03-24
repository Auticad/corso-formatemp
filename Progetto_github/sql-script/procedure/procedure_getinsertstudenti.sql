-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	INSERMENTO STUDENTI
-- =============================================
CREATE PROCEDURE sp_GetInsertStudenti
	-- Add the parameters for the stored procedure here
			@Nome nvarchar(100),
            @Cognome nvarchar(100),
            @DataNascita date,
		    @Email nvarchar(150),
            @CodiceFiscale char(16)	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	INSERT INTO [dbo].[Studente]
           ([Nome]
           ,[Cognome]
           ,[DataNascita]
           ,[Email]
           ,[CodiceFiscale])
     VALUES
           (@Nome, 
		   @Cognome, 
		   @DataNascita, 
		   @Email, 
		   @CodiceFiscale);
END;
GO
