from flask import Flask, render_template, request

app = Flask(__name__)

class Calculadora:
    def __init__(self, valor1, valor2, operacao):
        self.valor1 = valor1
        self.valor2 = valor2
        self.operacao = operacao

@app.route("/")
def inicio():
    return render_template("calculadora.html")

@app.route("/calculadora", methods=["GET", "POST"])
def recebe_valores():
    calculo = Calculadora(request.form['valor1'], request.form['valor2'], request.form['operacao'])
    
    if calculo.operacao == "Adição":
        resultado = int(calculo.valor1) + int(calculo.valor2)
    elif calculo.operacao == "Subtração":
        resultado = int(calculo.valor1) - int(calculo.valor2)
    elif calculo.operacao == "Multiplicação":
        resultado = int(calculo.valor1) * int(calculo.valor2)
    elif calculo.operacao == "Divisão":
        resultado = int(calculo.valor1) / int(calculo.valor2)
    else:
        return "Não é possível realizar a operação."
    
    resposta = f"O resultado da {calculo.operacao} entre {calculo.valor1} e {calculo.valor2} é {resultado}."
    return resposta

app.run(debug=True)