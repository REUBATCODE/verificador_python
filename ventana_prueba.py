from tkinter import *
import tkinter.messagebox

#Funciones
def funcion():
    try:
        lbl_resultado["text"]="Resultado = \n"+entry_a.get()+'+'+entry_b.get()+'= '+str(float(entry_a.get())+float(entry_b.get()))+'\n'+entry_a.get()+'-'+entry_b.get()+'= '+str(float(entry_a.get())-float(entry_b.get()))+'\n'+entry_a.get()+'÷'+entry_b.get()+'= '+str(float(entry_a.get())/float(entry_b.get()))+'\n'+entry_a.get()+'x'+entry_b.get()+'= '+str(float(entry_a.get())*float(entry_b.get()))
    except:
        tkinter.messagebox.showerror()

ventana=Tk()
ventana.title('Operaciones aritméticas')
ventana['bg']='#456789'
ventana.geometry('500x500')

#Labels
lbl_a=Label(ventana, text="Introduzca el valor de 'a': ",font="Helvetica 16 bold italic")
lbl_a.place(x=25, y=15)

lbl_b=Label(ventana, text="Introduzca el valor de 'b': ", font="Helvetica 16 bold italic")
lbl_b.place(x=25, y=45)

lbl_resultado=Label(ventana, text="Resultados: ", font="Helvetica 16 bold italic")
lbl_resultado.place(x=25, y=225)

#Entries
entry_a=Entry(ventana)
entry_a.place(x=240, y=15)
entry_a.insert(END, "5")

entry_b=Entry(ventana)
entry_b.place(x=240, y=45)
entry_b.insert(END, "10")


#Buttons
btn_resultado=Button(ventana, text="Realizar operaciones", font="Helvetica 16 bold italic", command=lambda : funcion())
btn_resultado.place(x=25, y=200)

#Esta línea siempre va al final de las ventanas
ventana.mainloop()