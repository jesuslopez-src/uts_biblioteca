from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, messagebox, StringVar
import tkinter as tk
import customtkinter as ctk
from monitors import detect_monitor
from screeninfo import get_monitors
from PIL import ImageTk, Image, ImageOps
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

def dis_enable_cantidad(tipo_docu,entry:ctk.CTkEntry,cantidad:StringVar):
    if tipo_docu != 'Libro':
        cantidad.set('1')
        entry.configure(state='disable')
    else:
        cantidad.set('')
        entry.configure(state='normal')

def agregar_prestamo(window):
    prestamo_ventana = ctk.CTkToplevel(window)
    prestamo_ventana.title('Agregar Prestamo')
    prestamo_ventana.transient(window)
    prestamo_ventana.grab_set()
    prestamo_ventana.focus_set()

    id_var = StringVar()
    cantidad_var = StringVar()
    get_tipo_documento = StringVar()

    etiqueta_docu = ctk.CTkLabel(prestamo_ventana, text='Tipo de Documento a Solicitar su Prestamo:')
    etiqueta_docu.pack(padx=10, pady=(10, 0))
    tipo_documento = ['Libro','T.E.G','I.P']
    combobox = ttk.Combobox(prestamo_ventana,values=tipo_documento,width=6,state='readonly',textvariable=get_tipo_documento)
    combobox.pack(padx=10, pady=(10, 0))
    combobox.set('Libro')
    combobox.bind("<<ComboboxSelected>>",lambda e:dis_enable_cantidad(get_tipo_documento.get(),entrada_cantidad,cantidad_var))

    etiqueta_id = ctk.CTkLabel(prestamo_ventana, text='ID del Documento a Solicitar su Prestamo:')
    etiqueta_id.pack(padx=10, pady=(10, 0))
    entrada_id = ctk.CTkEntry(prestamo_ventana, textvariable=id_var)
    entrada_id.pack(padx=10, pady=(0, 10))

    etiqueta_cantidad = ctk.CTkLabel(prestamo_ventana, text='Cantidad a Prestar:')
    etiqueta_cantidad.pack(padx=10, pady=(10, 0))
    entrada_cantidad = ctk.CTkEntry(prestamo_ventana, textvariable=cantidad_var)
    entrada_cantidad.pack(padx=10, pady=(0, 10))

    boton_agregar = ctk.CTkButton(prestamo_ventana, text='Agregar Prestamo', command=lambda: agregar_prestamo_bd(get_tipo_documento.get(),id_var.get(), cantidad_var.get(), prestamo_ventana, window))
    boton_agregar.pack(padx=10, pady=10)
    
def agregar_prestamo_bd(tipo_documento,id, cantidad_prestamo, prestamo_ventana, window):
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

class create_biblioteca_user_window(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.monitors = get_monitors()
        self.monitor = detect_monitor()
        self.monitor_width=self.monitor.width
        self.monitor_height=self.monitor.height
        # self.monitor_width=self.monitors[0].width
        # self.monitor_height=self.monitors[0].height
        self.configure(bg="#FFFFFF")
        self.title("Biblioteca UTS")
        self.resizable(False, False)
        self.num_columnas = 60
        self.num_filas = 28
        self.create_widgets()

    def create_widgets(self):

        imagen_raw = Image.open(str(relative_to_assets("image_1.png")))
        imagen = ImageOps.contain(imagen_raw,(self.monitor_width,self.monitor_height))
        self.background_image = ImageTk.PhotoImage(imagen)
        self.geometry(f"{self.background_image.width()}x{self.background_image.height()}")

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=self.background_image.height(),
            width=self.background_image.width(),
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)
        canvas.create_image(0, 0, anchor="nw", image=self.background_image)

        # image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        # canvas.create_image(1160.0, 93.0, image=image_image_2)
        image_image_2_raw = Image.open(str(relative_to_assets("image_2.png")))
        image_image_2_width= int(self.background_image.width()*30/self.num_columnas)
        image_image_2_height= int(self.background_image.height()*5/self.num_filas)
        image_image_2_new_size = ImageOps.contain(image_image_2_raw,(image_image_2_width,image_image_2_height))
        self.image_image_2 = ImageTk.PhotoImage(image_image_2_new_size)
        canvas.create_image(self.background_image.width()*52/self.num_columnas, self.background_image.height()*4/self.num_filas, image=self.image_image_2)

        # button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_image_1_raw = Image.open(str(relative_to_assets("button_1.png")))
        button_1_width=int(self.background_image.width()*7/self.num_columnas)
        button_1_height=int(self.background_image.height()*3/self.num_filas)
        button_image_1_new_size = ImageOps.contain(button_image_1_raw,(button_1_width,button_1_height))
        button_image_1 = ImageTk.PhotoImage(button_image_1_new_size)
        button_1 = Button(
            command=lambda: cerrarsesion(self),
            image=button_image_1,
            borderwidth=0,
            cursor="hand2",
            highlightthickness=0,
            relief="flat"
        )
        # button_1.place(x=60.0, y=51.0, width=146.0, height=33.9346923828125)
        button_1.place(anchor="center",x=self.background_image.width()*6/self.num_columnas, y=self.background_image.height()*2/self.num_filas, width=button_image_1.width(), height=button_image_1.height())

        # button_image_hover_1 = PhotoImage(file=relative_to_assets("button_hover_1.png"))
        button_image_hover_1_raw = Image.open(str(relative_to_assets("button_hover_1.png")))
        button_image_hover_1_new_size = ImageOps.contain(button_image_hover_1_raw,(button_1_width,button_1_height))
        button_image_hover_1 = ImageTk.PhotoImage(button_image_hover_1_new_size)
        button_1.bind('<Enter>', lambda e: button_1.config(image=button_image_hover_1))
        button_1.bind('<Leave>', lambda e: button_1.config(image=button_image_1))

        # self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        image_image_3_raw = Image.open(str(relative_to_assets("image_3.png")))
        image_image_3_width= int(self.background_image.width()*30/self.num_columnas)
        image_image_3_height= int(self.background_image.height()*5/self.num_filas)
        image_image_3_new_size = ImageOps.contain(image_image_3_raw,(image_image_3_width,image_image_3_height))
        self.image_image_3 = ImageTk.PhotoImage(image_image_3_new_size)
        canvas.create_image(self.background_image.width()*30/self.num_columnas, self.background_image.height()*7/self.num_filas, image=self.image_image_3)
        # canvas.create_image(640.0, 196.0, image=self.image_image_3)

        # self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        image_image_4_raw = Image.open(str(relative_to_assets("image_4.png")))
        image_image_4_width= int(self.background_image.width()*30/self.num_columnas)
        image_image_4_height= int(self.background_image.height()*5/self.num_filas)
        image_image_4_new_size = ImageOps.contain(image_image_4_raw,(image_image_4_width,image_image_4_height))
        self.image_image_4 = ImageTk.PhotoImage(image_image_4_new_size)
        canvas.create_image(self.background_image.width()*30/self.num_columnas, self.background_image.height()*8/self.num_filas,anchor="s", image=self.image_image_4)
        # canvas.create_image(640.0, 224.99999999999983, image=self.image_image_4)

        # self.image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        image_image_5_raw = Image.open(str(relative_to_assets("image_5.png")))
        image_image_5_width= int(self.background_image.width()*42/self.num_columnas)
        image_image_5_height= int(self.background_image.height()*15/self.num_filas)
        image_image_5_new_size = ImageOps.contain(image_image_5_raw,(image_image_5_width,image_image_5_height))
        self.image_image_5 = ImageTk.PhotoImage(image_image_5_new_size)
        self.positionx_5_6 = self.background_image.width()*30/self.num_columnas
        self.positiony_5_6 = self.background_image.height()*19/self.num_filas
        canvas.create_image(self.positionx_5_6, self.positiony_5_6, image=self.image_image_5)
        # canvas.create_image(644.0, 559.0, image=self.image_image_5)

        # self.image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        image_image_6_raw = Image.open(str(relative_to_assets("image_6.png")))
        image_image_6_width= image_image_5_width
        image_image_6_height= image_image_5_height
        image_image_6_new_size = ImageOps.contain(image_image_6_raw,(image_image_6_width,image_image_6_height))
        self.image_image_6 = ImageTk.PhotoImage(image_image_6_new_size)
        canvas.create_image(self.positionx_5_6, self.positiony_5_6, image=self.image_image_6)
        # canvas.create_image(644.0, 560.0, image=self.image_image_6)

        # self.image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
        image_image_7_raw = Image.open(str(relative_to_assets("image_7.png")))
        image_image_7_width= int(self.background_image.width()*28/self.num_columnas)
        image_image_7_height= int(self.background_image.height()*4/self.num_filas)
        image_image_7_new_size = ImageOps.contain(image_image_7_raw,(image_image_7_width,image_image_7_height))
        self.image_image_7 = ImageTk.PhotoImage(image_image_7_new_size)
        three_buttons_image_x = self.background_image.width()*30/self.num_columnas
        three_buttons_image_y = self.background_image.height()*11/self.num_filas
        canvas.create_image(three_buttons_image_x, three_buttons_image_y, image=self.image_image_7)
        # canvas.create_image(642.0, 289.0, image=self.image_image_7)

        # button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_image_2_raw = Image.open(str(relative_to_assets("button_2.png")))
        button_2_width=int(self.background_image.width()*8/self.num_columnas)
        button_2_height=int(self.background_image.height()*3/self.num_filas)
        button_image_2_new_size = ImageOps.contain(button_image_2_raw,(button_2_width,button_2_height))
        button_image_2 = ImageTk.PhotoImage(button_image_2_new_size)
        button_2 = Button(
            command=lambda: agregar_prestamo(self),
            image=button_image_2,
            borderwidth=0,
            cursor="hand2",
            highlightthickness=0,
            relief="flat"
        )
        # button_2.place(x=374.0, y=270.0, width=146.0, height=38.0)
        button_2.place(anchor="center",x=self.background_image.width()*21/self.num_columnas, y=three_buttons_image_y, width=button_image_2.width(), height=button_image_2.height())

        # button_image_hover_2 = PhotoImage(file=relative_to_assets("button_hover_2.png"))
        button_image_2_hover_raw = Image.open(str(relative_to_assets("button_hover_2.png")))
        button_image_2_hover_new_size = ImageOps.contain(button_image_2_hover_raw,(button_2_width,button_2_height))
        button_image_hover_2 = ImageTk.PhotoImage(button_image_2_hover_new_size)
        button_2.bind('<Enter>', lambda e: button_2.config(image=button_image_hover_2))
        button_2.bind('<Leave>', lambda e: button_2.config(image=button_image_2))

        # button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        button_image_3_raw = Image.open(str(relative_to_assets("button_3.png")))
        button_3_width=int(self.background_image.width()*8/self.num_columnas)
        button_3_height=int(self.background_image.height()*3/self.num_filas)
        button_image_3_new_size = ImageOps.contain(button_image_3_raw,(button_3_width,button_3_height))
        button_image_3 = ImageTk.PhotoImage(button_image_3_new_size)
        button_3 = Button(
            command=lambda: mostrar_TEG(self),
            image=button_image_3,
            borderwidth=0,
            cursor="hand2",
            highlightthickness=0,
            relief="flat"
        )
        # button_3.place(x=570.0, y=270.0, width=146.0, height=38.0)
        button_3.place(anchor="center",x=self.background_image.width()*30/self.num_columnas, y=three_buttons_image_y, width=button_image_3.width(), height=button_image_3.height())

        # button_image_hover_3 = PhotoImage(file=relative_to_assets("button_hover_3.png"))
        button_image_3_hover_raw = Image.open(str(relative_to_assets("button_hover_3.png")))
        button_image_3_hover_new_size = ImageOps.contain(button_image_3_hover_raw,(button_3_width,button_3_height))
        button_image_hover_3 = ImageTk.PhotoImage(button_image_3_hover_new_size)
        button_3.bind('<Enter>', lambda e: button_3.config(image=button_image_hover_3))
        button_3.bind('<Leave>', lambda e: button_3.config(image=button_image_3))

        # button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        button_image_4_raw = Image.open(str(relative_to_assets("button_4.png")))
        button_4_width=int(self.background_image.width()*8/self.num_columnas)
        button_4_height=int(self.background_image.height()*3/self.num_filas)
        button_image_4_new_size = ImageOps.contain(button_image_4_raw,(button_4_width,button_4_height))
        button_image_4 = ImageTk.PhotoImage(button_image_4_new_size)
        self.table:ttk.Treeview
        button_4 = Button(
            command=lambda: mostrar_tabla(self),
            image=button_image_4,
            borderwidth=0,
            cursor="hand2",
            highlightthickness=0,
            relief="flat"
        )
        # button_4.place(x=766.0, y=270.0, width=146.0, height=38.0)
        button_4.place(anchor="center",x=self.background_image.width()*39/self.num_columnas, y=three_buttons_image_y, width=button_image_4.width(), height=button_image_4.height())

        # button_image_hover_4 = PhotoImage(file=relative_to_assets("button_hover_4.png"))
        button_image_4_hover_raw = Image.open(str(relative_to_assets("button_hover_4.png")))
        button_image_4_hover_new_size = ImageOps.contain(button_image_4_hover_raw,(button_4_width,button_4_height))
        button_image_hover_4 = ImageTk.PhotoImage(button_image_4_hover_new_size)
        button_4.bind('<Enter>', lambda e: button_4.config(image=button_image_hover_4))
        button_4.bind('<Leave>', lambda e: button_4.config(image=button_image_4))

def mostrar_tabla(window:create_biblioteca_user_window):
    data = obtener_libros()

    if not data:
        messagebox.showinfo("No hay Datos Existentes", "Actualmente la tabla está vacia en la Base de Datos...")
        return

    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview.Heading", font=("Arial", 9, "bold"), background="#dcdcdc")
    style.configure("Treeview.Row", font=("Calibri", 12))
    style.configure("Treeview", background="#dcdcdc")

    # table_frame = ttk.Frame(window, padding=1, borderwidth=0.1, relief=tk.FLAT)
    # table_frame.place(x=window.positionx_5_6 , y=window.positiony_5_6, width=window.image_image_5.width(), height=window.image_image_5.height())

    column_names = ['id', 'titulo', 'autor', 'año_publicacion', 'cantidad', 'edicion','area_de_conocimiento']

    window.table = ttk.Treeview(window, columns=column_names, show="headings")

    for col in column_names:
        window.table.heading(col, text=col.upper(), anchor=tk.CENTER)
        window.table.column(col, width=get_max_width(data, column_names.index(col)), anchor=tk.CENTER)

    for row in data:
        row = tuple(row)
        window.table.insert("", tk.END, values=row)

    window.table.tag_configure("evenrow", background="#f5f5f5")
    window.table.tag_configure("oddrow", background="#fff")
    window.table.tag_configure("headings", background="#333", foreground="#fff")

    # table.pack(fill=tk.BOTH, expand=True)
    window.table.place(anchor="center",x=window.positionx_5_6 , y=window.positiony_5_6, width=window.image_image_5.width()-20, height=window.image_image_5.height()-20)

if __name__ == "__main__":
    create_biblioteca_user_window()