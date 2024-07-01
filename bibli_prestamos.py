from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, ttk, messagebox
import customtkinter as ctk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from biblioteca_functions import mostrar_tabla_prestamos, eliminar_prestamos


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "prestamos" / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def volveradmin(window):
    window.destroy()
    from biblioteca_adm import create_biblioteca_admin_window 
    admin_window = create_biblioteca_admin_window() 
    admin_window.mainloop()

def create_biblioteca_prestamos_window():
    
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
    639.0,
    244.0,
    image=image_image_2
)

 button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
 button_1 = Button(
     command=lambda: volveradmin(window),
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
    514.0,
    image=image_image_4
)

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

 button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
 button_2 = Button(
     command=lambda: eliminar_prestamos(table),
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
 
 table = ttk.Treeview(window, columns=['id', 'nombre', 'autor', 'año', 'cantidad', 'tipo'], show="headings")
 table = mostrar_tabla_prestamos(window, table)
    
 button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
 button_3.place(
    x=108.0,
    y=527.0,
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


 image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
 image_7 = canvas.create_image(
    640.0,
    244.0,
    image=image_image_7
)
 window.resizable(False, False)
 window.mainloop()
