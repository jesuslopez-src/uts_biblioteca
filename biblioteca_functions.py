from tkinter import messagebox
import sqlite3
from database import agregar_libro, editar_libro, eliminar_libro, obtener_prestamos, obtener_libros, obtener_teg

def mostrar_prestamos(window):
    try:
        data = obtener_prestamos()
        mostrar_tabla(window, data, ['nombre_prestamo', 'autor_prestamo', 'año_prestamo', 'cantidad_prestamo', 'tipo_prestamo', 'fecha_prestamo'], None, None)
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al obtener los préstamos: {str(e)}")

def mostrar_TEG(window):
    try:
        data = obtener_teg()
        mostrar_tabla(window, data, ['nombre', 'autor', 'año', 'cantidad', 'tipo'], None, None)
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al obtener los TEG: {str(e)}")

def mostrar_tabla(window, data, column_names, table, search_entry, editar_fila):
    if not data:
        messagebox.showinfo("No hay Datos Existentes", "Actualmente la tabla está vacia en la Base de Datos...")
        return

    if table is not None:
        table.delete(*table.get_children())

    for row in data:
        table.insert("", "end", values=row)

    def on_double_click(event):
        item = table.selection()[0]
        values = table.item(item, "values")
        editar_fila(window, values)  # Make sure editar_fila is defined or imported correctly

    def on_key_press(event):
        busqueda(window, table, search_entry)  # Make sure busqueda is defined or imported correctly

    table.bind("<Double-1>", on_double_click)
    if search_entry is not None:
        search_entry.bind("<KeyRelease>", on_key_press)


def busqueda(window, table, search_entry):
    search_term = search_entry.get().lower()
    filtered_data = []

    if search_term:
        for child in table.get_children():
            values = table.item(child, "values")
            if search_term in values[1].lower():  # Assuming the title is in the second column (index 1)
                filtered_data.append(values)
    else:
        # If the search entry is empty, display the original data
        filtered_data = obtener_libros()

    table.delete(*table.get_children())

    for row in filtered_data:
        table.insert("", "end", values=row)