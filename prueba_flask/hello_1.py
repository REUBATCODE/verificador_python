#$ . .venv/bin/activate
#$ flask --app hello_1 run 
#$ flask --app hello_1 run --debug #Para no tener que reiniciar el servidor y que se reinicie solo

from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
@app.route("/")
def hello_world():
    print(request.method)
    print(request.form)
    print(request.form.get("num1"))
    try:
        number1 = float(request.form.get("num1"))
        number2 = float(request.form.get("num2"))
        suma = number1+number2
        print(suma)
        resta = number1-number2
        print(resta)
        division = number1/number2
        print(division)
        multiplicacion = number1*number2
        print(multiplicacion)
    except:
        number1=''
        number2=''
        suma=''
        resta=''
        multiplicacion=''
        division=''
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Aplicación de las cuatro operaciones básicas</h1>
    <div>
        <form action="#" method="POST">
            <p>Número 1</p> <input name="num1" type="number" value='"""+str(number1)+"""'>
            <p>Número 2</p> <input name="num2" type="number" value='"""+str(number2)+"""'>
            <button id="btncalcular">Calcular</button>
        </form>
        <p>
        Resultados: <br> La suma es: """+str(number1)+"""+"""+str(number2)+"""="""+str(suma)+"""
        <br> La resta es: """+str(number1)+"""-"""+str(number2)+"""="""+str(resta)+"""
        <br> La multiplicación es: """+str(number1)+"""x"""+str(number2)+"""="""+str(multiplicacion)+"""
        <br> La division es: """+str(number1)+"""÷"""+str(number2)+"""="""+str(division)+"""
        </p>
    </div>
</body>
</html>"""
