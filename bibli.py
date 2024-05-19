from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, ttk, messagebox
import sqlite3
from database import agregar_libro, editar_libro, eliminar_libro, obtener_prestamos, obtener_libros, obtener_teg
import customtkinter as ctk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "biblioteca_adm" / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def cerrarsesion(window):
    window.destroy()
    from seleccion import SeleccionWindow
    seleccion_window = SeleccionWindow()
    seleccion_window.mainloop()

def agregar_fila(window, table, refresh_table):
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
                refresh_table()  
                agregar_ventana.destroy()
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al agregar el libro: {str(e)}")

    boton_agregar = ctk.CTkButton(agregar_ventana, text='Agregar', command=agregar_libro_handler)
    boton_agregar.pack(padx=10, pady=10)

def editar_fila(window, values, refresh_table):
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
                refresh_table() 
                editar_ventana.destroy()
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al editar el libro: {str(e)}")

    boton_editar = ctk.CTkButton(editar_ventana, text='Editar', command=editar_libro_handler)
    boton_editar.pack(padx=10, pady=10)

def eliminar_fila(table, refresh_table):
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
            table.delete(item)
            messagebox.showinfo("Éxito", "Libro eliminado exitosamente.")
            refresh_table()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al eliminar el libro: {str(e)}")

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

def mostrar_tabla_libros(window, search_entry):
    try:
        data = obtener_libros()
        table = ttk.Treeview(window, columns=['id', 'nombre', 'autor', 'año', 'cantidad', 'tipo'], show="headings")
        mostrar_tabla(window, data, ['id', 'nombre', 'autor', 'año', 'cantidad', 'tipo'], table, search_entry)
        table.place(x=390, y=377, width=758, height=376)
        return table
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al obtener los libros: {str(e)}")

def mostrar_tabla(window, data, column_names, table, search_entry):
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
        editar_fila(window, values, refresh_table)

    def on_key_press(event):
        busqueda(window, table, search_entry)

    table.bind("<Double-1>", on_double_click)
    if search_entry is not None:
        search_entry.bind("<KeyRelease>", on_key_press)

def busqueda(window, table, search_entry):
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
        table.insert("", "end", values=row)

def create_biblioteca_admin_window():
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
        command=lambda: cerrarsesion(window),
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
        command=lambda: mostrar_prestamos(window),
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
        command=lambda: mostrar_TEG(window),
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
    
    def refresh_table():
        table = mostrar_tabla_libros(window, search_entry)
        return table

    button_4 = Button(
        command=lambda: agregar_fila(window, refresh_table(), refresh_table),
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
        command=lambda: editar_fila(window),
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

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    canvas.create_image(730.0, 300, image=entry_image_1)

    search_entry = Entry(
        window,
        bd=0,
        bg="#BDBDBD",
        fg="#000716",
        highlightthickness=0
    )
    search_entry.place(x=648.0, y=289, width=178.0, height=25.0)

    table = ttk.Treeview(window, columns=['id', 'nombre', 'autor', 'año', 'cantidad', 'tipo'], show="headings")
    table = mostrar_tabla_libros(window, search_entry)

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        command=lambda: eliminar_fila(table, refresh_table),
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
        command=refresh_table,
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

if __name__ == "__main__":
    create_biblioteca_admin_window()