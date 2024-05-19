from tkinter import messagebox, ttk
import sqlite3
import customtkinter as ctk
from database import agregar_libro, editar_libro, eliminar_libro, obtener_prestamos, obtener_libros, obtener_teg

def agregar_fila(window, search_entry):
    agregar_ventana = ctk.CTkToplevel(window)
    agregar_ventana.title('Agregar Libro/T.E.G')
    agregar_ventana.transient(window)
    agregar_ventana.grab_set()
    agregar_ventana.focus_set()

    etiqueta_nombre = ctk.CTkLabel(agregar_ventana, text='Nombre:')
    etiqueta_nombre.pack(padx=10, pady=(10, 0))
    entrada_nombre = ctk.CTkEntry(agregar_ventana)
    entrada_nombre.pack(padx=10, pady=(0, 10))

    etiqueta_autor = ctk.CTkLabel(agregar_ventana, text='Autor:')
    etiqueta_autor.pack(padx=10, pady=(10, 0))
    entrada_autor = ctk.CTkEntry(agregar_ventana)
    entrada_autor.pack(padx=10, pady=(0, 10))

    etiqueta_año = ctk.CTkLabel(agregar_ventana, text='Año:')
    etiqueta_año.pack(padx=10, pady=(10, 0))
    entrada_año = ctk.CTkEntry(agregar_ventana)
    entrada_año.pack(padx=10, pady=(0, 10))

    etiqueta_cantidad = ctk.CTkLabel(agregar_ventana, text='Cantidad:')
    etiqueta_cantidad.pack(padx=10, pady=(10, 0))
    entrada_cantidad = ctk.CTkEntry(agregar_ventana)
    entrada_cantidad.pack(padx=10, pady=(0, 10))

    etiqueta_tipo = ctk.CTkLabel(agregar_ventana, text='Tipo:')
    etiqueta_tipo.pack(padx=10, pady=(10, 0))
    entrada_tipo = ctk.CTkEntry(agregar_ventana)
    entrada_tipo.pack(padx=10, pady=(0, 10))

    def agregar_libro_handler():
        nombre = entrada_nombre.get()
        autor = entrada_autor.get()
        año = entrada_año.get()
        cantidad = entrada_cantidad.get()
        tipo = entrada_tipo.get()

        if not nombre or not autor or not año or not cantidad or not tipo:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
        else:
            try:
                agregar_libro(nombre, autor, año, cantidad, tipo)
                messagebox.showinfo("Éxito", "Libro agregado exitosamente.")
                mostrar_tabla_libros(window, search_entry)  # Refresh the table after adding a book
                agregar_ventana.destroy()
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al agregar el libro: {str(e)}")

    boton_agregar = ctk.CTkButton(agregar_ventana, text='Agregar', command=agregar_libro_handler)
    boton_agregar.pack(padx=10, pady=10)

def editar_fila(window, values):
    # ... (editar_fila code remains the same)
    print('agregar fila')


def eliminar_fila(window, table, search_entry):
    selected_item = table.selection()
    if not selected_item:
        messagebox.showinfo("No hay selección", "Por favor, seleccione una fila para eliminar.")
        return

    confirmar = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de que desea eliminar la fila seleccionada?")
    if confirmar:
        item = selected_item[0]
        values = table.item(item, "values")
        id = values[0]

        try:
            eliminar_libro(id)
            mostrar_tabla_libros(window, search_entry)  # Refresh the table after deleting a book
            messagebox.showinfo("Éxito", "Libro eliminado exitosamente.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al eliminar el libro: {str(e)}")


def mostrar_prestamos(window):
    # ... (mostrar_prestamos code remains the same)
    print('agregar fila')


def mostrar_TEG(window):
    # ... (mostrar_TEG code remains the same)
    print('agregar fila')


def mostrar_tabla_libros(window, search_entry):
    try:
        data = obtener_libros()
        if not data:
            messagebox.showinfo("No hay Datos Existentes", "Actualmente la tabla está vacia en la Base de Datos...")
            return

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview.Heading", font=("Arial Black", 12), background="#FFFFFF")
        style.configure("Treeview.Row", font=("Arial", 12))
        style.configure("Treeview", background="#FFFFFF")

        table = ttk.Treeview(window, columns=['id', 'nombre', 'autor', 'año', 'cantidad', 'tipo'], show="headings")

        table.heading('id', text='ID', anchor='w')
        table.heading('nombre', text='NOMBRE', anchor='w')
        table.heading('autor', text='AUTOR', anchor='w')
        table.heading('año', text='AÑO', anchor='w')
        table.heading('cantidad', text='CANTIDAD', anchor='w')
        table.heading('tipo', text='TIPO', anchor='w')

        scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=table.yview)
        scrollbar.pack(side='right', fill='y')
        table.configure(yscrollcommand=scrollbar.set)

        for row in data:
            table.insert("", "end", values=row)

        table.tag_configure("evenrow", background="#f5f5f5")
        table.tag_configure("oddrow", background="#fff")
        table.tag_configure("headings", background="#333", foreground="#fff")
        table.place(x=390, y=377, width=758, height=376)

        def on_double_click(event):
            item = table.selection()[0]
            values = table.item(item, "values")
            editar_fila(window, values)

        def on_key_press(event):
            busqueda(window, table, search_entry)

        table.bind("<Double-1>", on_double_click)
        search_entry.bind("<KeyRelease>", on_key_press)

        return table

    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al obtener los libros: {str(e)}")



def mostrar_tabla(window):
    # ... (mostrar_tabla code remains the same)
    print('agregar fila')


def busqueda(window):
    # ... (busqueda code remains the same)
    print('agregar fila')
