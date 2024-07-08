-- Instrucciones para la creacion de la base de datos
CREATE DATABASE IF NOT EXISTS biblioteca
CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci;
USE biblioteca;

CREATE TABLE IF NOT EXISTS Areas_de_conocimientos(
nombre              varchar(500) unique not null,
CONSTRAINT `pk_nombre` PRIMARY KEY(nombre)
)ENGINE=InnoDb;
-- UPDATE Areas_de_conocimientos set nombre = TRIM(nombre);
-- INSERT INTO Areas_de_conocimientos VALUES('matemáticas');

CREATE TABLE IF NOT EXISTS Libros(
id                      int unsigned auto_increment not null,
titulo			        varchar(800) not null,
autor                   varchar(800) not null,
año_publicacion         year(4),
cantidad                int unsigned,
edicion                 smallint unsigned,
area_de_conocimiento    varchar(500) not null,
CONSTRAINT `pk_libro` PRIMARY KEY(id),
CONSTRAINT `fk_conocimientos` FOREIGN KEY(`area_de_conocimiento`) REFERENCES Areas_de_conocimientos (nombre)
ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=InnoDb;



-- INSERT INTO Libros VALUES(NULL,'Algún título','pepe','1924',5,1,'matemáticas');

CREATE TABLE IF NOT EXISTS Prestamos(
id                      int unsigned auto_increment not null,
nombre_prestamo			varchar(800) not null,
autor_prestamo		    varchar(800) not null,
año_prestamo            year(4) not null,
cantidad_prestamo       smallint unsigned not null,
tipo_prestamo           varchar(800),
fecha_prestamo          date,
CONSTRAINT `pk_prestamo` PRIMARY KEY(id)
)ENGINE=InnoDb;

CREATE TABLE IF NOT EXISTS Usuarios(
usu_id                  int unsigned auto_increment not null,
usu_nom			        varchar(500) not null,
usu_pass		        varchar(100) not null,
admin_pin               varchar(100) not null,
rol                     varchar(500),
CONSTRAINT `pk_usuario` PRIMARY KEY(usu_id)
)ENGINE=InnoDb;

CREATE TABLE IF NOT EXISTS Especialidades(
codigo_especialidad     varchar(15) unique not null,
nombre			        varchar(600) not null unique,
CONSTRAINT `id_especialidad` PRIMARY KEY(codigo_especialidad)
)ENGINE=InnoDb;

CREATE TABLE IF NOT EXISTS Documentos(
id_documento            int unsigned auto_increment not null,
autor			        varchar(500) not null,
cedula_autor		    varchar(30) not null,
titulo                  varchar(800) not null,
especialidad            varchar(15) not null,
tipo                    ENUM('T.E.G','I.P') not null,
año                     year(4) not null,
tutor                   varchar(300),                        
CONSTRAINT `id_documento` PRIMARY KEY(id_documento),
CONSTRAINT `fk_especialidad` FOREIGN KEY(especialidad) REFERENCES Especialidades (codigo_especialidad)
ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=InnoDb;