USE [biblioteca]
GO

/****** Object:  Table [dbo].[usuarios_sistema]    Script Date: 07/19/2024 19:35:46 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[usuarios_sistema](
	[fk_usu_id] [int] NOT NULL,
	[usu_pass] [varchar](100) NOT NULL,
	[admin_pin] [varchar](100) NULL,
	[rol] [varchar](20) NULL
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO

ALTER TABLE [dbo].[usuarios_sistema]  WITH CHECK ADD  CONSTRAINT [FK_Usuarios_Sistema_Usuarios] FOREIGN KEY([fk_usu_id])
REFERENCES [dbo].[usuarios] ([usu_id])
ON UPDATE CASCADE
GO

ALTER TABLE [dbo].[usuarios_sistema] CHECK CONSTRAINT [FK_Usuarios_Sistema_Usuarios]
GO

