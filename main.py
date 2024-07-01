
from inicio import InicioWindow
from database import create_tables

def main():
    create_tables()
    window = InicioWindow()
    window.mainloop()

if __name__ == "__main__":
    main()