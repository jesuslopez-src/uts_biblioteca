from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from database import login_user


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "login" / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class LoginWindow(Tk):
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

        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        canvas.create_image(640.0, 366.5, image=entry_image_1)
        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#BDBDBD",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(x=550.0, y=351.0, width=178.0, height=35.0)

        entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        canvas.create_image(638.0, 438.5, image=entry_image_2)
        self.entry_2 = Entry(
            self,
            show="*",
            bd=0,
            bg="#BDBDBD",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(x=548.0, y=423.0, width=178.0, height=35.0)

        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            command=self.abrir_seleccion,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_1.place(x=60.0, y=51.0, width=146.0, height=34.0)

        button_image_hover_1 = PhotoImage(file=relative_to_assets("button_hover_1.png"))
        button_1.bind('<Enter>', lambda e: button_1.config(image=button_image_hover_1))
        button_1.bind('<Leave>', lambda e: button_1.config(image=button_image_1))

        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            command=self.login,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_2.place(x=565.0, y=572.0, width=146.0, height=38.0)

        button_image_hover_2 = PhotoImage(file=relative_to_assets("button_hover_2.png"))
        button_2.bind('<Enter>', lambda e: button_2.config(image=button_image_hover_2))
        button_2.bind('<Leave>', lambda e: button_2.config(image=button_image_2))

        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        canvas.create_image(569.0, 331.0, image=image_image_2)

        image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        canvas.create_image(587.0, 403.0, image=image_image_3)

        image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        canvas.create_image(637.0, 232.0, image=image_image_5)

        self.image_references = [
            background_image, entry_image_1, entry_image_2,
            button_image_1, button_image_hover_1, button_image_2,
            button_image_hover_2, image_image_2, image_image_3,
            image_image_5
        ]

    def login(self):
        usu_nom = self.entry_1.get()
        usu_pass = self.entry_2.get()

        self.login_user(usu_nom, usu_pass)

    def login_user(self, usu_nom, usu_pass):
        user = login_user(usu_nom, usu_pass)

        if user:
            self.destroy()
            print("Login Usuario Exitoso")
            # TODO: Abrir la ventana de usuario
        else:
            messagebox.showinfo(title="Error", message="Usuario o contraseña incorrectos")

    def abrir_seleccion(self):
        self.destroy()
        from seleccion import SeleccionWindow
        seleccion_window = SeleccionWindow()
        seleccion_window.mainloop()

if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.mainloop()