from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
@app.route("/")
def hello_world():
    try:
        number1 = float(request.form.get("num1"))
        number2 = float(request.form.get("num2"))
        suma = number1+number2
        resta = number1-number2
        division = number1/number2
        multiplicacion = number1*number2
    except:
        number1, number2, suma, resta, multiplicacion, division='','','','','',''
    return render_template("hello_1.html", n1=number1, n2=number2, suma=suma, resta=resta, multiplicacion=multiplicacion, division=division)