
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import tkinter as tk
import sqlite3
import os
import sys
import subprocess

OUTPUT_PATH = os.path.join(os.path.dirname(__file__))
ASSETS_PATH = os.path.join(OUTPUT_PATH, "assets", "frame0")

ruta_directorio_actual = os.getcwd()

ruta_login = os.path.join(ruta_directorio_actual, "Inicio de Sesion", "login.py")

ruta_registro = os.path.join(ruta_directorio_actual, "Registro Estudiante", "registro.py")

ruta_registroadmin = os.path.join(ruta_directorio_actual, "Registro Admin", "registro_admin.py")

ruta_volver = os.path.join(ruta_directorio_actual, "Inicio", "inicio.py")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

conn = sqlite3.connect('biblioteca.db')
c = conn.cursor()


window = Tk()

window.geometry("1280x810")
window.configure(bg = "#FFFFFF")

def abrir_login():
    
  window.destroy()

  subprocess.call(["python", ruta_login])

def abrir_registro():
    
  window.destroy()

  subprocess.call(["python", ruta_registro])
  
def abrir_registroadmin():
    
  window.destroy()

  subprocess.call(["python", ruta_registroadmin])

def abrir_volver():
    
  window.destroy()

  subprocess.call(["python", ruta_volver])


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

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    command = abrir_volver,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_1.place(
    x=57.0,
    y=36.0,
    width=146.0,
    height=36.150001525878906
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
    command = abrir_login,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_2.place(
    x=116.0,
    y=616.0,
    width=205.0,
    height=57.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    command = abrir_login,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_3.place(
    x=958.0,
    y=615.0,
    width=205.0,
    height=58.0
)

button_image_hover_3 = PhotoImage(
    file=relative_to_assets("button_hover_2.png"))

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
    command = abrir_registroadmin,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_4.place(
    x=957.0,
    y=691.0,
    width=205.0,
    height=58.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    command = abrir_registro,
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_5.place(
    x=116.0,
    y=695.0,
    width=205.0,
    height=57.0
)

button_image_hover_4 = PhotoImage(
    file=relative_to_assets("button_hover_3.png"))

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


button_image_hover_2 = PhotoImage(
    file=relative_to_assets("button_hover_4.png"))

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


image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    226.0,
    404.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1072.0,
    420.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    226.0,
    590.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    1061.0,
    590.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    226.0,
    164.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    1072.0,
    164.0,
    image=image_image_7
)
window.resizable(False, False)
window.mainloop()
