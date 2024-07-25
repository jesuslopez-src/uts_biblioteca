from PIL import ImageTk, Image, ImageOps


def crear_imagen(bg_image:ImageTk.PhotoImage,path:str,ancho_col,alto_col,num_columnas,num_filas)->ImageTk.PhotoImage:
    image_raw = Image.open(path)
    x = bg_image.width()*ancho_col/num_columnas
    y = bg_image.height()*alto_col/num_filas
    image_width= int(x)
    image_height= int(y)
    image_new_size = ImageOps.contain(image_raw,(image_width,image_height))
    image = ImageTk.PhotoImage(image_new_size)
    return image
