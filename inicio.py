from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from database import create_tables, insert_user
from seleccion import SeleccionWindow
from PIL import ImageTk, Image, ImageOps
from screeninfo import get_monitors

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__))
print(OUTPUT_PATH)
ASSETS_PATH = os.path.join(OUTPUT_PATH, "assets", "inicio", "assets", "frame0")
print(ASSETS_PATH)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class InicioWindow(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.monitors = get_monitors()
        # self.geometry(f"{self.monitors[1].width}x{self.monitors[1].height}")
        self.configure(bg="#FFFFFF")
        self.resizable(True, True)
        self.create_widgets()

    def create_widgets(self):
        # background_image = PhotoImage(file=relative_to_assets("image_1.png"))
        # imagen_mitad = background_image.subsample(2,2)

        imagen_raw = Image.open(str(relative_to_assets("image_1.png")))
        imagen = ImageOps.contain(imagen_raw,(self.monitors[1].width,self.monitors[1].height))
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

        
      
        # width, height = imagen.size
        # imagen = imagen.resize((int(width/2), int(height/2)))

        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        # imagen_mitad = image_image_1.subsample(2,2)
        # canvas.create_image(0, 0, image=imagen_mitad,anchor="nw")

        # button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_image_1_raw = Image.open(str(relative_to_assets("button_1.png")))
        button_image_1_new_size = ImageOps.contain(button_image_1_raw,(int(self.monitors[1].width/4),int(self.monitors[1].height/5)))
        button_image_1 = ImageTk.PhotoImage(button_image_1_new_size)
        button_1 = Button(
            self,
            command=self.abrir_seleccion,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        print(self.winfo_height()/2)
        print(self.winfo_width()/2)
        button_1.place(x=background_image.height()/2.0, y=background_image.width()/2.0, width=button_image_1.width(), height=button_image_1.height())
        # button_1.pack()

        button_image_hover_1 = PhotoImage(file=relative_to_assets("button_hover_1.png"))
        button_1.bind('<Enter>', lambda e: button_1.config(image=button_image_hover_1))
        button_1.bind('<Leave>', lambda e: button_1.config(image=button_image_1))

        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        canvas.create_image(640.0, 114.0, image=image_image_2)
        
        canvas.create_image(0, 0, anchor="nw", image=background_image)

        self.image_references = [background_image, button_image_1, button_image_hover_1, image_image_2]


    def abrir_seleccion(self):
        create_tables()
        insert_user()
        self.destroy()
        seleccion_window = SeleccionWindow()  
        seleccion_window.mainloop()  