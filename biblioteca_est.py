from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, messagebox, StringVar
import tkinter as tk
import customtkinter as ctk
import sys
import subprocess
import datetime
from database import create_connection, agregar_prestamo_db, obtener_libros, obtener_teg

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "biblioteca_est" / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def cerrarsesion(window):
    window.destroy()
    from seleccion import SeleccionWindow
    seleccion_window = SeleccionWindow()
    seleccion_window.mainloop()

def agregar_prestamo(window):
    prestamo_ventana = ctk.CTkToplevel(window)
    prestamo_ventana.title('Agregar Prestamo')
    prestamo_ventana.transient(window)
    prestamo_ventana.grab_set()
    prestamo_ventana.focus_set()

    id_var = StringVar()
    cantidad_var = StringVar()

    etiqueta_id = ctk.CTkLabel(prestamo_ventana, text='ID del Libro/T.E.G a Solicitar su Prestamo:')
    etiqueta_id.pack(padx=10, pady=(10, 0))
    entrada_id = ctk.CTkEntry(prestamo_ventana, textvariable=id_var)
    entrada_id.pack(padx=10, pady=(0, 10))

    etiqueta_cantidad = ctk.CTkLabel(prestamo_ventana, text='Cantidad a Prestar:')
    etiqueta_cantidad.pack(padx=10, pady=(10, 0))
    entrada_cantidad = ctk.CTkEntry(prestamo_ventana, textvariable=cantidad_var)
    entrada_cantidad.pack(padx=10, pady=(0, 10))

    boton_agregar = ctk.CTkButton(prestamo_ventana, text='Agregar Prestamo', command=lambda: agregar_prestamo_bd(id_var.get(), cantidad_var.get(), prestamo_ventana, window))
    boton_agregar.pack(padx=10, pady=10)
    
def agregar_prestamo_bd(id, cantidad_prestamo, prestamo_ventana, window):
    libro_data = obtener_libro_por_id(id)

    if not libro_data:
        messagebox.showerror("Error", "LA ID DE LIBRO, NO HA SIDO ENCONTRADO")
        return

    nombre_prestamo, autor_prestamo, año_prestamo, cantidad_actual_str, tipo_prestamo = libro_data
    cantidad_actual = int(cantidad_actual_str)

    if int(cantidad_prestamo) > cantidad_actual:
        messagebox.showerror("Error", "La cantidad solicitada es mayor a la disponible.")
        return

    agregar_prestamo_db(id, cantidad_prestamo, nombre_prestamo, autor_prestamo, año_prestamo, tipo_prestamo)

    mostrar_tabla(window)
    prestamo_ventana.destroy()

def obtener_libro_por_id(id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT nombre, autor, año, cantidad, tipo FROM libros WHERE id = ?', (id,))
    libro_data = cursor.fetchone()
    conn.close()

    return libro_data

def get_max_width(data, col_index):
    return max(len(str(row[col_index])) for row in data)

def mostrar_tabla(window):
    data = obtener_libros()

    if not data:
        messagebox.showinfo("No hay Datos Existentes", "Actualmente la tabla está vacia en la Base de Datos...")
        return

    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview.Heading", font=("Arial", 9, "bold"), background="#dcdcdc")
    style.configure("Treeview.Row", font=("Calibri", 12))
    style.configure("Treeview", background="#dcdcdc")

    table_frame = ttk.Frame(window, padding=1, borderwidth=0.1, relief=tk.FLAT)
    table_frame.pack()

    column_names = ['id', 'nombre', 'autor', 'año', 'cantidad', 'tipo']

    table = ttk.Treeview(window, columns=column_names, show="headings")

    for col in column_names:
        table.heading(col, text=col.upper(), anchor=tk.CENTER)
        table.column(col, width=get_max_width(data, column_names.index(col)), anchor=tk.CENTER)

    for row in data:
        table.insert("", tk.END, values=row)

    table.tag_configure("evenrow", background="#f5f5f5")
    table.tag_configure("oddrow", background="#fff")
    table.tag_configure("headings", background="#333", foreground="#fff")

    table.pack(fill=tk.BOTH, expand=True)
    table.place(x=265, y=362, width=758, height=396)

def mostrar_TEG(window):
    data = obtener_teg()

    if not data:
        messagebox.showinfo("No hay Datos Existentes", "Actualmente la tabla está vacia en la Base de Datos...")
        return

    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#dcdcdc")
    style.configure("Treeview.Row", font=("Calibri", 12))
    style.configure("Treeview", background="#dcdcdc")

    table_frame = ttk.Frame(window, padding=1, borderwidth=0.1, relief=tk.FLAT)
    table_frame.pack()

    column_names = ['nombre', 'autor', 'año', 'cantidad', 'tipo']

    table = ttk.Treeview(window, columns=column_names, show="headings")

    for col in column_names:
        table.heading(col, text=col.upper(), anchor=tk.CENTER)
        table.column(col, width=get_max_width(data, column_names.index(col)), anchor=tk.CENTER)

    for row in data:
        table.insert("", tk.END, values=row)

    table.tag_configure("evenrow", background="#f5f5f5")
    table.tag_configure("oddrow", background="#fff")
    table.tag_configure("headings", background="#333", foreground="#fff")

    table.pack(fill=tk.BOTH, expand=True)
    table.place(x=265, y=362, width=758, height=396)

def create_biblioteca_user_window():
    window = Tk()
    window.geometry("1280x810")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=810,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.create_image(640.0, 407.0, image=image_image_1)

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    canvas.create_image(1160.0, 93.0, image=image_image_2)

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        command=lambda: cerrarsesion(window),
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    button_1.place(x=60.0, y=51.0, width=146.0, height=33.9346923828125)

    button_image_hover_1 = PhotoImage(file=relative_to_assets("button_hover_1.png"))
    button_1.bind('<Enter>', lambda e: button_1.config(image=button_image_hover_1))
    button_1.bind('<Leave>', lambda e: button_1.config(image=button_image_1))

    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    canvas.create_image(640.0, 196.0, image=image_image_3)

    image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
    canvas.create_image(640.0, 224.99999999999983, image=image_image_4)

    image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
    canvas.create_image(644.0, 559.0, image=image_image_5)

    image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
    canvas.create_image(644.0, 560.0, image=image_image_6)

    image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
    canvas.create_image(642.0, 289.0, image=image_image_7)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        command=lambda: agregar_prestamo(window),
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    button_2.place(x=374.0, y=270.0, width=146.0, height=38.0)

    button_image_hover_2 = PhotoImage(file=relative_to_assets("button_hover_2.png"))
    button_2.bind('<Enter>', lambda e: button_2.config(image=button_image_hover_2))
    button_2.bind('<Leave>', lambda e: button_2.config(image=button_image_2))

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        command=lambda: mostrar_TEG(window),
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    button_3.place(x=570.0, y=270.0, width=146.0, height=38.0)

    button_image_hover_3 = PhotoImage(file=relative_to_assets("button_hover_3.png"))
    button_3.bind('<Enter>', lambda e: button_3.config(image=button_image_hover_3))
    button_3.bind('<Leave>', lambda e: button_3.config(image=button_image_3))

    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(
        command=lambda: mostrar_tabla(window),
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    button_4.place(x=766.0, y=270.0, width=146.0, height=38.0)

    button_image_hover_4 = PhotoImage(file=relative_to_assets("button_hover_4.png"))
    button_4.bind('<Enter>', lambda e: button_4.config(image=button_image_hover_4))
    button_4.bind('<Leave>', lambda e: button_4.config(image=button_image_4))

    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    create_biblioteca_user_window()