from tkinter import messagebox, ttk
import sqlite3
import customtkinter as ctk
from database import agregar_libro, editar_libro, eliminar_libro, obtener_prestamos, obtener_libros, obtener_teg, eliminar_prestamo

def create_connection():
    conn = sqlite3.connect('biblioteca.db')
    return conn

def agregar_fila(window, search_entry, table):
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

                for item in table.get_children():
                    table.delete(item)

                data = obtener_libros()
                for row in data:
                    table.insert("", "end", values=row)

                agregar_ventana.destroy()
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al agregar el libro: {str(e)}")

    boton_agregar = ctk.CTkButton(agregar_ventana, text='Agregar', command=agregar_libro_handler)
    boton_agregar.pack(padx=10, pady=10)

def editar_fila(window, values, table):
    editar_ventana = ctk.CTkToplevel(window)
    editar_ventana.title('Editar fila')
    editar_ventana.transient(window)
    editar_ventana.grab_set()
    editar_ventana.focus_set()

    etiqueta_id = ctk.CTkLabel(editar_ventana, text='ID de la fila a editar:')
    etiqueta_id.pack(padx=10, pady=(10, 0))
    entrada_id = ctk.CTkEntry(editar_ventana)
    entrada_id.insert(0, values[0])
    entrada_id.configure(state='readonly')
    entrada_id.pack(padx=10, pady=(0, 10))

    etiqueta_nombre = ctk.CTkLabel(editar_ventana, text='Nombre:')
    etiqueta_nombre.pack(padx=10, pady=(10, 0))
    entrada_nombre = ctk.CTkEntry(editar_ventana)
    entrada_nombre.insert(0, values[1])
    entrada_nombre.pack(padx=10, pady=(0, 10))

    etiqueta_autor = ctk.CTkLabel(editar_ventana, text='Autor:')
    etiqueta_autor.pack(padx=10, pady=(10, 0))
    entrada_autor = ctk.CTkEntry(editar_ventana)
    entrada_autor.insert(0, values[2])
    entrada_autor.pack(padx=10, pady=(0, 10))

    etiqueta_año = ctk.CTkLabel(editar_ventana, text='Año:')
    etiqueta_año.pack(padx=10, pady=(10, 0))
    entrada_año = ctk.CTkEntry(editar_ventana)
    entrada_año.insert(0, values[3])
    entrada_año.pack(padx=10, pady=(0, 10))

    etiqueta_cantidad = ctk.CTkLabel(editar_ventana, text='Cantidad:')
    etiqueta_cantidad.pack(padx=10, pady=(10, 0))
    entrada_cantidad = ctk.CTkEntry(editar_ventana)
    entrada_cantidad.insert(0, values[4])
    entrada_cantidad.pack(padx=10, pady=(0, 10))

    etiqueta_tipo = ctk.CTkLabel(editar_ventana, text='Tipo:')
    etiqueta_tipo.pack(padx=10, pady=(10, 0))
    entrada_tipo = ctk.CTkEntry(editar_ventana)
    entrada_tipo.insert(0, values[5])
    entrada_tipo.pack(padx=10, pady=(0, 10))

    def editar_libro_handler():
        id = entrada_id.get()
        nombre = entrada_nombre.get()
        autor = entrada_autor.get()
        año = entrada_año.get()
        cantidad = entrada_cantidad.get()
        tipo = entrada_tipo.get()

        if not id or not nombre:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
        else:
            try:
                editar_libro(id, nombre, autor, año, cantidad, tipo)
                messagebox.showinfo("Éxito", "Libro editado exitosamente.")
                for item in table.get_children():
                    table.delete(item)

                data = obtener_libros()
                for row in data:
                    table.insert("", "end", values=row)
                editar_ventana.destroy()
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al editar el libro: {str(e)}")

    boton_editar = ctk.CTkButton(editar_ventana, text='Editar', command=editar_libro_handler)
    boton_editar.pack(padx=10, pady=10)
    
def eliminar_fila(table):
    selected_items = table.selection()
    if selected_items:
        item = selected_items[0]  
        values = table.item(item, "values") 
        book_id = values[0]  

        confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este libro?")
        if confirm:
            try:
                eliminar_libro(book_id) 
                table.delete(item)
                messagebox.showinfo("Éxito", "Libro eliminado exitosamente.")
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al eliminar el libro: {str(e)}")
    else:
        messagebox.showwarning("Advertencia", "No has seleccionado ningún libro.")
        
def eliminar_prestamos(table):
    selected_items = table.selection()
    if selected_items:
        item = selected_items[0]  
        values = table.item(item, "values") 
        prestamo_id = values[0]  

        confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este prestamo?")
        if confirm:
            try:
                eliminar_prestamo(prestamo_id) 
                table.delete(item)
                messagebox.showinfo("Éxito", "Prestamo eliminado exitosamente.")
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al eliminar el Prestamo: {str(e)}")
    else:
        messagebox.showwarning("Advertencia", "No has seleccionado ningún Prestamo.")

def mostrar_tabla_prestamos(window, search_entry):
    try:
        data = obtener_prestamos()

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview.Heading", font=("Arial Black", 12), background="#FFFFFF")
        style.configure("Treeview.Row", font=("Arial", 12))
        style.configure("Treeview", background="#FFFFFF")

        table = ttk.Treeview(window, columns=['id', 'nombre_prestamo', 'autor_prestamo', 'año_prestamo', 'cantidad_prestamo', 'tipo_prestamo','fecha_prestamo'], show="headings")

        table.heading('id', text='ID', anchor='w')
        table.heading('nombre_prestamo', text='NOMBRE', anchor='w')
        table.heading('autor_prestamo', text='AUTOR', anchor='w')
        table.heading('año_prestamo', text='AÑO', anchor='w')
        table.heading('cantidad_prestamo', text='CANTIDAD', anchor='w')
        table.heading('tipo_prestamo', text='TIPO', anchor='w')
        table.heading('fecha_prestamo', text='FECHA', anchor='w')

        for row in data:
            table.insert("", "end", values=row)

        table.tag_configure("evenrow", background="#f5f5f5")
        table.tag_configure("oddrow", background="#fff")
        table.tag_configure("headings", background="#333", foreground="#fff")
        table.place(x=390, y=377, width=758, height=376)


        return table

    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al obtener los prestamos: {str(e)}")
        return table


def mostrar_TEG(window, search_entry, table):
    try:
        data = obtener_teg()
        if not data:
            messagebox.showinfo("No hay Datos Existentes", "Actualmente no hay TEG en la Base de Datos...")
            return

        for item in table.get_children():
            table.delete(item)

        for row in data:
            table.insert("", "end", values=row)

    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al obtener los TEG: {str(e)}")

def mostrar_tabla_libros(window, search_entry, table):
    try:
        data = obtener_libros()

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview.Heading", font=("Arial Black", 12), background="#FFFFFF")
        style.configure("Treeview.Row", font=("Arial", 12))
        style.configure("Treeview", background="#FFFFFF")

        table = ttk.Treeview(window, columns=['id', 'titulo', 'autor', 'año_publicacion', 'cantidad', 'edicion','area_de_conocimiento'], show="headings")

        table.heading('id', text='ID', anchor='w')
        table.heading('titulo', text='TITULO', anchor='w')
        table.heading('autor', text='AUTOR', anchor='w')
        table.heading('año_publicacion', text='AÑO', anchor='w')
        table.heading('cantidad', text='CANTIDAD', anchor='w')
        table.heading('edicion', text='EDICION', anchor='w')
        table.heading('area_de_conocimiento', text='CATEGORIA', anchor='w')

        for row in data:
            row = tuple(row)
            table.insert("", "end", values=row)

        table.tag_configure("evenrow", background="#f5f5f5")
        table.tag_configure("oddrow", background="#fff")
        table.tag_configure("headings", background="#333", foreground="#fff")
        table.place(x=390, y=377, width=758, height=376)

        def on_double_click(event):
            item = table.selection()[0]
            values = table.item(item, "values")
            editar_fila(window, values, table)

        def on_key_press(event):
            busqueda(window, table, search_entry, event)

        table.bind("<Double-1>", on_double_click)
        search_entry.bind("<KeyRelease>", on_key_press)

        return table

    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al obtener los libros: {str(e)}")
        return table

def busqueda(window, table, search_entry, event=None):
    search_term = search_entry.get().lower()
    filtered_data = []

    if search_term:
        for child in table.get_children():
            values = table.item(child, "values")
            if search_term in values[1].lower():  
                filtered_data.append(values)
    else:
        filtered_data = obtener_libros()

    table.delete(*table.get_children())

    for row in filtered_data:
        row = tuple(row)
        table.insert("", "end", values=row)
