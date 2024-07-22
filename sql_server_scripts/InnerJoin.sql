SELECT * FROM [biblioteca].[dbo].[usuarios_sistema] INNER JOIN [biblioteca].[dbo].[usuarios]
ON ([biblioteca].[dbo].[usuarios_sistema].fk_usu_id = [biblioteca].[dbo].[usuarios].usu_id) 
WHERE usu_nom='admin' AND usu_pass='8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918';