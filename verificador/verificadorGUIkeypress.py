from tkinter import *
from PIL import Image, ImageTk
import apiBuscar

#colores
color_fondo = '#3E4551'
color_boton = '#FF9800'
color_texto = '#000000'
color_resultado = '#FFC107'

#variables globales
codigo = ''

def key_pressed(event):
    global codigo
    if event.keysym=='Return':
        llamarDatos(codigo)
        codigo = ''
    else:
        codigo += event.keysym

def llamarDatos(codigo):
    resultado = apiBuscar.buscarProducto(codigo)

    if resultado is None:
        lbl_resultado.config(text="Producto no encontrado", fg=color_resultado)
    else:
        try:
            #Mostrar los datos del producto encontrado
            nombre_producto = resultado[1]
            precio_producto = resultado[2]
            image = Image.open("."+str(resultado[3]))

            image = image.resize((200, 200))
            test = ImageTk.PhotoImage(image)
            lbl_imagencita = Label(ventana, image=test, width=200, height=200)
            lbl_imagencita.image = test
            lbl_imagencita.pack()
            y = (lbl_resultado.winfo_reqheight() + lbl_imagencita.winfo_reqheight()) + 60
            lbl_imagencita.place(x=50, y=y)
            llamarDatos.lbl_imagencita = lbl_imagencita

            #Actualizar la etiqueta de resultado
            lbl_resultado.config(text=f"Nombre: {nombre_producto}\nPrecio: ${precio_producto}", fg=color_resultado)
        except:
            print('Errorcito')
        
ventana = Tk()
ventana.title('Verificador')
ventana.state('zoomed')
ventana.configure(bg=color_fondo)

#Labels
lbl_codigo = Label(ventana, text="Introduzca el código del producto:", font="Helvetica 16 bold", fg=color_texto, bg=color_fondo)
lbl_codigo.pack(pady=20)

lbl_resultado = Label(ventana, text="Aqui debe aparecer el resultado", font="Helvetica 16 bold italic", fg=color_resultado, bg=color_fondo)
lbl_resultado.pack(pady=20)

ventana.bind('<Key>', key_pressed)
ventana.mainloop()