import os 
os.system('cls')
try: 
    print('Bienvenido al programa oara obtener las operaciones básicas')
    a=float(input('Ingrese el valor de la primera variable: '))
    b=float(input('Ingrese el valor de la segunda variable: '))
    print('La suma de los valores es:',a+b,'\nLa resta de los valores es:',a-b,'\nLa multiplicación de los valores es:',a*b,'\nLa división de los valores es:',a/b)
except:
    print('Ha ocurrido un error en la captura de datos, favor de reiniciar el programa.')