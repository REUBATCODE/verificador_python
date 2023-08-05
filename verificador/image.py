from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.title('Imagencita')
ventana.geometry('500x500')
#Creamos una variable para la imagen
try:
    image = Image.open("./img/portatil_ultrafino.jpg")
    image = image.resize((300, 300))

    test = ImageTk.PhotoImage(image)
    lbl_codigo = Label(ventana, image=test)
except:
    lbl_codigo = Label(ventana, text='imagen no disponible')


#Labels
lbl_codigo.pack(pady=20)

ventana.mainloop()