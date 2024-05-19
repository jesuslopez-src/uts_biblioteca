import hashlib
import sqlite3
import datetime

def create_connection():
    conn = sqlite3.connect('biblioteca.db')
    return conn

def create_tables():
    conn = create_connection()
    c = conn.cursor()

    create_libros_table = """CREATE TABLE IF NOT EXISTS libros (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nombre TEXT,
                                autor TEXT,
                                año NUMERIC,
                                cantidad NUMERIC,
                                tipo TEXT
                            );"""
    c.execute(create_libros_table)
    create_prestamos_table = """CREATE TABLE IF NOT EXISTS prestamos (
                                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   nombre_prestamo TEXT,
                                   autor_prestamo TEXT,
                                   año_prestamo NUMERIC,
                                   cantidad_prestamo NUMERIC,
                                   tipo_prestamo TEXT,
                                   fecha_prestamo TEXT
                               );"""
    c.execute(create_prestamos_table)
    create_usuario_table = """CREATE TABLE IF NOT EXISTS usuario (
                                usu_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                usu_nom TEXT,
                                usu_pass TEXT,
                                admin_pin NUMERIC,
                                rol TEXT
                            );"""
    c.execute(create_usuario_table)
        
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def registrar_admin(usu_nom, usu_pass, admin_pin):
    hashed_contraseña = hash_password(usu_pass)
    hashed_pin = hash_password(admin_pin)
    conn = create_connection()
    c = conn.cursor()
    c.execute('INSERT INTO usuario (usu_nom, usu_pass, admin_pin, rol) VALUES (?, ?, ?, ?)', (usu_nom, hashed_contraseña, hashed_pin, 'ADMIN'))
    c.execute('SELECT MAX(usu_id) FROM usuario')
    max_id = c.fetchone()[0]
    c.execute('UPDATE sqlite_sequence SET seq = ? WHERE name = ?', (max_id, 'usuario'))
    conn.commit()
    conn.close()

def registrar_usuario(usu_nom, usu_pass):
    hashed_contraseña = hash_password(usu_pass)
    conn = create_connection()
    c = conn.cursor()
    c.execute('INSERT INTO usuario (usu_nom, usu_pass, rol) VALUES (?, ?, ?)', (usu_nom, hashed_contraseña, 'USER'))
    c.execute('SELECT MAX(usu_id) FROM usuario')
    max_id = c.fetchone()[0]
    c.execute('UPDATE sqlite_sequence SET seq = ? WHERE name = ?', (max_id, 'usuario'))
    conn.commit()
    conn.close()

def insert_user():
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM usuario WHERE usu_nom = 'admin'")
    count = c.fetchone()[0]
    if count == 0:
        registrar_admin("admin", "admin", "1496")
    else:
        print("Admin user already exists")
    conn.close()

def login_user(usu_nom, usu_pass):
    hashed_contraseña = hash_password(usu_pass)
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM usuario WHERE usu_nom = ? AND usu_pass = ?", (usu_nom, hashed_contraseña))
    user = c.fetchone()
    conn.close()
    return user

def login_admin(usu_nom, usu_pass, admin_pin):
    hashed_contraseña = hash_password(usu_pass)
    hashed_pin = hash_password(admin_pin)
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM usuario WHERE usu_nom = ? AND usu_pass = ? AND admin_pin = ?",
              (usu_nom, hashed_contraseña, hashed_pin))
    user = c.fetchone()
    conn.close()
    return user

def agregar_prestamo_db(id, cantidad_prestamo, nombre_prestamo, autor_prestamo, año_prestamo, tipo_prestamo):
    conn = create_connection()
    cursor = conn.cursor()

    cantidad = obtener_cantidad_libro(id) - int(cantidad_prestamo)
    cursor.execute('UPDATE libros SET cantidad = ? WHERE id = ?', (cantidad, id))

    fecha_prestamo = datetime.datetime.now()
    cursor.execute('INSERT INTO prestamos (nombre_prestamo, autor_prestamo, año_prestamo, cantidad_prestamo, tipo_prestamo, fecha_prestamo) VALUES (?, ?, ?, ?, ?, ?)', (nombre_prestamo, autor_prestamo, año_prestamo, cantidad_prestamo, tipo_prestamo, fecha_prestamo))

    conn.commit()
    conn.close()

def obtener_cantidad_libro(id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT cantidad FROM libros WHERE id = ?', (id,))
    cantidad = cursor.fetchone()[0]
    conn.close()

    return cantidad

def obtener_libros():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nombre, autor, año, cantidad, tipo FROM libros")
    libros = cursor.fetchall()
    conn.close()

    return libros

def obtener_teg():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT nombre, autor, año, cantidad, tipo FROM libros WHERE tipo = 'T.E.G'")
    teg = cursor.fetchall()
    conn.close()

    return teg

def agregar_libro(nombre, autor, año, cantidad, tipo):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO libros (nombre, autor, año, cantidad, tipo) VALUES (?, ?, ?, ?, ?)', (nombre, autor, año, cantidad, tipo))
    conn.commit()
    conn.close()


def editar_libro(id, nombre, autor, año, cantidad, tipo):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('UPDATE libros SET nombre = ?, autor = ?, año = ?, cantidad = ?, tipo = ? WHERE id = ?', (nombre, autor, año, cantidad, tipo, id))
    conn.commit()
    conn.close()

def eliminar_libro(id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM libros WHERE id = ?', (id,))
    cursor.execute('SELECT MAX(id) FROM libros')
    max_id = cursor.fetchone()[0]
    cursor.execute('UPDATE sqlite_sequence SET seq = ? WHERE name = ?', (max_id, 'libros'))
    conn.commit()
    conn.close()


def obtener_prestamos():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT nombre_prestamo, autor_prestamo, año_prestamo, cantidad_prestamo, tipo_prestamo, fecha_prestamo FROM prestamos")
    prestamos = cursor.fetchall()
    conn.close()

    return prestamos

def obtener_libros():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nombre, autor, año, cantidad, tipo FROM libros")
    libros = cursor.fetchall()
    conn.close()

    return libros

def obtener_teg():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT nombre, autor, año, cantidad, tipo FROM libros WHERE tipo = 'T.E.G'")
    teg = cursor.fetchall()
    conn.close()

    return teg
