
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, Frame, Label
import tkinter as tk
import sqlite3
import os
import sys
import subprocess
from tkintertable import TableModel, TableCanvas
from customtkinter import CTkButton, CTkFrame
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


def agregar_fila():
    # aqui creamos la miniventana, que se desplegara al lado del programa
    agregar_ventana = tk.Toplevel(window)
    agregar_ventana.title('Agregar Libro/T.E.G')

    #  en terminos simples, esto, primero se hace el titulo, osea la etiqueta de la entry, y seguido de eso, la entry de esa etiqueta
    etiqueta_nombre = tk.Label(agregar_ventana, text='Nombre:')
    etiqueta_nombre.pack()

    entrada_nombre = tk.Entry(agregar_ventana)
    entrada_nombre.pack()

    etiqueta_autor = tk.Label(agregar_ventana, text='Autor:')
    etiqueta_autor.pack()

    entrada_autor = tk.Entry(agregar_ventana)
    entrada_autor.pack()

    etiqueta_año = tk.Label(agregar_ventana, text='Año:')
    etiqueta_año.pack()

    entrada_año = tk.Entry(agregar_ventana)
    entrada_año.pack()

    etiqueta_cantidad = tk.Label(agregar_ventana, text='Cantidad:')
    etiqueta_cantidad.pack()

    entrada_cantidad = tk.Entry(agregar_ventana)
    entrada_cantidad.pack()

    etiqueta_tipo = tk.Label(agregar_ventana, text='Tipo:')
    etiqueta_tipo.pack()

    entrada_tipo = tk.Entry(agregar_ventana)
    entrada_tipo.pack()

    boton_agregar = tk.Button(agregar_ventana, text='agregar', command=lambda: agregar_fila_bd(entrada_nombre.get(), entrada_autor.get(), entrada_año.get(), entrada_cantidad.get(), entrada_tipo.get()))
    boton_agregar.pack()
    

    def agregar_fila_bd(nombre, autor, año, cantidad, tipo):
     # aqui conectamos nuestra db
     conexion = sqlite3.connect('biblioteca.db')
     cursor = conexion.cursor()

    # aqui insertamos los datos que introducimos en los entrys de agregar fila en nuestra tabla
     cursor.execute('INSERT INTO libros (nombre, autor, año, cantidad, tipo) VALUES (?, ?, ?, ?, ?)', (nombre, autor, año, cantidad, tipo))
     
     conexion.commit()

    # esto es para que se refresque la tabla que nos muestra los datos en general, ya sean libros, T.E.G...
     mostrar_tabla()

    # cerramos la conexion
     conexion.close()
    
     messagebox.showinfo("EXITO", "Libro/T.E.G Agregado Exitosamente")

     agregar_ventana.destroy()
    
   


def editar_fila():
    
    editar_ventana = tk.Toplevel(window)
    editar_ventana.title('Editar fila')

    etiqueta_id = tk.Label(editar_ventana, text='ID de la fila a editar:')
    etiqueta_id.pack()

    entrada_id = tk.Entry(editar_ventana)
    entrada_id.pack()

    etiqueta_nombre = tk.Label(editar_ventana, text='Nombre:')
    etiqueta_nombre.pack()

    entrada_nombre = tk.Entry(editar_ventana)
    entrada_nombre.pack()

    etiqueta_autor = tk.Label(editar_ventana, text='Autor:')
    etiqueta_autor.pack()

    entrada_autor = tk.Entry(editar_ventana)
    entrada_autor.pack()

    etiqueta_año = tk.Label(editar_ventana, text='Año:')
    etiqueta_año.pack()

    entrada_año = tk.Entry(editar_ventana)
    entrada_año.pack()

    etiqueta_cantidad = tk.Label(editar_ventana, text='Cantidad:')
    etiqueta_cantidad.pack()

    entrada_cantidad = tk.Entry(editar_ventana)
    entrada_cantidad.pack()
    
    etiqueta_tipo = tk.Label(editar_ventana, text='Tipo:')
    etiqueta_tipo.pack()

    entrada_tipo = tk.Entry(editar_ventana)
    entrada_tipo.pack()

    boton_editar = tk.Button(editar_ventana, text='Editar', command=lambda: editar_fila_bd(entrada_id.get(), entrada_nombre.get(), entrada_autor.get(), entrada_año.get(), entrada_cantidad.get(), entrada_tipo.get()))
    boton_editar.pack()
    
    

    def editar_fila_bd(id , nombre, autor, fecha, cantidad, tipo):
    
      conexion = sqlite3.connect('biblioteca.db')
      cursor = conexion.cursor()

      cursor.execute('UPDATE libros SET nombre = ?, autor = ?, año = ?, cantidad = ?, tipo = ? WHERE id = ?', (nombre, autor, fecha , cantidad, tipo, id))

      conexion.commit()
      
      mostrar_tabla()
    
      conexion.close()
    
      messagebox.showinfo("Edicion Exitosa", "Libro Editado Correctamente") 
      
      editar_ventana.destroy()
    

   

def eliminar_fila():

    eliminar_ventana = tk.Toplevel(window)
    eliminar_ventana.title('Eliminar fila')

    etiqueta_id = tk.Label(eliminar_ventana, text='ID de la fila a eliminar:')
    etiqueta_id.pack()

    entrada_id = tk.Entry(eliminar_ventana)
    entrada_id.pack()

    boton_eliminar = tk.Button(eliminar_ventana, text='Eliminar', command=lambda: eliminar_fila_bd(entrada_id.get()))
    boton_eliminar.pack()
    
    
    def eliminar_fila_bd(id):
   
     conexion = sqlite3.connect('biblioteca.db')
     cursor = conexion.cursor()

     cursor.execute('DELETE FROM libros WHERE id = ?', (id,))
     cursor.execute('SELECT MAX(id) FROM libros')
     max_id = cursor.fetchone()[0]
     cursor.execute('UPDATE sqlite_sequence SET seq = ? WHERE name = ?', (max_id, 'libros'))
     conexion.commit()

  # aqui se resetea la sqlite seq, en donde where name, es el nombre de la tabla a la cual queremos que se le quite el bug del rowid

    # cerramos
     conexion.close()

    # desplegamos un mensajito
     messagebox.showinfo("Eliminacion Exitosa", "Libro Eliminado exitosamente")

    # se cierra la ventanita
     eliminar_ventana.destroy()

def mostrar_prestamos():
  # Citado
  query = "SELECT nombre_prestamo, autor_prestamo, año_prestamo, cantidad_prestamo, tipo_prestamo, fecha_prestamo FROM prestamos"
  data = c.execute(query).fetchall()
  
  if not data:
        messagebox.showinfo("No hay Datos Existentes", "Actualmente la tabla está vacia en la Base de Datos...")
  
  style = ttk.Style()
  style.theme_use("default") 

  style.configure("Treeview.Heading", font=("Arial", 7, "bold"), background="#dcdcdc")
  style.configure("Treeview.Row", font=("Calibri", 12))
  style.configure("Treeview", background="#dcdcdc")
  # Creacion del frame
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
  table.place(x=390, y=377, width=758, height=376)
  


def mostrar_TEG():
  # Citado
  query = "SELECT nombre, autor, año, cantidad, tipo FROM libros WHERE tipo = 'T.E.G';"
  data = c.execute(query).fetchall()
  
  if not data:
        messagebox.showinfo("No hay Datos Existentes", "Actualmente la tabla está vacia en la Base de Datos...")
  
  style = ttk.Style()
  style.theme_use("default") 

  style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#dcdcdc")
  style.configure("Treeview.Row", font=("Calibri", 12))
  style.configure("Treeview", background="#dcdcdc")
  # Creacion del frame
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
  table.place(x=390, y=377, width=758, height=376)
  


def mostrar_tabla():
  # Citado
  query = "SELECT id, nombre, autor, año, cantidad, tipo FROM libros" 
  data = c.execute(query).fetchall()
  
  if not data:
        messagebox.showinfo("No hay Datos Existentes", "Actualmente la tabla está vacia en la Base de Datos...")
  
  style = ttk.Style()
  style.theme_use("default")  # hay varios temas, este es el mas bonito aja

  style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#dcdcdc")
  style.configure("Treeview.Row", font=("Calibri", 12))
  style.configure("Treeview", background="#dcdcdc")
  # Creacion del frame
  table_frame = ttk.Frame(window, padding=1, borderwidth=0.1, relief=tk.FLAT)
  table_frame.pack()  # aqui ajusto los parametros para el espaciado, bordes, etc

  # extraigo el nombre de las columnas
  column_names = [i[0] for i in c.description]

  # creo el widget de treeview, i h8 this fr
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
  table.place(x=390, y=377, width=758, height=376)
  
  
  
# bueno esto es para saber el maximo width de cada columna, osea el col.
def get_max_width(data, col_index):
  return max(len(str(row[col_index])) for row in data)



window = Tk()

window.geometry("1280x810")
window.configure(bg = "#FFFFFF")


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
    330.0,
    299.0,
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
    y=50.0,
    width=146.0,
    height=34.0
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


button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    command = mostrar_prestamos,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_2.place(
    x=160.0,
    y=281.0,
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
    x=351.0,
    y=281.0,
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


image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1147.0,
    85.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    181.0,
    532.0,
    image=image_image_4
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    command = agregar_fila,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_4.place(
    x=108.0,
    y=403.0,
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


image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    769.0,
    565.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    769.0,
    565.0,
    image=image_image_6
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    command = editar_fila,
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_5.place(
    x=108.0,
    y=473.0,
    width=146.0,
    height=38.0
)

button_image_hover_5 = PhotoImage(
    file=relative_to_assets("button_hover_5.png"))

def button_5_hover(e):
    button_5.config(
        image=button_image_hover_5
    )
def button_5_leave(e):
    button_5.config(
        image=button_image_5
    )

button_5.bind('<Enter>', button_5_hover)
button_5.bind('<Leave>', button_5_leave)


button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    command = eliminar_fila,
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_6.place(
    x=108.0,
    y=543.0,
    width=146.0,
    height=38.0
)

button_image_hover_6 = PhotoImage(
    file=relative_to_assets("button_hover_6.png"))

def button_6_hover(e):
    button_6.config(
        image=button_image_hover_6
    )
def button_6_leave(e):
    button_6.config(
        image=button_image_6
    )

button_6.bind('<Enter>', button_6_hover)
button_6.bind('<Leave>', button_6_leave)


button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    command = mostrar_tabla,
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_7.place(
    x=108.0,
    y=613.0,
    width=146.0,
    height=38.0
)

button_image_hover_7 = PhotoImage(
    file=relative_to_assets("button_hover_7.png"))

def button_7_hover(e):
    button_7.config(
        image=button_image_hover_7
    )
def button_7_leave(e):
    button_7.config(
        image=button_image_7
    )

button_7.bind('<Enter>', button_7_hover)
button_7.bind('<Leave>', button_7_leave)


image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    640.0,
    210.0,
    image=image_image_7
)
window.resizable(False, False)
window.mainloop()
