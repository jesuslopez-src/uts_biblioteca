-- Instrucciones para la creacion de la base de datos
CREATE DATABASE IF NOT EXISTS biblioteca
CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci;
USE biblioteca;

CREATE TABLE IF NOT EXISTS Areas_de_conocimientos(
id_area             int unsigned auto_increment not null,              
nombre              varchar(500) not null,
CONSTRAINT  PRIMARY KEY(id_area),
CONSTRAINT  UNIQUE KEY(nombre) 
)ENGINE=InnoDb;
-- UPDATE Areas_de_conocimientos set nombre = TRIM(nombre);
-- INSERT INTO Areas_de_conocimientos VALUES('matemáticas');

CREATE TABLE IF NOT EXISTS Libros(
id                      varchar(10) not null,
titulo			        varchar(300) not null,
autor                   varchar(200) default 'Desconocido',
año_publicacion         year(4),
cantidad                int unsigned,
edicion                 smallint unsigned,
area_de_conocimiento    int unsigned,
CONSTRAINT PRIMARY KEY(id),
CONSTRAINT `fk_conocimientos` FOREIGN KEY(`area_de_conocimiento`) REFERENCES Areas_de_conocimientos (id_area)
ON DELETE SET NULL ON UPDATE CASCADE
)ENGINE=InnoDb;

CREATE TABLE IF NOT EXISTS Usuarios(
usu_id                  int unsigned auto_increment not null,
usu_nom			        varchar(500) not null,
usu_c_identidad         varchar(15) unique not null,
CONSTRAINT PRIMARY KEY(usu_id)
)ENGINE=InnoDb;


CREATE TABLE IF NOT EXISTS Usuarios_Sistema(
fk_usu_id               int unsigned not null,
usu_pass		        varchar(100) not null,
admin_pin               varchar(100),
rol                     varchar(500),
CONSTRAINT PRIMARY KEY(fk_usu_id),
CONSTRAINT `fk_usuarios` FOREIGN KEY(fk_usu_id) REFERENCES Usuarios (usu_id)
ON DELETE RESTRICT ON UPDATE CASCADE
)ENGINE=InnoDb;

-- INSERT INTO Libros VALUES(NULL,'Algún título','pepe','1924',5,1,'matemáticas');

CREATE TABLE IF NOT EXISTS Prestamos_Libros(
id                      int unsigned auto_increment not null,
id_usuario              int unsigned not null,
id_libro                varchar(10) not null,
cantidad_prestamo       smallint unsigned not null,
fecha_prestamo          timestamp not null default CURRENT_TIMESTAMP(),
CONSTRAINT  PRIMARY KEY(id),
CONSTRAINT `fk_libro` FOREIGN KEY(id_libro) REFERENCES Libros (id)
ON DELETE RESTRICT ON UPDATE CASCADE,
CONSTRAINT `fk_el_usuario` FOREIGN KEY(id_usuario) REFERENCES Usuarios (usu_id)
ON DELETE RESTRICT ON UPDATE CASCADE
)ENGINE=InnoDb;

CREATE TABLE IF NOT EXISTS Especialidades(
codigo_especialidad     varchar(15) unique not null,
nombre			        varchar(600) not null unique,
CONSTRAINT PRIMARY KEY(codigo_especialidad)
)ENGINE=InnoDb;

CREATE TABLE IF NOT EXISTS Documentos(
id_documento            int unsigned auto_increment not null,
autor			        varchar(500) not null,
cedula_autor		    varchar(30),
titulo                  varchar(800)not null unique,
especialidad            varchar(15),
tipo                    ENUM('T.E.G','I.P') not null,
año                     year(4) not null,
tutor                   varchar(300),                       
CONSTRAINT PRIMARY KEY(id_documento),
CONSTRAINT UNIQUE KEY(cedula_autor,especialidad,tipo),
CONSTRAINT `fk_especialidad` FOREIGN KEY(especialidad) REFERENCES Especialidades (codigo_especialidad)
ON DELETE SET NULL ON UPDATE CASCADE
)ENGINE=InnoDb;

CREATE TABLE IF NOT EXISTS Prestamos_Documentos(
id                      int unsigned auto_increment not null,
id_usuario              int unsigned not null,
id_docu                 int unsigned not null,
fecha_prestamo          timestamp not null default CURRENT_TIMESTAMP(),
CONSTRAINT PRIMARY KEY(id),
CONSTRAINT `fk_docu` FOREIGN KEY(id_docu) REFERENCES Documentos (id_documento)
ON DELETE RESTRICT ON UPDATE CASCADE,
CONSTRAINT `fk_usuario` FOREIGN KEY(id_usuario) REFERENCES Usuarios(usu_id)
ON DELETE RESTRICT ON UPDATE CASCADE
)ENGINE=InnoDb;

-- disparadores
DELIMITER //
CREATE TRIGGER trim_espacios_areas_conocimientos
BEFORE INSERT ON Areas_de_conocimientos
FOR EACH ROW
BEGIN
    SET NEW.nombre = TRIM(NEW.nombre);
    IF NEW.nombre='' THEN
        SET NEW.nombre=NULL;
    END IF;
END; 


CREATE TRIGGER trim_espacios_especialidades
BEFORE INSERT ON Especialidades
FOR EACH ROW
BEGIN
    SET NEW.codigo_especialidad = TRIM(NEW.codigo_especialidad);
    IF NEW.codigo_especialidad='' THEN
        SET NEW.codigo_especialidad=NULL;
    END IF;
    SET NEW.nombre = TRIM(NEW.nombre);
    IF NEW.nombre='' THEN
        SET NEW.nombre=NULL;
    END IF;
END; 

CREATE TRIGGER trim_libros
BEFORE INSERT ON Libros
FOR EACH ROW
BEGIN
    SET NEW.id = TRIM(NEW.id);
    IF NEW.id='' THEN
        SET NEW.id=NULL;
    END IF;
    SET NEW.titulo = TRIM(NEW.titulo);
    IF NEW.titulo='' THEN
        SET NEW.titulo=NULL;
    END IF;
    SET NEW.autor = TRIM(NEW.autor);
    IF NEW.autor='' THEN
        SET NEW.autor=default;
    END IF;
END; 

CREATE TRIGGER trim_usuarios
BEFORE INSERT ON Usuarios
FOR EACH ROW
BEGIN
    SET NEW.usu_nom = TRIM(NEW.usu_nom);
    IF NEW.usu_nom='' THEN
        SET NEW.usu_nom=NULL;
    END IF;
    SET NEW.usu_c_identidad = TRIM(NEW.usu_c_identidad);
    IF NEW.usu_c_identidad='' THEN
        SET NEW.usu_c_identidad=NULL;
    END IF;
END; 

CREATE TRIGGER trim_usuarios_sistema
BEFORE INSERT ON Usuarios_Sistema
FOR EACH ROW
BEGIN
    SET NEW.usu_pass = TRIM(NEW.usu_pass);
        IF NEW.usu_pass='' THEN
        SET NEW.usu_pass=NULL;
    END IF;
    SET NEW.admin_pin = TRIM(NEW.admin_pin);
    SET NEW.rol = TRIM(NEW.rol);
END;


CREATE TRIGGER trim_documentos
BEFORE INSERT ON Documentos
FOR EACH ROW
BEGIN
    SET NEW.autor = TRIM(NEW.autor);
    IF NEW.autor='' THEN
        SET NEW.autor=NULL;
    END IF;
    SET NEW.cedula_autor = TRIM(NEW.cedula_autor);
    SET NEW.titulo = TRIM(NEW.titulo);
    IF NEW.titulo='' THEN
        SET NEW.titulo=NULL;
    END IF;
    SET NEW.tutor = TRIM(NEW.tutor);
END; //
DELIMITER ;