
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import tkinter as tk
import sqlite3
import os
import sys
import subprocess
import datetime

OUTPUT_PATH = os.path.join(os.path.dirname(__file__))
ASSETS_PATH = os.path.join(OUTPUT_PATH, "assets", "frame0")

ruta_directorio_actual = os.getcwd()

ruta_cerrarsesion = os.path.join(ruta_directorio_actual, "Seleccion", "seleccion.py")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

conn = sqlite3.connect('biblioteca.db')
c = conn.cursor()

def cerrarsesion():
    
  window.destroy()

  subprocess.call(["python", ruta_cerrarsesion])
  
  
def get_max_width(data, col_index):
  
  return max(len(str(row[col_index])) for row in data)

def agregar_prestamo():

    prestamo_ventana = tk.Toplevel(window)
    prestamo_ventana.title('Agregar Prestamo')

    # esto es para ingresar la id del libro
    etiqueta_id = tk.Label(prestamo_ventana, text='ID del Libro/T.E.G a Solicitar su Prestamo:')
    etiqueta_id.pack()
    entrada_id = tk.Entry(prestamo_ventana)
    entrada_id.pack()

    # aqui son las entrys para especificar la cantidad a prestar
    etiqueta_cantidad = tk.Label(prestamo_ventana, text='Cantidad a Prestar:')
    etiqueta_cantidad.pack()
    entrada_cantidad = tk.Entry(prestamo_ventana)
    entrada_cantidad.pack()

    # Y bueno esto es como que para que se ejecute el agregar prestamobd, por medio del boton
    boton_agregar = tk.Button(prestamo_ventana, text='Agregar Prestamo', command=lambda: agregar_prestamo_bd(entrada_id.get(), entrada_cantidad.get()))
    boton_agregar.pack()

    def agregar_prestamo_bd(id, cantidad_prestamo):

        # aqui nos conectamso a la base de datos
        conexion = sqlite3.connect('biblioteca.db')
        cursor = conexion.cursor()

        # obtenemos los datos del libro por medio del select, obvio, si es que estamos conectados a una database
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
        conexion.commit()
    
        messagebox.showinfo("Éxito", "Préstamo agregado correctamente.")

        # aqui refrescamos la tabla...
        mostrar_tabla()
        
        conexion.close()

        # esto cerrara la ventana al terminar todo
        prestamo_ventana.destroy()



window = Tk()

window.geometry("1280x810")
window.configure(bg = "#FFFFFF")


def mostrar_tabla():
  # Citado
  query = "SELECT id, nombre, autor, año, cantidad, tipo FROM libros" 
  data = c.execute(query).fetchall()
  
  if not data:
        messagebox.showinfo("No hay Datos Existentes", "Actualmente la tabla está vacia en la Base de Datos...")
  
  style = ttk.Style()
  style.theme_use("default")  # Tema predefinido

  style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#dcdcdc")
  style.configure("Treeview.Row", font=("Calibri", 12))
  style.configure("Treeview", background="#dcdcdc")
  # Creamos el frame
  table_frame = ttk.Frame(window, padding=1, borderwidth=0.1, relief=tk.FLAT)
  table_frame.pack()  # aqui ajusto la ubicacion en dnd quiero que se muestre eso

  # extraigo el nombre de las columnas
  column_names = [i[0] for i in c.description]

  # creo el widget de treeview :3
  table = ttk.Treeview(window, columns=column_names, show="headings")
  

  # colocamos las cabeceras de las columnas y su proporcion
  for col in column_names:
    table.heading(col, text=col.upper(), anchor=tk.CENTER)
    table.column(col, width=get_max_width(data, column_names.index(col)), anchor=tk.CENTER)  # se ajusta la proporcion basado en la data de la tabla

  # aqui insertamos las filas de la tabla
  for row in data:
    table.insert("", tk.END, values=row)

  # estilo de la treeview
  table.tag_configure("evenrow", background="#f5f5f5") 
  table.tag_configure("oddrow", background="#fff")  
  table.tag_configure("headings", background="#333", foreground="#fff") 
 

  table.pack(fill=tk.BOTH, expand=True)
  


  # Posicionamiento
  table.place(x=265, y=362, width=758, height=396)
  
  

  
def mostrar_TEG():
  # Citado
  query = "SELECT nombre, autor, año, cantidad, tipo FROM libros WHERE tipo = 'T.E.G';"
  data = c.execute(query).fetchall()
  
  if not data:
        messagebox.showinfo("No hay Datos Existentes", "Actualmente la tabla está vacia en la Base de Datos...")
  
  style = ttk.Style()
  style.theme_use("default")  # Tema predefinido

  style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#dcdcdc")
  style.configure("Treeview.Row", font=("Calibri", 12))
  style.configure("Treeview", background="#dcdcdc")
  
  table_frame = ttk.Frame(window, padding=1, borderwidth=0.1, relief=tk.FLAT)
  table_frame.pack()  # aqui ajusto la ubicacion en dnd quiero que se muestre eso

  # extraigo el nombre de las columnas
  column_names = [i[0] for i in c.description]

  # creo el widget de treeview, te odio
  table = ttk.Treeview(window, columns=column_names, show="headings")
  

  # colocamos las cabeceras de las columnas y su proporcion
  for col in column_names:
    table.heading(col, text=col.upper(), anchor=tk.CENTER)
    table.column(col, width=get_max_width(data, column_names.index(col)), anchor=tk.CENTER)  # se ajusta la proporcion basado en la data de la tabla

  # aqui insertamos las filas de la tabla
  for row in data:
    table.insert("", tk.END, values=row)

  # estilo de la treeview
  table.tag_configure("evenrow", background="#f5f5f5") 
  table.tag_configure("oddrow", background="#fff")  
  table.tag_configure("headings", background="#333", foreground="#fff") 

  table.pack(fill=tk.BOTH, expand=True)
  


  # Posicionamiento
  table.place(x=265, y=362, width=758, height=396)
  
  

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 810,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    407.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1160.0,
    93.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    command = cerrarsesion,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_1.place(
    x=60.0,
    y=51.0,
    width=146.0,
    height=33.9346923828125
)

button_image_hover_1 = PhotoImage(
    file=relative_to_assets("button_hover_1.png"))

def button_1_hover(e):
    button_1.config(
        image=button_image_hover_1
    )
def button_1_leave(e):
    button_1.config(
        image=button_image_1
    )

button_1.bind('<Enter>', button_1_hover)
button_1.bind('<Leave>', button_1_leave)


image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    640.0,
    196.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    640.0,
    224.99999999999983,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    644.0,
    559.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    644.0,
    560.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    642.0,
    289.0,
    image=image_image_7
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    command = agregar_prestamo,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_2.place(
    x=374.0,
    y=270.0,
    width=146.0,
    height=38.0
)

button_image_hover_2 = PhotoImage(
    file=relative_to_assets("button_hover_2.png"))

def button_2_hover(e):
    button_2.config(
        image=button_image_hover_2
    )
def button_2_leave(e):
    button_2.config(
        image=button_image_2
    )

button_2.bind('<Enter>', button_2_hover)
button_2.bind('<Leave>', button_2_leave)


button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    command = mostrar_TEG,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_3.place(
    x=570.0,
    y=270.0,
    width=146.0,
    height=38.0
)

button_image_hover_3 = PhotoImage(
    file=relative_to_assets("button_hover_3.png"))

def button_3_hover(e):
    button_3.config(
        image=button_image_hover_3
    )
def button_3_leave(e):
    button_3.config(
        image=button_image_3
    )

button_3.bind('<Enter>', button_3_hover)
button_3.bind('<Leave>', button_3_leave)


button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    command = mostrar_tabla,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_4.place(
    x=766.0,
    y=270.0,
    width=146.0,
    height=38.0
)

button_image_hover_4 = PhotoImage(
    file=relative_to_assets("button_hover_4.png"))

def button_4_hover(e):
    button_4.config(
        image=button_image_hover_4
    )
def button_4_leave(e):
    button_4.config(
        image=button_image_4
    )

button_4.bind('<Enter>', button_4_hover)
button_4.bind('<Leave>', button_4_leave)

window.resizable(False, False)
window.mainloop()
