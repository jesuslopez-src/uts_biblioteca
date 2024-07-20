USE [biblioteca]
GO

/****** Object:  Table [dbo].[areas_de_conocimientos]    Script Date: 07/19/2024 19:31:34 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[areas_de_conocimientos](
	[id_area] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [varchar](500) NOT NULL,
 CONSTRAINT [PK_Areas_de_conocimientos] PRIMARY KEY CLUSTERED 
(
	[id_area] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO

