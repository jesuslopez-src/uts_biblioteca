from pathlib import Path
from tkinter import Tk, Canvas, Button
from database import insert_user
from seleccion import SeleccionWindow
from PIL import ImageTk, Image, ImageOps
from monitors import detect_monitor
from screeninfo import get_monitors

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__))
ASSETS_PATH = os.path.join(OUTPUT_PATH, "assets", "inicio", "assets", "frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class InicioWindow(Tk):
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
        self.create_widgets()
        

    def create_widgets(self):

        imagen_raw = Image.open(str(relative_to_assets("image_1.png")))
        imagen = ImageOps.contain(imagen_raw,(self.monitor_width,self.monitor_height))
        background_image = ImageTk.PhotoImage(imagen)
        self.geometry(f"{background_image.width()}x{background_image.height()}")

        print(background_image.height())
        print(background_image.width())
        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=background_image.height(),
            width=background_image.width(),
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        button_image_1_raw = Image.open(str(relative_to_assets("button_1.png")))
        button_image_1_new_size = ImageOps.contain(button_image_1_raw,(int(background_image.width()/4),int(background_image.height()/5)))
        button_image_1 = ImageTk.PhotoImage(button_image_1_new_size)
        button_1 = Button(
            self,
            command=self.abrir_seleccion,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        print(background_image.height()/2.0)
        print(background_image.width()/2.0)
        button_1.place(anchor="center",x=background_image.width()/2.0, y=background_image.height()*10/11.0, width=button_image_1.width(), height=button_image_1.height())

        button_hover_image_raw = Image.open(str(relative_to_assets("button_hover_1.png")))
        button_hover_image_new_size = ImageOps.contain(button_hover_image_raw,(int(background_image.width()/4),int(background_image.height()/5)))
        button_image_hover_1 = ImageTk.PhotoImage(button_hover_image_new_size)
        
        button_1.bind('<Enter>', lambda e: button_1.config(image=button_image_hover_1))
        button_1.bind('<Leave>', lambda e: button_1.config(image=button_image_1))
        button_1.focus_set()
        button_1.bind('<Return>',lambda e: self.abrir_seleccion())

        # image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        # canvas.create_image(640.0, 114.0, image=image_image_2)
        
        canvas.create_image(0, 0, anchor="nw", image=background_image)

        self.image_references = [background_image, button_image_1, button_image_hover_1]

    def abrir_seleccion(self):
        insert_user()
        self.destroy()
        seleccion_window = SeleccionWindow()  
        seleccion_window.mainloop()