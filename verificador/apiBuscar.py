import mysql.connector

def buscarProducto(codigo):
    try:
        conexion = mysql.connector.connect(host='localhost', user='root', password='', database='pos')
        resultado = conexion.cursor()
        resultado.execute("SELECT * FROM productos WHERE codigo="+"'"+codigo+"'")
        registro = resultado.fetchone()
        if registro:
            #Toda la información del producto: código, nombre, precio, imagen.
            return registro
        else:
            #Se regresa None cuando no se encuentra el producto.
            return None
    except:
        #Se regresa None cuando hay un error en la conexión.
        return None
