CREATE PROCEDURE sp_GetStudenteByName
	@NomeStudente NVARCHAR(100)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT * FROM Studente WHERE Nome = @NomeStudente
END
GO
