from tkinter import *
import tkinter.messagebox
import apiBuscar
from PIL import Image, ImageTk

ventana = Tk()
ventana.title('Verificador')
ventana.geometry('500x500')

#colores
color_fondo = '#3E4551'
color_boton = '#FF9800'
color_texto = '#000000'
color_resultado = '#FFC107'

#ventana.configure(bg=color_fondo)

def llamarDatos():
    codigo = entry_a.get()
    resultado = apiBuscar.buscarProducto(codigo)

    if resultado is None:
        lbl_resultado.config(text="Producto no encontrado", fg=color_resultado)
    else:
        try:
            #Mostrar los datos del producto encontrado
            nombre_producto = resultado[1]
            precio_producto = resultado[2]
            print(f'.{resultado[3]}')
            image = Image.open("."+str(resultado[3]))
            #image = Image.open("./img/portatil_ultrafino.jpg")

            image = image.resize((200, 200))
            test = ImageTk.PhotoImage(image)
            lbl_imagencita = Label(ventana, image=test, width=200, height=200)
            lbl_imagencita.image = test
            #lbl_imagencita["image"] = test
            lbl_imagencita.pack()
            #lbl_imagencita = Label(ventana, image=test)
            #lbl_imagencita.pack(pady=20)
            y = (lbl_resultado.winfo_reqheight() + lbl_imagencita.winfo_reqheight()) + 60
            lbl_imagencita.place(x=50, y=y)
            llamarDatos.lbl_imagencita = lbl_imagencita

            #Actualizar la etiqueta de resultado
            lbl_resultado.config(text=f"Nombre: {nombre_producto}\nPrecio: ${precio_producto}", fg=color_resultado)
        except:
            print('Errorcito')
        

#Labels
lbl_codigo = Label(ventana, text="Introduzca el código del producto:", font="Helvetica 16 bold", fg=color_texto, bg=color_fondo)
lbl_codigo.pack(pady=20)

lbl_resultado = Label(ventana, text="Aqui debe aparecer el resultado", font="Helvetica 16 bold italic", fg=color_resultado, bg=color_fondo)
lbl_resultado.pack(pady=20)



#Buttons
btn_buscar = Button(ventana, text="Buscar producto", font="Helvetica 16 bold", bg=color_boton, fg=color_texto, command=llamarDatos)
btn_buscar.pack(pady=20)

#Entries
entry_a = Entry(ventana, font="Helvetica 16 bold", justify='center')
entry_a.pack(pady=20)

#image = Image.open("./img/portatil_ultrafino.jpg")

#image = image.resize((200, 200))
#test = ImageTk.PhotoImage(image)

#lbl_imagencita = Label(ventana, image=test)
#lbl_imagencita.pack(pady=20)

ventana.mainloop()