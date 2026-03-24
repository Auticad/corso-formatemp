SELECT * FROM Esame;

EXEC sp_help;

EXEC sp_columns
@table_name = 'Corso',
@table_owner = 'dbo';

EXEC sp_tables @table_type = "'TABLE'";


EXEC sp_helpdb 'scuoladb';

SELECT @@VERSION     --Microsoft SQL Server 2022  
SELECT @@SERVERNAME  --DESKTOP-H94GPH9