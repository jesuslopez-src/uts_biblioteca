from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from loginadm import LoginAdmin
from login import LoginWindow
from registro_adm import RegistroAdminWindow
from registro_user import RegistroEstudianteWindow


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "seleccion" / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class SeleccionWindow(Tk):
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

        background_image = PhotoImage(file=relative_to_assets("image_1.png"))
        canvas.create_image(640.0, 407.0, image=background_image)

        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            command=self.abrir_volver,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_1.place(x=57.0, y=36.0, width=146.0, height=36.150001525878906)

        button_image_hover_1 = PhotoImage(file=relative_to_assets("button_hover_1.png"))
        button_1.bind('<Enter>', lambda e: button_1.config(image=button_image_hover_1))
        button_1.bind('<Leave>', lambda e: button_1.config(image=button_image_1))

        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            command=self.abrir_login,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_2.place(x=116.0, y=616.0, width=205.0, height=57.0)

        button_image_hover_2 = PhotoImage(file=relative_to_assets("button_hover_3.png"))
        button_2.bind('<Enter>', lambda e: button_2.config(image=button_image_hover_2))
        button_2.bind('<Leave>', lambda e: button_2.config(image=button_image_2))

        button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self,
            command=self.abrir_loginadm,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_3.place(x=958.0, y=615.0, width=205.0, height=58.0)

        button_image_hover_3 = PhotoImage(file=relative_to_assets("button_hover_2.png"))
        button_3.bind('<Enter>', lambda e: button_3.config(image=button_image_hover_3))
        button_3.bind('<Leave>', lambda e: button_3.config(image=button_image_3))

        button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        button_4 = Button(
            self,
            command=self.abrir_registro,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_4.place(x=116.0, y=695.0, width=205.0, height=57.0)

        button_image_hover_4 = PhotoImage(file=relative_to_assets("button_hover_4.png"))
        button_4.bind('<Enter>', lambda e: button_4.config(image=button_image_hover_4))
        button_4.bind('<Leave>', lambda e: button_4.config(image=button_image_4))


        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        canvas.create_image(226.0, 404.0, image=image_image_2)

        image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        canvas.create_image(1072.0, 420.0, image=image_image_3)

        image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        canvas.create_image(226.0, 590.0, image=image_image_4)

        image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        canvas.create_image(1061.0, 590.0, image=image_image_5)

        image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        canvas.create_image(226.0, 164.0, image=image_image_6)

        image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
        canvas.create_image(1072.0, 164.0, image=image_image_7)

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