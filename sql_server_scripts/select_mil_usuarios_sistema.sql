/****** Script para el comando SelectTopNRows de SSMS  ******/
SELECT TOP 1000 [fk_usu_id]
      ,[usu_pass]
      ,[admin_pin]
      ,[rol]
  FROM [biblioteca].[dbo].[usuarios_sistema]