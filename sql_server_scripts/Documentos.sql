USE [biblioteca]
GO

/****** Object:  Table [dbo].[documentos]    Script Date: 07/19/2024 19:32:01 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[documentos](
	[id_documento] [int] NOT NULL,
	[autor] [varchar](500) NOT NULL,
	[cedula_autor] [varchar](15) NULL,
	[titulo] [varchar](800) NOT NULL,
	[especialidad] [varchar](15) NULL,
	[tipo] [varchar](8) NULL,
	[año] [smallint] NULL,
	[nombre_tutor] [varchar](300) NULL,
 CONSTRAINT [PK_Documentos] PRIMARY KEY CLUSTERED 
(
	[id_documento] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO

ALTER TABLE [dbo].[documentos]  WITH CHECK ADD  CONSTRAINT [FK_Documentos_Especialidades] FOREIGN KEY([especialidad])
REFERENCES [dbo].[especialidades] ([codigo_especialidad])
ON UPDATE CASCADE
ON DELETE SET NULL
GO

ALTER TABLE [dbo].[documentos] CHECK CONSTRAINT [FK_Documentos_Especialidades]
GO

ALTER TABLE [dbo].[documentos]  WITH CHECK ADD  CONSTRAINT [FK_Documentos_Tipos_Documentos] FOREIGN KEY([tipo])
REFERENCES [dbo].[tipos_documentos] ([tipo_doc])
ON UPDATE CASCADE
ON DELETE SET NULL
GO

ALTER TABLE [dbo].[documentos] CHECK CONSTRAINT [FK_Documentos_Tipos_Documentos]
GO

