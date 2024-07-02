-- Instrucciones para la creacion de la base de datos
CREATE DATABASE IF NOT EXISTS biblioteca
CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci;
USE biblioteca;

CREATE TABLE IF NOT EXISTS libros(
id              int unsigned auto_increment not null,
nombre			varchar(800) not null,
autor           varchar(500) not null,
año             year(4),
cantidad        int unsigned,
tipo            text,
CONSTRAINT `pk_libro` PRIMARY KEY(id)
)ENGINE=InnoDb;

CREATE TABLE IF NOT EXISTS prestamos(
id                      int unsigned auto_increment not null,
nombre_prestamo			varchar(800) not null,
autor_prestamo		    varchar(800) not null,
año_prestamo            year(4) not null,
cantidad_prestamo       smallint unsigned not null,
tipo_prestamo           varchar(800),
fecha_prestamo          date,
CONSTRAINT `pk_prestamo` PRIMARY KEY(id)
)ENGINE=InnoDb;

CREATE TABLE IF NOT EXISTS usuarios(
usu_id                  int unsigned auto_increment not null,
usu_nom			        varchar(500) not null,
usu_pass		        text not null,
admin_pin               smallint unsigned not null,
rol                     varchar(600),
CONSTRAINT `pk_usuario` PRIMARY KEY(usu_id)
)ENGINE=InnoDb;