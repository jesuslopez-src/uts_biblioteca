import hashlib
import datetime
import pyodbc 
from tkinter import messagebox

def create_connection():
    servidor = 'DESKTOP-78S6O5M\\SQLEXPRESS'  # Nombre del servidor SQL con el cual se hará la conexión
    bddatos = 'biblioteca'  # Nombre de la base de datos SQL
    usuario = 'dbo' # Nombre del usuario conectado a la base de datos
    #clave = ''  # Contraseña del usuario de SQL
    conn = pyodbc.connect('DRIVER={SQL server};SERVER='+servidor+';DATABASE='+bddatos)
    print('conexion exitosa')
    cursor = conn.cursor()
    cursor.execute(f"SELECT TABLE_NAME FROM {bddatos}.INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
    
    for row in cursor.fetchall():
        print (row)
    cursor.close()
    print(conn.getinfo(pyodbc.SQL_DATABASE_NAME))
    print(conn.getinfo(pyodbc.SQL_USER_NAME))
    return conn

# def create_connection():
#     conn = pyodbc.connect('biblioteca')
#     return conn

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def registrar_admin(conn,usu_nom, usu_pass, admin_pin):
    hashed_contraseña = hash_password(usu_pass)
    hashed_pin = hash_password(admin_pin)
    c = conn.cursor()
    c.execute(f'INSERT INTO {conn.getinfo(pyodbc.SQL_DATABASE_NAME)}.{conn.getinfo(pyodbc.SQL_USER_NAME)}.[usuarios]\
            ([usu_nom],[usu_c_identidad]) VALUES (?,?)',(usu_nom,'18205268'))
    conn.commit()
    c.execute(f"SELECT usu_id FROM {conn.getinfo(pyodbc.SQL_DATABASE_NAME)}.{conn.getinfo(pyodbc.SQL_USER_NAME)}.usuarios WHERE usu_c_identidad = '18205268'")
    usu_id = c.fetchone()[0]
    c.execute(f'INSERT INTO {conn.getinfo(pyodbc.SQL_DATABASE_NAME)}.{conn.getinfo(pyodbc.SQL_USER_NAME)}.[usuarios_sistema]\
            ([fk_usu_id],[usu_pass],[admin_pin],[rol]) VALUES (?,?,?,?)',(usu_id,hashed_contraseña,hashed_pin,'admin'))
    # max_id = c.fetchone()[0]
    # c.execute('UPDATE sqlite_sequence SET seq = ? WHERE name = ?', (max_id, 'usuarios'))
    conn.commit()

def registrar_usuario(usu_nom, usu_pass,usu_cedula)->tuple:
    hashed_contraseña = hash_password(usu_pass)
    conn = create_connection()
    c = conn.cursor()
    #chequear si el usuario ya existe en la tabla usuarios de la base de datos 
    c.execute(f"SELECT usu_id FROM {conn.getinfo(pyodbc.SQL_DATABASE_NAME)}.{conn.getinfo(pyodbc.SQL_USER_NAME)}.usuarios WHERE usu_c_identidad = ?",(usu_cedula))
    usuario = c.fetchone()
    mensaje =("Registro Exitoso", "Usuario registrado exitosamente")
    if  usuario == None:
        c.execute(f'INSERT INTO {conn.getinfo(pyodbc.SQL_DATABASE_NAME)}.{conn.getinfo(pyodbc.SQL_USER_NAME)}.[usuarios] (usu_nom, usu_c_identidad) VALUES (?, ?)', (usu_nom,usu_cedula))
        c.commit()
        c.execute(f'SELECT MAX(usu_id) FROM {conn.getinfo(pyodbc.SQL_DATABASE_NAME)}.{conn.getinfo(pyodbc.SQL_USER_NAME)}.[usuarios]')
        usu_id = c.fetchone()[0]
        c.execute(f'INSERT INTO {conn.getinfo(pyodbc.SQL_DATABASE_NAME)}.{conn.getinfo(pyodbc.SQL_USER_NAME)}.[usuarios_sistema] (fk_usu_id, usu_pass, admin_pin, rol) VALUES (?, ?, ?, ?)', (usu_id, hashed_contraseña,None,"user"))
    else:
        usu_id = usuario[0]
        c.execute(f"SELECT fk_usu_id FROM {conn.getinfo(pyodbc.SQL_DATABASE_NAME)}.{conn.getinfo(pyodbc.SQL_USER_NAME)}.usuarios_sistema WHERE fk_usu_id = ?",(usu_id))
        usuario = c.fetchone()
        if  usuario == None:
            c.execute(f'INSERT INTO {conn.getinfo(pyodbc.SQL_DATABASE_NAME)}.{conn.getinfo(pyodbc.SQL_USER_NAME)}.[usuarios_sistema] (fk_usu_id, usu_pass, admin_pin, rol) VALUES (?, ?, ?, ?)', (usu_id, hashed_contraseña,None,"user"))
        else:
            mensaje = ("Registro exitoso","usuario previamente registrado")
    c.commit()
    conn.close()
    return mensaje

def insert_user():
    conn = create_connection()
    c = conn.cursor()
    c.execute(f"SELECT COUNT(*) FROM {conn.getinfo(pyodbc.SQL_DATABASE_NAME)}.{conn.getinfo(pyodbc.SQL_USER_NAME)}.usuarios_sistema WHERE rol = 'admin'")
    count = c.fetchone()[0]
    if count == 0:
        registrar_admin(conn,"admin", "admin", "1496")
    else:
        print("Admin user already exists")
    conn.close()

def login_user(usu_nom, usu_pass):
    hashed_contraseña = hash_password(usu_pass)
    conn = create_connection()
    c = conn.cursor()
    c.execute(f"SELECT * FROM {conn.getinfo(pyodbc.SQL_DATABASE_NAME)}.{conn.getinfo(pyodbc.SQL_USER_NAME)}.usuarios_sistema\
              INNER JOIN {conn.getinfo(pyodbc.SQL_DATABASE_NAME)}.{conn.getinfo(pyodbc.SQL_USER_NAME)}.usuarios\
              ON ({conn.getinfo(pyodbc.SQL_DATABASE_NAME)}.{conn.getinfo(pyodbc.SQL_USER_NAME)}.[usuarios_sistema].fk_usu_id = {conn.getinfo(pyodbc.SQL_DATABASE_NAME)}.{conn.getinfo(pyodbc.SQL_USER_NAME)}.[usuarios].usu_id) WHERE usu_nom = ? AND usu_pass = ?", (usu_nom, hashed_contraseña))
    user = c.fetchone()
    conn.close()
    # print(user)
    return user

def login_admin(usu_nom, usu_pass, admin_pin):
    hashed_contraseña = hash_password(usu_pass)
    hashed_pin = hash_password(admin_pin)
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios WHERE usu_nom = ? AND usu_pass = ? AND admin_pin = ?",
              (usu_nom, hashed_contraseña, hashed_pin))
    user = c.fetchone()
    conn.close()
    return user

def agregar_prestamo_db(id, cantidad_prestamo, nombre_prestamo, autor_prestamo, año_prestamo, tipo_prestamo):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT nombre, autor, año, cantidad, tipo FROM libros WHERE id = ?', (id,))
    libro_data = cursor.fetchone()

        # Validar si el ID del libro existe
    if not libro_data:
            messagebox.showerror("Error", "LA ID DE LIBRO, NO HA SIDO ENCONTRADO")
            return

    nombre_prestamo, autor_prestamo, año_prestamo, cantidad_actual_str, tipo_prestamo = libro_data

        # aqui convertimos la cantidad actual a entero...
    cantidad_actual = int(cantidad_actual_str)

        # Validamos la cantidad prestada
    if int(cantidad_prestamo) > cantidad_actual:
            messagebox.showerror("Error", "La cantidad solicitada es mayor a la disponible.")
            return

        # Actualizamos la cantidad del libro
    cantidad = cantidad_actual - int(cantidad_prestamo)
    cursor.execute('UPDATE libros SET cantidad = ? WHERE id = ?', (cantidad, id))

        # registramos el prestamo
    fecha_prestamo = datetime.datetime.now()
    cursor.execute('INSERT INTO prestamos (nombre_prestamo, autor_prestamo, año_prestamo, cantidad_prestamo, tipo_prestamo, fecha_prestamo) VALUES (?, ?, ?, ?, ?, ?)', (nombre_prestamo, autor_prestamo, año_prestamo, cantidad_prestamo, tipo_prestamo, fecha_prestamo))

        # bueno, esperemos que se confirme la operaciom y cerramos la conexion
    conn.commit()
    
    messagebox.showinfo("Éxito", "Préstamo agregado correctamente.")

# def obtener_cantidad_libro(id):
#     conn = create_connection()
#     cursor = conn.cursor()

#     cursor.execute('SELECT cantidad FROM libros WHERE id = ?', (id,))
#     cantidad = cursor.fetchone()[0]
#     conn.close()

#     return cantidad

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

# def agregar_libro(nombre, autor, año, cantidad, tipo):
#     conn = create_connection()
#     cursor = conn.cursor()

#     cursor.execute('INSERT INTO libros (nombre, autor, año, cantidad, tipo) VALUES (?, ?, ?, ?, ?)', (nombre, autor, año, cantidad, tipo))
#     conn.commit()
#     conn.close()

# def editar_libro(id, nombre, autor, año, cantidad, tipo):
#     conn = create_connection()
#     cursor = conn.cursor()

#     cursor.execute('UPDATE libros SET nombre = ?, autor = ?, año = ?, cantidad = ?, tipo = ? WHERE id = ?', (nombre, autor, año, cantidad, tipo, id))
#     conn.commit()
#     conn.close()

# def eliminar_libro(id):
#     conn = create_connection()
#     cursor = conn.cursor()

#     cursor.execute('DELETE FROM libros WHERE id = ?', (id,))
#     cursor.execute('SELECT MAX(id) FROM libros')
#     max_id = cursor.fetchone()[0]
#     cursor.execute('UPDATE sqlite_sequence SET seq = ? WHERE name = ?', (max_id, 'libros'))
#     conn.commit()
#     conn.close()

  
# def eliminar_prestamo(id):
#     conn = create_connection()
#     cursor = conn.cursor()

#     cursor.execute('DELETE FROM prestamos WHERE id = ?', (id,))
#     cursor.execute('SELECT MAX(id) FROM prestamos')
#     max_id = cursor.fetchone()[0]
#     cursor.execute('UPDATE sqlite_sequence SET seq = ? WHERE name = ?', (max_id, 'prestamos'))
#     conn.commit()
#     conn.close()
    

# def obtener_prestamos():
#     conn = create_connection()
#     cursor = conn.cursor()

#     cursor.execute("SELECT id, nombre_prestamo, autor_prestamo, año_prestamo, cantidad_prestamo, tipo_prestamo, fecha_prestamo FROM prestamos")
#     prestamos = cursor.fetchall()
#     conn.close()

#     return prestamos

# def obtener_libros():
#     conn = create_connection()
#     cursor = conn.cursor()

#     cursor.execute("SELECT id, nombre, autor, año, cantidad, tipo FROM libros")
#     libros = cursor.fetchall()
#     conn.close()

#     return libros

# def obtener_teg():
#     conn = create_connection()
#     cursor = conn.cursor()

#     cursor.execute("SELECT nombre, autor, año, cantidad, tipo FROM libros WHERE tipo = 'T.E.G'")
#     teg = cursor.fetchall()
#     conn.close()

#     return teg

if __name__ == "__main__":
    print(__name__)
    create_connection()