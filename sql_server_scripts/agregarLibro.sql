INSERT INTO [biblioteca].[dbo].[libros]
           ([id]
           ,[titulo]
           ,[autor]
           ,[año_publicacion]
           ,[cantidad]
           ,[edicion]
           ,[area_de_conocimiento])
     VALUES
           ('AD-025'
           ,'El Titulo'
           ,'Pepe Guerrrero'
           ,GETDATE()
           ,5
           ,2
           ,1)
GO


