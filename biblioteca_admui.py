from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, ttk, messagebox
import customtkinter as ctk
from monitors import detect_monitor
from screeninfo import get_monitors
from PIL import ImageTk, Image, ImageOps
from utilities import crear_imagen
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
   monitor = detect_monitor()
   monitor_width=monitor.width
   monitor_height=monitor.height

   window.configure(bg = "#FFFFFF")
   window.title("Biblioteca UTS")
   window.resizable(False, False)
   num_columnas = 60
   num_filas = 28
   imagen_raw = Image.open(str(relative_to_assets("image_1.png")))
   imagen = ImageOps.contain(imagen_raw,(monitor_width,monitor_height))
   background_image = ImageTk.PhotoImage(imagen)
   window.geometry(f"{background_image.width()}x{background_image.height()}")
   
   canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height=background_image.height(),
    width=background_image.width(),
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
   
   canvas.place(x = 0, y = 0)
   canvas.create_image(0, 0, anchor="nw", image=background_image)

   # fondo del titulo central
   image_image_2 = crear_imagen(background_image,str(relative_to_assets("image_2.png")),33,4,num_columnas,num_filas)
   canvas.create_image(background_image.width()*30/num_columnas, background_image.height()*7/num_filas, image=image_image_2,anchor='center')

   # botón cerrar sesion
   button_1_width=int(background_image.width()*7/num_columnas)
   button_1_height=int(background_image.height()*3/num_filas)
   button_image_1_raw = Image.open(str(relative_to_assets("button_1.png")))
   button_image_1_new_size = ImageOps.contain(button_image_1_raw,(button_1_width,button_1_height))
   button_image_1 = ImageTk.PhotoImage(button_image_1_new_size)
   button_1 = Button(
      command=lambda: cerrarsesion(window),
      image=button_image_1,
      borderwidth=0,
      highlightthickness=0,
      relief="flat"
   )
   button_1.place(anchor="center",x=background_image.width()*6/num_columnas, y=background_image.height()*2/num_filas, width=button_image_1.width(), height=button_image_1.height())
   button_image_hover_1_raw = Image.open(str(relative_to_assets("button_hover_1.png")))
   button_image_hover_1_new_size = ImageOps.contain(button_image_hover_1_raw,(button_1_width,button_1_height))
   button_image_hover_1 = ImageTk.PhotoImage(button_image_hover_1_new_size)

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

   # figura de administrador
   image_image_3 = crear_imagen(background_image,str(relative_to_assets("image_3.png")),7,5,num_columnas,num_filas)
   canvas.create_image(background_image.width()*55/num_columnas, background_image.height()*10/num_filas, image=image_image_3,anchor='center')

   # fondo rojo botones de la izquierda
   image_image_4 = crear_imagen(background_image,str(relative_to_assets("image_4.png")),30,7,num_columnas,num_filas)
   canvas.create_image(background_image.width()*5/num_columnas, background_image.height()*15/num_filas, image=image_image_4,anchor='center')
  
   # cuadro rojo arriba de la tabla (fondo de los botones)
   image_image_5 = crear_imagen(background_image,str(relative_to_assets("image_5.png")),35,10,num_columnas,num_filas)
   canvas.create_image(background_image.width()*30/num_columnas, background_image.height()*11/num_filas, image=image_image_5,anchor='center')

   # cuadro rojo detras de la tabla
   tabla_image_x = background_image.width()*30/num_columnas
   tabla_image_y =  background_image.height()*19/num_filas
   image_image_6 = crear_imagen(background_image,str(relative_to_assets("image_6.png")),42,15,num_columnas,num_filas)
   canvas.create_image(tabla_image_x, tabla_image_y, image=image_image_6,anchor='center')

   # imagen para la tabla
   image_image_7 = crear_imagen(background_image,str(relative_to_assets("image_7.png")),42,15,num_columnas,num_filas)
   canvas.create_image(tabla_image_x, tabla_image_y, image=image_image_7,anchor='center')

   # boton agregar
   button_image_2 = crear_imagen(background_image,str(relative_to_assets("button_2.png")),7,3,num_columnas,num_filas)
   button_2 = Button(
      command=lambda: agregar_fila(window, search_entry, table),
      image=button_image_2,
      borderwidth=0,
      highlightthickness=0,
      relief="flat"
   )
   button_2.place(anchor="center",x=background_image.width()*5/num_columnas, y=background_image.height()*13/num_filas, width=button_image_2.width(), height=button_image_2.height())
   
   button_image_hover_2 = crear_imagen(background_image,str(relative_to_assets("button_hover_2.png")),7,3,num_columnas,num_filas)
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

   # boton prestamos
   button_image_3 = crear_imagen(background_image,str(relative_to_assets("button_3.png")),7,3,num_columnas,num_filas)
   button_3 = Button(
      command=lambda: prestamos(window),
      image=button_image_3,
      borderwidth=0,
      highlightthickness=0,
      relief="flat"
   )
   button_3.place(anchor="s",x=background_image.width()*30/num_columnas, y=background_image.height()*11/num_filas, width=button_image_3.width(), height=button_image_3.height())

   button_image_hover_3 = crear_imagen(background_image,str(relative_to_assets("button_hover_3.png")),7,3,num_columnas,num_filas)
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

   # boton TEG
   button_image_4 = crear_imagen(background_image,str(relative_to_assets("button_4.png")),7,3,num_columnas,num_filas)
   button_4 = Button(
      command=lambda: mostrar_TEG(window, search_entry, table),
      image=button_image_4,
      borderwidth=0,
      highlightthickness=0,
      relief="flat"
   )
   button_4.place(anchor="s",x=background_image.width()*39/num_columnas, y=background_image.height()*11/num_filas, width=button_image_4.width(), height=button_image_4.height())

   button_image_hover_4 = crear_imagen(background_image,str(relative_to_assets("button_hover_4.png")),7,3,num_columnas,num_filas)
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
   
   #input (entry) de busqueda
   search_entry = Entry(
         window,
         bd=0,
         bg="#BDBDBD",
         fg="#000716",
         highlightthickness=0
      )
   entry_image_1 = crear_imagen(background_image,str(relative_to_assets("entry_1.png")),9,6,num_columnas,num_filas)
   entry_x= background_image.width()*20/num_columnas
   entry_y=  background_image.height()*11/num_filas
   canvas.create_image(entry_x,entry_y, image=entry_image_1,anchor='s')
   search_entry.place(anchor="s",x=entry_x, y=entry_y, width=entry_image_1.width()-20, height=entry_image_1.height()-5)

   # boton de editar
   button_image_5 = crear_imagen(background_image,str(relative_to_assets("button_5.png")),7,3,num_columnas,num_filas)
   button_5 = Button(
      command=lambda: edit_row(window, table),
      image=button_image_5,
      borderwidth=0,
      highlightthickness=0,
      relief="flat"
   )
   button_5.place(anchor="center",
                  x=background_image.width()*5/num_columnas,
                  y=background_image.height()*15/num_filas,
                  width=button_image_5.width(), 
                  height=button_image_5.height())

   button_image_hover_5 = crear_imagen(background_image,str(relative_to_assets("button_hover_5.png")),7,3,num_columnas,num_filas)
   
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
   
   # Init tabla
   table = mostrar_tabla_libros(window, search_entry)
   table.place(anchor="center",
                  x=tabla_image_x,
                  y=tabla_image_y,
                  width=image_image_7.width()-16, 
                  height=image_image_7.height()-16)
   
   def edit_row(window, table):
         selected_values = get_selected_row(table)
         if selected_values:
               editar_fila(window, selected_values, table)


   # boton de eliminar
   button_image_6 = crear_imagen(background_image
                           ,str(relative_to_assets("button_6.png")),
                           7,
                           3,
                           num_columnas,
                           num_filas)
   button_6 = Button(
      command=lambda: eliminar_fila(table),
      image=button_image_6,
      borderwidth=0,
      highlightthickness=0,
      relief="flat"
   )
   button_6.place(anchor="center",
                  x=background_image.width()*5/num_columnas,
                  y=background_image.height()*17/num_filas,
                  width=button_image_6.width(), 
                  height=button_image_6.height())

   button_image_hover_6 = crear_imagen(background_image
                           ,str(relative_to_assets("button_hover_6.png")),
                           7,
                           3,
                           num_columnas,
                           num_filas)

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


   button_image_7 = crear_imagen(background_image
                           ,str(relative_to_assets("button_7.png")),
                           7,
                           3,
                           num_columnas,
                           num_filas)
   button_7 = Button(
      command=lambda: registroadmin(window), 
      image=button_image_7,
      borderwidth=0,
      highlightthickness=0,
      relief="flat"
   )
   button_7.place(anchor="center",
                  x=background_image.width()*55/num_columnas,
                  y=background_image.height()*13/num_filas,
                  width=button_image_7.width(), 
                  height=button_image_7.height())

   button_image_hover_7 = crear_imagen(background_image
                           ,str(relative_to_assets("button_hover_7.png")),
                           7,
                           3,
                           num_columnas,
                           num_filas)

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


   image_image_8 = crear_imagen(background_image
                           ,str(relative_to_assets("image_8.png")),
                           30,
                           5,
                           num_columnas,
                           num_filas)
   canvas.create_image(background_image.width()*30/num_columnas, 
                       background_image.height()*7/num_filas, 
                       image=image_image_8,anchor='center')
   
   window.resizable(False, False)
   window.mainloop()
