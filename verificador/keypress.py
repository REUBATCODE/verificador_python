from tkinter import *
import tkinter.messagebox
import apiBuscar
from PIL import Image, ImageTk

codigo = ''

def key_pressed(event):
    global codigo
    if event.keysym=='Return':
        #print(event.keysym)
        print("Buscamos producto"+codigo)
        codigo = ''
    else:
        codigo += event.keysym
    
ventana=Tk()
ventana.title('Keypressed')
ventana.geometry('500x500')

ventana.bind('<Key>', key_pressed)
ventana.mainloop()