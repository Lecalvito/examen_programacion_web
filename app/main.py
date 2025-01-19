from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/redirigir', methods=['GET', 'POST'])
def redirigir():
    ejercicio = request.form.get('ejercicio')
    if ejercicio == 'Ejercicio1':
        return redirect('/ejercicio1')
    elif  ejercicio == 'Ejercicio2':
        return redirect('/ejercicio2')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'GET':
        return render_template('ejercicio1.html', resultado=None)
    elif request.method == 'POST':
        nombre = request.form.get('nombre', '')
        edad = int(request.form.get('edad'), 0)
        cantidad = int(request.form.get('cantidad'), 0)
        valor_total = 9000 * cantidad

        if edad >= 18:
            if edad <= 30:
                descuento = 15
            else:
                descuento = 25
        else:
            descuento = 0

        valor_descuento = valor_total * (descuento / 100)
        valor_final = valor_total - valor_descuento

        resultado_hombre = f"Nombre del cliente: {nombre}"
        resultado_sin_descuento = f"Total sin descuento: ${valor_total}"
        resultado_descuento = f"El descuento es: ${valor_descuento}"
        resultado_total = f"El total a pagar es de: ${valor_final}"

        return render_template('ejercicio1.html',  nombre=resultado_hombre, valor_total=resultado_sin_descuento,
                               valor_descuento=resultado_descuento, valor_final=resultado_total)



@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():

    usuario_admin = "juan"
    usuario_user = "pepe"
    pass_admin = "admin"
    pass_user = "user"

    if request.method == 'GET':
        return render_template('ejercicio2.html', resultado=None)
    elif request.method == 'POST':
        nombre = request.form.get('nombre', '')
        password = request.form.get('password', '')
        if nombre == usuario_admin and password == pass_admin:
            mensaje = f"Bienvenido Administrador: {nombre}"
        elif nombre == usuario_user and password == pass_user:
            mensaje = f"Bienvenido Usuario: {nombre}"
        else:
            mensaje = "Usuario o contraseña incorrectos"
        return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == "__main__":
    app.run()