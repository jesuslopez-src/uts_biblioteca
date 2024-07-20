USE [biblioteca]
GO

/****** Object:  Table [dbo].[prestamos_documentos]    Script Date: 07/19/2024 19:34:09 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[prestamos_documentos](
	[id] [int] NOT NULL,
	[id_usuario] [int] NOT NULL,
	[id_docu] [int] NOT NULL,
	[fecha_prestamo] [datetime2](0) NULL,
 CONSTRAINT [PK_Prestamos_Documentos] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

ALTER TABLE [dbo].[prestamos_documentos]  WITH CHECK ADD  CONSTRAINT [FK_Prestamos_Documentos_Documentos] FOREIGN KEY([id_docu])
REFERENCES [dbo].[documentos] ([id_documento])
ON UPDATE CASCADE
GO

ALTER TABLE [dbo].[prestamos_documentos] CHECK CONSTRAINT [FK_Prestamos_Documentos_Documentos]
GO

ALTER TABLE [dbo].[prestamos_documentos]  WITH CHECK ADD  CONSTRAINT [FK_Prestamos_Documentos_Usuarios] FOREIGN KEY([id_usuario])
REFERENCES [dbo].[usuarios] ([usu_id])
ON UPDATE CASCADE
GO

ALTER TABLE [dbo].[prestamos_documentos] CHECK CONSTRAINT [FK_Prestamos_Documentos_Usuarios]
GO

