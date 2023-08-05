import mysql.connector
try:
    conexion = mysql.connector.connect(host='localhost', user='root', password='', database='pos')
    resultado = conexion.cursor()
    nombre=''
    while nombre != 'salir':
        nombre=input('Escriba el nombre del producto a buscar: ')
        if nombre=='salir': break
        resultado.execute("SELECT * FROM productos WHERE nombre="+"'"+nombre+"'")
        registro = resultado.fetchone()
        if registro:
            print("El precio es: "+str(registro[2]))
        else:
            print("No existe el producto llamado "+nombre)
except:
    print('No hubo conexión.')
print('Gracias por usar el Sistema.')