from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox, constants
from database import login_user
from PIL import ImageTk, Image, ImageOps
from monitors import detect_monitor
from screeninfo import get_monitors
from database import registrar_usuario


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "reguser" / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class RegistroEstudianteWindow(Tk):
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
        self.num_columnas = 30
        self.num_filas = 18
        self.create_widgets()

    def create_widgets(self):

        imagen_raw = Image.open(str(relative_to_assets("image_1.png")))
        imagen = ImageOps.contain(imagen_raw,(self.monitor_width,self.monitor_height))
        background_image = ImageTk.PhotoImage(imagen)
        self.geometry(f"{background_image.width()}x{background_image.height()}")

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

        # background_image = PhotoImage(file=relative_to_assets("image_1.png"))
        canvas.create_image(0, 0, anchor="nw", image=background_image)

        # entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_image_1_raw = Image.open(str(relative_to_assets("entry_1.png")))
        entry_image_1_width= int(background_image.width()*5/self.num_columnas)
        entry_image_1_height= int(background_image.height()*3/self.num_filas)
        entry_image_1_new_size = ImageOps.contain(entry_image_1_raw,(entry_image_1_width,entry_image_1_height))
        entry_image_1 = ImageTk.PhotoImage(entry_image_1_new_size)
        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#BDBDBD",
            fg="#000716",
            relief="flat",
            highlightthickness=0
        )
        # self.entry_1.place(x=550.0, y=351.0, width=178.0, height=35.0)
        entry_1_x = background_image.width()*15/self.num_columnas
        entry_1_y = background_image.height()*11/self.num_filas
        canvas.create_image(entry_1_x, entry_1_y, image=entry_image_1)
        self.entry_1.place(anchor="center",x=entry_1_x, y=entry_1_y, width=entry_image_1.width()-20, height=entry_image_1.height()-5)

        # entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_image_2_raw = Image.open(str(relative_to_assets("entry_2.png")))
        entry_image_2_width= int(background_image.width()*5/self.num_columnas)
        entry_image_2_height= int(background_image.height()*3/self.num_filas)
        entry_image_2_new_size = ImageOps.contain(entry_image_2_raw,(entry_image_2_width,entry_image_2_height))
        entry_image_2 = ImageTk.PhotoImage(entry_image_2_new_size)
        # canvas.create_image(638.0, 438.5, image=entry_image_2)
        self.entry_2 = Entry(
            self,
            show="*",
            bd=0,
            bg="#BDBDBD",
            fg="#000716",
            highlightthickness=0
        )
        # self.entry_2.place(x=548.0, y=423.0, width=178.0, height=35.0)
        entry_2_x = background_image.width()*15/self.num_columnas
        entry_2_y = background_image.height()*13/self.num_filas
        canvas.create_image(entry_2_x, entry_2_y, image=entry_image_2)
        self.entry_2.place(anchor="center",x=entry_2_x, y=entry_2_y, width=entry_image_2.width()-20, height=entry_image_2.height()-5)

        # botón regresar
        button_1_width=int(background_image.width()*3/self.num_columnas)
        button_1_height=int(background_image.height()*3/self.num_filas)
        button_image_1_raw = Image.open(str(relative_to_assets("button_1.png")))
        button_image_1_new_size = ImageOps.contain(button_image_1_raw,(button_1_width,button_1_height))
        button_image_1 = ImageTk.PhotoImage(button_image_1_new_size)
        button_1 = Button(
            self,
            command=self.abrir_seleccion,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        # button_1.place(x=60.0, y=51.0, width=146.0, height=34.0)
        button_1.place(anchor="center",x=background_image.width()*3/self.num_columnas, y=background_image.height()*1/self.num_filas, width=button_image_1.width(), height=button_image_1.height())

        button_image_hover_1_raw = Image.open(str(relative_to_assets("button_hover_1.png")))
        button_image_hover_1_new_size = ImageOps.contain(button_image_hover_1_raw,(button_1_width,button_1_height))
        button_image_hover_1 = ImageTk.PhotoImage(button_image_hover_1_new_size)
        button_1.bind('<Enter>', lambda e: button_1.config(image=button_image_hover_1))
        button_1.bind('<Leave>', lambda e: button_1.config(image=button_image_1))

        # botón iniciar sesión
        # button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_image_2_raw = Image.open(str(relative_to_assets("button_2.png")))
        button_2_width=int(background_image.width()*4/self.num_columnas)
        button_2_height=int(background_image.height()*3/self.num_filas)
        button_image_2_new_size = ImageOps.contain(button_image_2_raw,(button_2_width,button_2_height))
        button_image_2 = ImageTk.PhotoImage(button_image_2_new_size)
        button_2 = Button(
            self,
            command=self.registrar_estudiante,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        # button_2.place(x=565.0, y=572.0, width=146.0, height=38.0)
        button_2.place(anchor="center",x=background_image.width()*15/self.num_columnas, y=background_image.height()*15/self.num_filas, width=button_image_2.width(), height=button_image_2.height())

        # button_image_hover_2 = PhotoImage(file=relative_to_assets("button_hover_2.png"))
        button_image_2_hover_raw = Image.open(str(relative_to_assets("button_hover_2.png")))
        button_image_2_hover_new_size = ImageOps.contain(button_image_2_hover_raw,(button_2_width,button_2_height))
        button_image_hover_2 = ImageTk.PhotoImage(button_image_2_hover_new_size)
        button_2.bind('<Enter>', lambda e: button_2.config(image=button_image_hover_2))
        button_2.bind('<Leave>', lambda e: button_2.config(image=button_image_2))

        # image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_image_2_raw = Image.open(str(relative_to_assets("image_2.png")))
        image_image_2_width= int(background_image.width()*2/self.num_columnas)
        image_image_2_height= int(background_image.height()/self.num_filas)
        image_image_2_new_size = ImageOps.contain(image_image_2_raw,(image_image_2_width,image_image_2_height))
        image_image_2 = ImageTk.PhotoImage(image_image_2_new_size)
        canvas.create_image(background_image.width()*14/self.num_columnas, background_image.height()*10/self.num_filas, image=image_image_2,anchor=constants.N)
        # canvas.create_image(569.0, 331.0, image=image_image_2)

        # image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        image_image_3_raw = Image.open(str(relative_to_assets("image_3.png")))
        image_image_3_width= int(background_image.width()*3/self.num_columnas)
        image_image_3_height= int(background_image.height()/self.num_filas)
        image_image_3_new_size = ImageOps.contain(image_image_3_raw,(image_image_3_width,image_image_3_height))
        image_image_3 = ImageTk.PhotoImage(image_image_3_new_size)
        canvas.create_image(background_image.width()*14/self.num_columnas, background_image.height()*12/self.num_filas, image=image_image_3,anchor=constants.N)
        # canvas.create_image(587.0, 403.0, image=image_image_3)

        # image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        image_image_4_raw = Image.open(str(relative_to_assets("image_4.png")))
        image_image_4_width= int(background_image.width()*15/self.num_columnas)
        image_image_4_height= int(background_image.height()*5/self.num_filas)
        image_image_4_new_size = ImageOps.contain(image_image_4_raw,(image_image_4_width,image_image_4_height))
        image_image_4 = ImageTk.PhotoImage(image_image_4_new_size)
        canvas.create_image(background_image.width()*15/self.num_columnas, background_image.height()*6/self.num_filas, image=image_image_4)

        self.image_references = [
            background_image, entry_image_1, entry_image_2,
            button_image_1, button_image_hover_1, button_image_2,
            button_image_hover_2, image_image_2, image_image_3,
            image_image_4
        ]

    def registrar_estudiante(self):
        usu_nom = self.entry_1.get()
        usu_pass = self.entry_2.get()

        registrar_usuario(usu_nom, usu_pass)

        self.entry_1.delete(0, 'end')
        self.entry_2.delete(0, 'end')

        messagebox.showinfo("Registro Exitoso", "Usuario registrado exitosamente")

    def abrir_seleccion(self):
        self.destroy()
        from seleccion import SeleccionWindow
        seleccion_window = SeleccionWindow()
        seleccion_window.mainloop()

if __name__ == "__main__":
    registro_estudiante_window = RegistroEstudianteWindow()
    registro_estudiante_window.mainloop()