import apiBuscar
codigo=''
while codigo != 'salir':
    codigo=input('Escriba el codigo del producto a buscar: ')
    if codigo=='salir': break
    respuesta = apiBuscar.buscarProducto(codigo)
    if respuesta == 0:
        print("No existe el producto llamado "+codigo)
    elif respuesta == -1:
        print('No hubo conexión.')
    else:
        print("El producto es: "+str(respuesta[1])+"\nEl precio es: "+str(respuesta[2]))
print('Gracias por usar el Sistema.')