# login.py
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from PIL import ImageTk, Image, ImageOps
from monitors import detect_monitor
from screeninfo import get_monitors
from database import login_admin


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "login" / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class LoginAdmin(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.monitors = get_monitors()
        self.monitor = detect_monitor()
        self.monitor_width=self.monitor.width
        self.monitor_height=self.monitor.height
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

        entry_image_1_raw = Image.open(str(relative_to_assets("entry_1.png")))
        entry_image_1_width= int(self.background_image.width()*11/self.num_columnas)
        entry_image_1_height= int(self.background_image.height()*4/self.num_filas)
        entry_image_1_new_size = ImageOps.contain(entry_image_1_raw,(entry_image_1_width,entry_image_1_height))
        self.entry_image_1 = ImageTk.PhotoImage(entry_image_1_new_size)
        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#BDBDBD",
            fg="#000716",
            highlightthickness=0
        )
        entry_1_x = self.background_image.width()*30/self.num_columnas
        entry_1_y = self.background_image.height()*14/self.num_filas
        canvas.create_image(entry_1_x, entry_1_y, image=self.entry_image_1)
        self.entry_1.place(anchor="center",x=entry_1_x, y=entry_1_y, width=self.entry_image_1.width()-20, height=self.entry_image_1.height()-5)

        # entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        # canvas.create_image(638.0, 438.5, image=entry_image_2)
        entry_image_2_raw = Image.open(str(relative_to_assets("entry_2.png")))
        entry_image_2_new_size = ImageOps.contain(entry_image_2_raw,(entry_image_1_width,entry_image_1_height))
        self.entry_image_2 = ImageTk.PhotoImage(entry_image_2_new_size)
        self.entry_2 = Entry(
            self,
            show="*",
            bd=0,
            bg="#BDBDBD",
            fg="#000716",
            highlightthickness=0
        )
        # self.entry_2.place(x=548.0, y=423.0, width=178.0, height=35.0)
        entry_2_x = self.background_image.width()*30/self.num_columnas
        entry_2_y = self.background_image.height()*18/self.num_filas
        canvas.create_image(entry_2_x, entry_2_y, image=self.entry_image_2)
        self.entry_2.place(anchor="center",x=entry_2_x, y=entry_2_y, width=self.entry_image_2.width()-20, height=self.entry_image_2.height()-5)

        #entry PIN
        entry_image_3_raw = Image.open(str(relative_to_assets("entry_2.png")))
        entry_image_3_new_size = ImageOps.contain(entry_image_3_raw,(entry_image_1_width,entry_image_1_height))
        self.entry_image_3 = ImageTk.PhotoImage(entry_image_3_new_size)
        self.entry_3 = Entry(
            self,
            show="*",
            bd=0,
            bg="#BDBDBD",
            fg="#000716",
            highlightthickness=0
        )
        entry_3_x = self.background_image.width()*30/self.num_columnas
        entry_3_y = self.background_image.height()*22/self.num_filas
        canvas.create_image(entry_3_x, entry_3_y, image=self.entry_image_3)
        self.entry_3.place(anchor="center",x=entry_3_x, y=entry_3_y, width=self.entry_image_3.width()-20, height=self.entry_image_3.height()-5)
        
        
        # botón regresar
        button_1_width=int(self.background_image.width()*7/self.num_columnas)
        button_1_height=int(self.background_image.height()*3/self.num_filas)
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
        button_1.place(anchor="center",x=self.background_image.width()*6/self.num_columnas, y=self.background_image.height()*2/self.num_filas, width=button_image_1.width(), height=button_image_1.height())

        button_image_hover_1_raw = Image.open(str(relative_to_assets("button_hover_1.png")))
        button_image_hover_1_new_size = ImageOps.contain(button_image_hover_1_raw,(button_1_width,button_1_height))
        button_image_hover_1 = ImageTk.PhotoImage(button_image_hover_1_new_size)
        button_1.bind('<Enter>', lambda e: button_1.config(image=button_image_hover_1))
        button_1.bind('<Leave>', lambda e: button_1.config(image=button_image_1))

        #boton iniciar sesion
        button_image_2_raw = Image.open(str(relative_to_assets("button_2.png")))
        button_2_width=int(self.background_image.width()*8/self.num_columnas)
        button_2_height=int(self.background_image.height()*4/self.num_filas)
        button_image_2_new_size = ImageOps.contain(button_image_2_raw,(button_2_width,button_2_height))
        button_image_2 = ImageTk.PhotoImage(button_image_2_new_size)
        button_2 = Button(
            self,
            command=self.login,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        
        button_2.place(anchor="center",x=self.background_image.width()*30/self.num_columnas, y=self.background_image.height()*25/self.num_filas, width=button_image_2.width(), height=button_image_2.height())

        button_image_2_hover_raw = Image.open(str(relative_to_assets("button_hover_2.png")))
        button_image_2_hover_new_size = ImageOps.contain(button_image_2_hover_raw,(button_2_width,button_2_height))
        button_image_hover_2 = ImageTk.PhotoImage(button_image_2_hover_new_size)
        button_2.bind('<Enter>', lambda e: button_2.config(image=button_image_hover_2))
        button_2.bind('<Leave>', lambda e: button_2.config(image=button_image_2))
        
        #imagen usuario
        image_image_2_raw = Image.open(str(relative_to_assets("image_2.png")))
        image_image_2_width= int(self.background_image.width()*5/self.num_columnas)
        image_image_2_height= int(self.background_image.height()/self.num_filas)
        image_image_2_new_size = ImageOps.contain(image_image_2_raw,(image_image_2_width,image_image_2_height))
        self.image_image_2 = ImageTk.PhotoImage(image_image_2_new_size)
        canvas.create_image(self.background_image.width()*25/self.num_columnas, self.background_image.height()*13/self.num_filas, image=self.image_image_2,anchor='sw')
        # image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        # canvas.create_image(569.0, 331.0, image=image_image_2)

        #imagen contraseña
        image_image_3_raw = Image.open(str(relative_to_assets("image_3.png")))
        image_image_3_width= int(self.background_image.width()*7/self.num_columnas)
        image_image_3_height= int(self.background_image.height()*5/self.num_filas)
        image_image_3_new_size = ImageOps.contain(image_image_3_raw,(image_image_3_width,image_image_3_height))
        self.image_image_3 = ImageTk.PhotoImage(image_image_3_new_size)
        canvas.create_image(self.background_image.width()*25/self.num_columnas, self.background_image.height()*17/self.num_filas, image=self.image_image_3,anchor='sw')
        # image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        # canvas.create_image(587.0, 403.0, image=image_image_3)


        # image PIN
        image_image_4_raw = Image.open(str(relative_to_assets("image_4.png")))
        image_image_4_width= int(self.background_image.width()*9/self.num_columnas)
        image_image_4_height= int(self.background_image.height()*8/self.num_filas)
        image_image_4_new_size = ImageOps.contain(image_image_4_raw,(image_image_4_width,image_image_4_height))
        self.image_image_4 = ImageTk.PhotoImage(image_image_4_new_size)
        canvas.create_image(self.background_image.width()*25/self.num_columnas, self.background_image.height()*21/self.num_filas,anchor="sw", image=self.image_image_4)
        
        # image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        # canvas.create_image(623.0, 475.0, image=image_image_4)

        #bienvenido a la biblioteca imagen
        image_image_5_raw = Image.open(str(relative_to_assets("image_5.png")))
        image_image_5_width= int(self.background_image.width()*23/self.num_columnas)
        image_image_5_height= int(self.background_image.height()*15/self.num_filas)
        image_image_5_new_size = ImageOps.contain(image_image_5_raw,(image_image_5_width,image_image_5_height))
        self.image_image_5 = ImageTk.PhotoImage(image_image_5_new_size)
        positionx_5_6 = self.background_image.width()*30/self.num_columnas
        positiony_5_6 = self.background_image.height()*9/self.num_filas
        canvas.create_image(positionx_5_6, positiony_5_6, image=self.image_image_5)

        self.image_references = [
            self.background_image, self.entry_image_1, self.entry_image_2,
            button_image_1, button_image_hover_1, button_image_2,
            button_image_hover_2, self.image_image_2, self.image_image_3,
            self.entry_image_3, self.image_image_4, self.image_image_5
        ]

    def login(self):
        usu_nom = self.entry_1.get()
        usu_pass = self.entry_2.get()
        admin_pin = self.entry_3.get()

        self.login_admin(usu_nom, usu_pass, admin_pin)


    def login_admin(self, usu_nom, usu_pass, admin_pin):
        user = login_admin(usu_nom, usu_pass, admin_pin)

        if user:
            self.destroy()
            print("Acceso a Admin Logrado con Exito")
            from biblioteca_adm import create_biblioteca_admin_window 

            admin_window = create_biblioteca_admin_window() 
            admin_window.mainloop()
        else:
            messagebox.showinfo(title="Error", message="Usuario, contraseña o pin de administrador incorrectos")

    def abrir_seleccion(self):
        self.destroy()
        print('hi')
        from seleccion import SeleccionWindow
        seleccion_window = SeleccionWindow()
        seleccion_window.mainloop()


if __name__ == "__main__":
    login_window = LoginAdmin()
    login_window.mainloop()