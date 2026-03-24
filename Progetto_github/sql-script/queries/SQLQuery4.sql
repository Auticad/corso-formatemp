SELECT 
    local_tcp_port AS [Porta SQL Server],
    connection_id
FROM sys.dm_exec_connections
WHERE local_net_address IS NOT NULL
  AND session_id = @@SPID;


EXEC xp_readerrorlog 0, 1, N'Server is listening on';