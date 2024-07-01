from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, ttk, messagebox
import customtkinter as ctk
from biblioteca_functions import agregar_fila, editar_fila, eliminar_fila, mostrar_TEG, mostrar_tabla_libros

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "biblioteca_adm" / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def cerrarsesion(window):
    window.destroy()
    from seleccion import SeleccionWindow
    seleccion_window = SeleccionWindow()
    seleccion_window.mainloop()
    
def prestamos(window):
    window.destroy()
    from bibli_prestamos import create_biblioteca_prestamos_window
    prestamos_window = create_biblioteca_prestamos_window()
    prestamos_window.mainloop()
    
def registroadmin(window):
    window.destroy()
    from registro_adm import RegistroAdminWindow
    registro_admin_window = RegistroAdminWindow()
    registro_admin_window.mainloop()

def create_biblioteca_admin_window():

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
    640.0,
    216.0,
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
    578.0,
    image=image_image_4
)

 image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
 image_5 = canvas.create_image(
    763.0,
    323.0,
    image=image_image_5
)

 image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
 image_6 = canvas.create_image(
    769.0,
    565.0,
    image=image_image_6
)

 image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
 image_7 = canvas.create_image(
    769.0,
    565.0,
    image=image_image_7
)

 button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
 button_2 = Button(
    command=lambda: agregar_fila(window, search_entry, table),
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
 button_2.place(
    x=108.0,
    y=463.0,
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
    command=lambda: prestamos(window),
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
 button_3.place(
    x=589.0,
    y=304.0,
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
    command=lambda: mostrar_TEG(window, search_entry, table),
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
 button_4.place(
    x=787.0,
    y=304.0,
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
 
 search_entry = Entry(
        window,
        bd=0,
        bg="#BDBDBD",
        fg="#000716",
        highlightthickness=0
    )
 search_entry.place(x=303.0, y=310, width=178.0, height=25.0)
 
 entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
 canvas.create_image(390.0, 320, image=entry_image_1)


 button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
 button_5 = Button(
    command=lambda: edit_row(window, table),
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
 button_5.place(
    x=108.0,
    y=527.0,
    width=146.0,
    height=38.0
)

 button_image_hover_5 = PhotoImage(
    file=relative_to_assets("button_hover_5.png"))
 
 # Init tabla
 table = ttk.Treeview(window, columns=['id', 'nombre', 'autor', 'año', 'cantidad', 'tipo'], show="headings")
 table = mostrar_tabla_libros(window, search_entry, table)

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
 
 def edit_row(window, table):
        selected_values = get_selected_row(table)
        if selected_values:
            editar_fila(window, selected_values, table)


 button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
 button_6 = Button(
    command=lambda: eliminar_fila(table),
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
 button_6.place(
    x=108.0,
    y=591.0,
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
 
 def get_selected_row(table):
        selected_items = table.selection()
        if selected_items:
            item = selected_items[0]
            values = table.item(item, "values")
            return values
        else:
            messagebox.showwarning("Advertencia", "No has seleccionado ningún libro.")
            return None


 button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
 button_7 = Button(
    command=lambda: registroadmin(window), 
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
 button_7.place(
    x=108.0,
    y=655.0,
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


 image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
 image_8 = canvas.create_image(
    639.0,
    216.0,
    image=image_image_8
)
 window.resizable(False, False)
 window.mainloop()
