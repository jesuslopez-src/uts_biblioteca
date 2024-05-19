from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from database import create_tables, insert_user
from seleccion import SeleccionWindow  
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__))
ASSETS_PATH = os.path.join(OUTPUT_PATH, "assets", "inicio", "assets", "frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class InicioWindow(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1280x810")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=810,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        canvas.create_image(640.0, 407.0, image=image_image_1)

        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            command=self.abrir_seleccion,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_1.place(x=432.0, y=696.0, width=368.0, height=66.0)

        button_image_hover_1 = PhotoImage(file=relative_to_assets("button_hover_1.png"))
        button_1.bind('<Enter>', lambda e: button_1.config(image=button_image_hover_1))
        button_1.bind('<Leave>', lambda e: button_1.config(image=button_image_1))

        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        canvas.create_image(640.0, 114.0, image=image_image_2)

        background_image = PhotoImage(file=relative_to_assets("image_1.png"))
        canvas.create_image(0, 0, anchor="nw", image=background_image)

        self.image_references = [image_image_1, button_image_1, button_image_hover_1, image_image_2, background_image]

    def abrir_seleccion(self):
        create_tables()
        insert_user()
        self.destroy()
        seleccion_window = SeleccionWindow()  
        seleccion_window.mainloop()  