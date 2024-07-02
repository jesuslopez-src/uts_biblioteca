from pathlib import Path
from tkinter import Tk, Canvas, Button
from loginadm import LoginAdmin
from login import LoginWindow
from registro_adm import RegistroAdminWindow
from registro_user import RegistroEstudianteWindow
from PIL import ImageTk, Image, ImageOps
from monitors import detect_monitor
from screeninfo import get_monitors


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "seleccion" / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class SeleccionWindow(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.monitors = get_monitors()
        self.monitor = detect_monitor()
        self.monitor_width=self.monitor.width
        self.monitor_height=self.monitor.height
        # self.monitor_width=self.monitors[0].width
        # self.monitor_height=self.monitors[0].height
        self.configure(bg="#FFFFFF")
        self.title("El Sistema Biblioteca")
        self.resizable(False, False)
        self.num_columnas = 20
        self.num_filas = 12
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

        canvas.create_image(0, 0, anchor="nw", image=background_image)

        # botón regresar
        button_1_width=int(background_image.width()*2/self.num_columnas)
        button_1_height=int(background_image.height()*2/self.num_filas)
        button_image_1_raw = Image.open(str(relative_to_assets("button_1.png")))
        button_image_1_new_size = ImageOps.contain(button_image_1_raw,(button_1_width,button_1_height))
        button_image_1 = ImageTk.PhotoImage(button_image_1_new_size)
        button_1 = Button(
            self,
            command=self.abrir_volver,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_1.place(anchor="center",x=background_image.width()*2/self.num_columnas, y=background_image.height()*1/self.num_filas, width=button_image_1.width(), height=button_image_1.height())

        button_image_hover_1_raw = Image.open(str(relative_to_assets("button_hover_1.png")))
        button_image_hover_1_new_size = ImageOps.contain(button_image_hover_1_raw,(button_1_width,button_1_height))
        button_image_hover_1 = ImageTk.PhotoImage(button_image_hover_1_new_size)
        button_1.bind('<Enter>', lambda e: button_1.config(image=button_image_hover_1))
        button_1.bind('<Leave>', lambda e: button_1.config(image=button_image_1))

        # COSAS DEL ESTUDIANTE
        # botón login estudiante
        button_image_2_raw = Image.open(str(relative_to_assets("button_2.png")))
        button_2_width= int(background_image.width()*3/self.num_columnas)
        button_2_height= int(background_image.height()*2/self.num_filas)
        button_image_2_new_size = ImageOps.contain(button_image_2_raw,(button_2_width,button_2_height))
        button_image_2 = ImageTk.PhotoImage(button_image_2_new_size)
        button_2 = Button(
            self,
            command=self.abrir_login,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_2.place(anchor="center",x=background_image.width()*5/self.num_columnas, y=background_image.height()*9/self.num_filas, width=button_image_2.width(), height=button_image_2.height())

        # button_image_hover_2 = PhotoImage(file=relative_to_assets("button_hover_3.png"))
        button_image_hover_2_raw = Image.open(str(relative_to_assets("button_hover_3.png")))
        button_image_hover_2_new_size = ImageOps.contain(button_image_hover_2_raw,(button_2_width,button_2_height))
        button_image_hover_2 = ImageTk.PhotoImage(button_image_hover_2_new_size)
        button_2.bind('<Enter>', lambda e: button_2.config(image=button_image_hover_2))
        button_2.bind('<Leave>', lambda e: button_2.config(image=button_image_2))

        # botón registrar estudiante
        # button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        button_image_4_raw = Image.open(str(relative_to_assets("button_4.png")))
        button_4_width= int(background_image.width()*3/self.num_columnas)
        button_4_height= int(background_image.height()*2/self.num_filas)
        button_image_4_new_size = ImageOps.contain(button_image_4_raw,(button_4_width,button_4_height))
        button_image_4 = ImageTk.PhotoImage(button_image_4_new_size)
        button_4 = Button(
            self,
            command=self.abrir_registro,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_4.place(anchor="center",x=background_image.width()*5/self.num_columnas, y=background_image.height()*10/self.num_filas, width=button_image_4.width(), height=button_image_4.height())
        # button_4.place(x=116.0, y=695.0, width=205.0, height=57.0)

        # button_image_hover_4 = PhotoImage(file=relative_to_assets("button_hover_4.png"))
        button_image_hover_4_raw = Image.open(str(relative_to_assets("button_hover_4.png")))
        button_image_hover_4_new_size = ImageOps.contain(button_image_hover_4_raw,(button_4_width,button_4_height))
        button_image_hover_4 = ImageTk.PhotoImage(button_image_hover_4_new_size)
        button_4.bind('<Enter>', lambda e: button_4.config(image=button_image_hover_4))
        button_4.bind('<Leave>', lambda e: button_4.config(image=button_image_4))

        # image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_image_2_raw = Image.open(str(relative_to_assets("image_2.png")))
        image_image_2_width= int(background_image.width()*5/self.num_columnas)
        image_image_2_height= int(background_image.height()*4/self.num_filas)
        image_image_2_new_size = ImageOps.contain(image_image_2_raw,(image_image_2_width,image_image_2_height))
        image_image_2 = ImageTk.PhotoImage(image_image_2_new_size)
        canvas.create_image(background_image.width()*5/self.num_columnas, background_image.height()*6/self.num_filas, image=image_image_2)
        
        # image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        # canvas.create_image(226.0, 590.0, image=image_image_4)
        image_image_4_raw = Image.open(str(relative_to_assets("image_4.png")))
        image_image_4_width= int(background_image.width()*5/self.num_columnas)
        image_image_4_height= int(background_image.height()*4/self.num_filas)
        image_image_4_new_size = ImageOps.contain(image_image_4_raw,(image_image_4_width,image_image_4_height))
        image_image_4 = ImageTk.PhotoImage(image_image_4_new_size)
        canvas.create_image(background_image.width()*5/self.num_columnas, background_image.height()*8/self.num_filas, image=image_image_4)
        
        # image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        # canvas.create_image(226.0, 164.0, image=image_image_6)
        image_image_6_raw = Image.open(str(relative_to_assets("image_6.png")))
        image_image_6_width= int(background_image.width()*4/self.num_columnas)
        image_image_6_height= int(background_image.height()*4/self.num_filas)
        image_image_6_new_size = ImageOps.contain(image_image_6_raw,(image_image_6_width,image_image_6_height))
        image_image_6 = ImageTk.PhotoImage(image_image_6_new_size)
        canvas.create_image(background_image.width()*5/self.num_columnas, background_image.height()*3/self.num_filas, image=image_image_6)
        
        
        # COSAS DEL ADMINISTRADOR
        # button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        button_image_3_raw = Image.open(str(relative_to_assets("button_3.png")))
        button_3_width= int(background_image.width()*3/self.num_columnas)
        button_3_height= int(background_image.height()*2/self.num_filas)
        button_image_3_new_size = ImageOps.contain(button_image_3_raw,(button_3_width,button_3_height))
        button_image_3 = ImageTk.PhotoImage(button_image_3_new_size)
        button_3 = Button(
            self,
            command=self.abrir_loginadm,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        # button_3.place(x=958.0, y=615.0, width=205.0, height=58.0)
        button_3.place(anchor="center",x=background_image.width()*15/self.num_columnas, y=background_image.height()*9/self.num_filas, width=button_image_3.width(), height=button_image_3.height())

        # button_image_hover_3 = PhotoImage(file=relative_to_assets("button_hover_2.png"))
        button_image_hover_3_raw = Image.open(str(relative_to_assets("button_hover_2.png")))
        button_image_hover_3_new_size = ImageOps.contain(button_image_hover_3_raw,(button_3_width,button_3_height))
        button_image_hover_3 = ImageTk.PhotoImage(button_image_hover_3_new_size)
        button_3.bind('<Enter>', lambda e: button_3.config(image=button_image_hover_3))
        button_3.bind('<Leave>', lambda e: button_3.config(image=button_image_3))

        


        # image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        # canvas.create_image(1072.0, 420.0, image=image_image_3)
        image_image_3_raw = Image.open(str(relative_to_assets("image_3.png")))
        image_image_3_width= int(background_image.width()*5/self.num_columnas)
        image_image_3_height= int(background_image.height()*5/self.num_filas)
        image_image_3_new_size = ImageOps.contain(image_image_3_raw,(image_image_3_width,image_image_3_height))
        image_image_3 = ImageTk.PhotoImage(image_image_3_new_size)
        canvas.create_image(background_image.width()*15/self.num_columnas, background_image.height()*6/self.num_filas, image=image_image_3)



        # image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        # canvas.create_image(1061.0, 590.0, image=image_image_5)
        image_image_5_raw = Image.open(str(relative_to_assets("image_5.png")))
        image_image_5_width= int(background_image.width()*5/self.num_columnas)
        image_image_5_height= int(background_image.height()*4/self.num_filas)
        image_image_5_new_size = ImageOps.contain(image_image_5_raw,(image_image_5_width,image_image_5_height))
        image_image_5 = ImageTk.PhotoImage(image_image_5_new_size)
        canvas.create_image(background_image.width()*15/self.num_columnas, background_image.height()*8/self.num_filas, image=image_image_5)


        # image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
        # canvas.create_image(1072.0, 164.0, image=image_image_7)
        image_image_7_raw = Image.open(str(relative_to_assets("image_7.png")))
        image_image_7_width= int(background_image.width()*5/self.num_columnas)
        image_image_7_height= int(background_image.height()*4/self.num_filas)
        image_image_7_new_size = ImageOps.contain(image_image_7_raw,(image_image_7_width,image_image_7_height))
        image_image_7 = ImageTk.PhotoImage(image_image_7_new_size)
        canvas.create_image(background_image.width()*15/self.num_columnas, background_image.height()*3/self.num_filas, image=image_image_7)

        self.image_references = [
            background_image, button_image_1, button_image_hover_1,
            button_image_2, button_image_hover_2, button_image_3,
            button_image_hover_3, button_image_4, button_image_hover_4,
            image_image_2,
            image_image_3, image_image_4, image_image_5, image_image_6,
            image_image_7
        ]

    def abrir_login(self):
        self.destroy() 
        print('Login User')
        login_window = LoginWindow()  
        login_window.mainloop()  

    def abrir_loginadm(self):
        self.destroy() 
        print('Login Admin')
        login_window = LoginAdmin()  
        login_window.mainloop()  


    def abrir_registro(self):
        self.destroy()
        print('Registro Estudiante')
        registro_user_window = RegistroEstudianteWindow()
        registro_user_window.mainloop()

    def abrir_registroadmin(self):
        self.destroy()
        print('Registro admin')
        registro_admin_window = RegistroAdminWindow()
        registro_admin_window.mainloop()

    def abrir_volver(self):
        self.destroy()
        from inicio import InicioWindow
        inicio_window = InicioWindow()
        inicio_window.mainloop()