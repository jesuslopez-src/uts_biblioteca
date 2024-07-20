USE [biblioteca]
GO

/****** Object:  Table [dbo].[libros]    Script Date: 07/19/2024 19:32:55 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[libros](
	[id] [varchar](10) NOT NULL,
	[titulo] [varchar](300) NOT NULL,
	[autor] [varchar](200) NULL,
	[año_publicacion] [date] NULL,
	[cantidad] [int] NULL,
	[edicion] [smallint] NULL,
	[area_de_conocimiento] [int] NULL,
 CONSTRAINT [PK_Libros] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO

ALTER TABLE [dbo].[libros]  WITH CHECK ADD  CONSTRAINT [FK_Libros_Areas_de_conocimientos] FOREIGN KEY([area_de_conocimiento])
REFERENCES [dbo].[areas_de_conocimientos] ([id_area])
ON UPDATE CASCADE
ON DELETE SET NULL
GO

ALTER TABLE [dbo].[libros] CHECK CONSTRAINT [FK_Libros_Areas_de_conocimientos]
GO

ALTER TABLE [dbo].[libros] ADD  CONSTRAINT [DF_Libros_autor]  DEFAULT ('Desconocido') FOR [autor]
GO

