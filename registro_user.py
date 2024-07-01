from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from database import registrar_usuario

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "reguser" / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class RegistroEstudianteWindow(Tk):
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
        canvas.create_image(640.0, 370.5, image=entry_image_1)
        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#BDBDBD",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(x=551.0, y=355.0, width=178.0, height=35.0)

        entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        canvas.create_image(640.0, 447.5, image=entry_image_2)
        self.entry_2 = Entry(
            self,
            show="*",
            bd=0,
            bg="#BDBDBD",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(x=551.0, y=432.0, width=178.0, height=35.0)

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

        def button_1_hover(e):
            button_1.config(image=button_image_hover_1)

        def button_1_leave(e):
            button_1.config(image=button_image_1)

        button_1.bind('<Enter>', button_1_hover)
        button_1.bind('<Leave>', button_1_leave)

        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            command=self.registrar_estudiante,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_2.place(x=565.0, y=513.0, width=146.0, height=38.0)

        button_image_hover_2 = PhotoImage(file=relative_to_assets("button_hover_2.png"))

        def button_2_hover(e):
            button_2.config(image=button_image_hover_2)

        def button_2_leave(e):
            button_2.config(image=button_image_2)

        button_2.bind('<Enter>', button_2_hover)
        button_2.bind('<Leave>', button_2_leave)

        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        canvas.create_image(571.0, 334.0, image=image_image_2)

        image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        canvas.create_image(587.0, 413.0, image=image_image_3)

        image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        canvas.create_image(637.0, 232.0, image=image_image_4)

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