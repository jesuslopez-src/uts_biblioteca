USE [biblioteca]
GO

/****** Object:  Table [dbo].[tipos_documentos]    Script Date: 07/19/2024 19:35:04 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[tipos_documentos](
	[tipo_doc] [varchar](8) NOT NULL,
	[Descripcion] [varchar](300) NULL,
 CONSTRAINT [PK_Tipos_Documentos] PRIMARY KEY CLUSTERED 
(
	[tipo_doc] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO

