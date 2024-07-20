USE [biblioteca]
GO

/****** Object:  Table [dbo].[prestamos_libros]    Script Date: 07/19/2024 19:34:27 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[prestamos_libros](
	[id] [int] NOT NULL,
	[id_usuario] [int] NOT NULL,
	[id_libro] [varchar](10) NOT NULL,
	[cantidad_prestamo] [smallint] NOT NULL,
	[fecha_prestamo] [datetime2](0) NOT NULL,
 CONSTRAINT [PK_Prestamos_Libros] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO

ALTER TABLE [dbo].[prestamos_libros]  WITH CHECK ADD  CONSTRAINT [FK_Prestamos_Libros_Libros] FOREIGN KEY([id_libro])
REFERENCES [dbo].[libros] ([id])
ON UPDATE CASCADE
GO

ALTER TABLE [dbo].[prestamos_libros] CHECK CONSTRAINT [FK_Prestamos_Libros_Libros]
GO

ALTER TABLE [dbo].[prestamos_libros]  WITH CHECK ADD  CONSTRAINT [FK_Prestamos_Libros_Usuarios] FOREIGN KEY([id_usuario])
REFERENCES [dbo].[usuarios] ([usu_id])
ON UPDATE CASCADE
GO

ALTER TABLE [dbo].[prestamos_libros] CHECK CONSTRAINT [FK_Prestamos_Libros_Usuarios]
GO

ALTER TABLE [dbo].[prestamos_libros] ADD  CONSTRAINT [DF_Prestamos_Libros_fecha_prestamo]  DEFAULT (getdate()) FOR [fecha_prestamo]
GO

