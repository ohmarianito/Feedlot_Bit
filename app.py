from flask import Flask, render_template, url_for, request, redirect, session, flash, json
from mysqlDb import mysql
from graph import makeGraph
from login import *
from rationType import *
from historicPrice import *
from systemParameter import *
from animalType import *
from slaughterhouse import *
from animal import *
from buyAnimal import *

# Objeto Flask
app = Flask(__name__)

# Llave secreta
app.secret_key = "appLogin"

# BD config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'feedlot'

# Objeto MySQL
mysql.init_app(app)

# Pagina Login
@app.route('/')
def index():
    print("INICIANDO:")
    if 'nombre' in session:
        return render_template('home.html')
    else:
        return render_template('login.html')

# Pagina Principal
@app.route('/inicio')
def inicio():
    if 'nombre' in session:
        return render_template('home.html')
    else:
        return render_template('login.html')

# Pagina registro usuario
@app.route('/registrar', methods=["GET", "POST"])
def registrar():
    print("REGISTRANDO:")
    if (request.method == "GET"):
        return render_template('login.html')
    else:
        # Obtener los datos
        nombre = request.form['usernameRegister']
        correo = request.form['emailRegister']
        password = request.form['passwordRegister']
        return registrarUsuario(nombre, correo, password)

# Pagina ingreso usuario
@app.route('/ingresar', methods=["GET", "POST"])
def ingresar():
    print("INGRESANDO:")
    if (request.method == "GET"):
        return render_template('login.html')
    else:
        # Obtener los datos
        correo = request.form['emailLogin']
        password = request.form['passwordLogin']
        return ingresoUsuario(correo, password)

# Pagina historia animal
@app.route('/historiaAnimal', methods=["GET", "POST"])
def historiaAnimal():
    if 'nombre' in session:
        makeGraph()
        return render_template("animalHistory.html")
    else:
        return render_template('login.html')


#################### PRECIO HISTORICO ####################
# Pagina Precio historico listar todo
@app.route('/PrecioHistoria', methods=["GET", "POST"])
def PrecioHistoria():
    if 'nombre' in session:
        return precioHistoriaInicio()
    else:
        return render_template('login.html')

# Pagina Precio historico add
@app.route('/AddPrecioHistoria', methods=["POST"])
def AddPrecioHistoria():
    print("HISTORIA DEL PRECIO ADD")
    if 'nombre' in session:
        fecha = request.form['fechaHistorial']
        precio = request.form['precioHistorial']
        return precioHistoriaAdd(fecha, precio)
    else:
        return render_template('login.html')

# Pagina Precio historico delete
@app.route('/DeletePrecioHistoria/<string:id>')
def DeletePrecioHistoria(id):
    print("HISTORIA DEL PRECIO DELETE")
    if 'nombre' in session:
        return precioHistoriaDelete(id)
    else:
        return render_template('login.html')

# Pagina Precio historico Update
@app.route('/UpdatePrecioHistoria', methods=["POST"])
def UpdatePrecioHistoria():
    print("HISTORIA DEL PRECIO UPDATE")
    if 'nombre' in session:
        idPrecioHistoria = request.form['idHistorialModal']
        fecha = request.form['fechaHistorialModal']
        precio = request.form['precioHistorialModal']
        return precioHistoriaUpdate(fecha, precio, idPrecioHistoria)
    else:
        return render_template('login.html')


#################### PARAMETROS DEL SISTEMA ####################
# Pagina Parametros listar todo
@app.route('/Parametros', methods=["GET", "POST"])
def Parametros():
    if 'nombre' in session:
        return parametroInicio()
    else:
        return render_template('login.html')

# Pagina Parametro add
@app.route('/AddParametro', methods=["POST"])
def AddParametro():
    print("PARAMETRO ADD")
    if 'nombre' in session:
        nombre = request.form['nombreParametro']
        valor = request.form['valorParametro']
        return parametroAdd(nombre, valor)
    else:
        return render_template('login.html')

# Pagina Precio historico delete
@app.route('/DeleteParametro/<string:id>')
def DeleteParametro(id):
    print("PARAMETRO DELETE")
    if 'nombre' in session:
        return parametroDelete(id)
    else:
        return render_template('login.html')

# Pagina Precio historico Update
@app.route('/UpdateParametro', methods=["POST"])
def UpdateParametro():
    print("PARAMETRO UPDATE")
    if 'nombre' in session:
        idParametro = request.form['idParametroModal']
        nombre = request.form['nombreParametroModal']
        valor = request.form['valorParametrolModal']
        return parametroUpdate(nombre, valor, idParametro)
    else:
        return render_template('login.html')

#################### TIPOS DE ANIMAL ####################
# Pagina TIPO ANIMAL listar todo
@app.route('/TipoAnimal', methods=["GET", "POST"])
def TipoAnimal():
    if 'nombre' in session:
        return tipoAnimalInicio()
    else:
        return render_template('login.html')

# Pagina TIPO ANIMAL add
@app.route('/AddTipoAnimal', methods=["POST"])
def AddTipoAnimal():
    print("TIPO ANIMAL ADD")
    if 'nombre' in session:
        nombre = request.form['nombreTipoAnimal']
        return tipoAnimalAdd(nombre)
    else:
        return render_template('login.html')

# Pagina TIPO ANIAMAL delete
@app.route('/DeleteTipoAnimal/<string:id>')
def DeleteTipoAnimal(id):
    print("TIPO ANIMAL DELETE")
    if 'nombre' in session:
        return tipoAnimalDelete(id)
    else:
        return render_template('login.html')

# Pagina Precio historico Update
@app.route('/UpdateTipoAnimal', methods=["POST"])
def UpdateTipoAnimal():
    print("TIPO ANIMAL UPDATE")
    if 'nombre' in session:
        idTipoAnimal = request.form['idTipoAnimalModal']
        nombre = request.form['nombreTipoAnimalModal']
        return tipoAnimalUpdate(nombre, idTipoAnimal)
    else:
        return render_template('login.html')


#################### TIPOS DE RACION ####################
# Pagina TIPO ANIMAL listar todo
@app.route('/TipoRacion', methods=["GET", "POST"])
def TipoRacion():
    if 'nombre' in session:
        return racionTipoInicio()
    else:
        return render_template('login.html')

# Pagina TIPO ANIMAL add
@app.route('/AddTipoRacion', methods=["POST"])
def AddTipoRacion():
    print("TIPO RACION ADD")
    if 'nombre' in session:
        nombre = request.form['nombreTipoRacion']
        return racionTipoAdd(nombre)
    else:
        return render_template('login.html')

# Pagina TIPO ANIAMAL delete
@app.route('/DeleteTipoRacion/<string:id>')
def DeleteTipoRacion(id):
    print("TIPO RACION DELETE")
    if 'nombre' in session:
        return racionTipoDelete(id)
    else:
        return render_template('login.html')

# Pagina Precio historico Update
@app.route('/UpdateTipoRacion', methods=["POST"])
def UpdateTipoRacion():
    print("TIPO RACION UPDATE")
    if 'nombre' in session:
        id = request.form['idTipoRacionModal']
        nombre = request.form['nombreTipoRacionModal']
        return racionTipoUpdate(nombre, id)
    else:
        return render_template('login.html')

#################### FRIGORÍFICO ####################
# Pagina frigorifico listar todo
@app.route('/Frigorifico', methods=["GET", "POST"])
def Frigorifico():
    if 'nombre' in session:
        return frigorificoInicio()
    else:
        return render_template('login.html')

# Pagina Frigorífico add
@app.route('/AddFrigorifico', methods=["POST"])
def AddFrigorifico():
    print("FRIGORÍFICO ADD")
    if 'nombre' in session:
        nombre = request.form['nombreFrigorifico']
        return frigorificoAdd(nombre)
    else:
        return render_template('login.html')

# Pagina Frigorífico delete
@app.route('/DeleteFrigorifico/<string:id>')
def DeleteFrigorifico(id):
    print("FRIGORÍFICO DELETE")
    if 'nombre' in session:
        return frigorificoDelete(id)
    else:
        return render_template('login.html')

# Pagina Frigorífico Update
@app.route('/UpdateFrigorifico', methods=["POST"])
def UpdateFrigorifico():
    print("FRIGORÍFICO UPDATE")
    if 'nombre' in session:
        idFrigorifico = request.form['idFrigorificoModal']
        nombre = request.form['nombreFrigorificoModal']
        return frigorificoUpdate(nombre, idFrigorifico)
    else:
        return render_template('login.html')

#################### ANIMAL ####################
# Pagina animal listar todo
@app.route('/Animal', methods=["GET", "POST"])
def Animal():
    if 'nombre' in session:
        return animalInicio()
    else:
        return render_template('login.html')

# Pagina Animal add
@app.route('/AddAnimal', methods=["POST"])
def AddAnimal():
    print("ANIMAL ADD")
    if 'nombre' in session:
        print('VIENE A ANIMALLLLLL')
        identificador = request.form['identificadorAnimal']
        tipoAnimal = request.form['idTipoAnimal']
        return animalAdd(identificador, tipoAnimal)
    else:
        return render_template('login.html')

# Pagina Animal delete
@app.route('/DeleteAnimal/<string:id>')
def DeleteAnimal(id):
    print("Animal DELETE")
    if 'nombre' in session:
        return animalDelete(id)
    else:
        return render_template('login.html')

# Pagina Animal Update
@app.route('/UpdateAnimal', methods=["POST"])
def UpdateAnimal():
    print("FRIGORÍFICO UPDATE")
    if 'nombre' in session:
        id = request.form['idAnimalModal']
        tipoAnimal = request.form['idTipoAnimalModal']
        identificador = request.form['identificadorAnimalModal']
        return animalUpdate(identificador, tipoAnimal, id)
    else:
        return render_template('login.html')


#################### COMPRA  TODO ####################
# Pagina frigorifico listar todo
@app.route('/Compra', methods=["GET", "POST"])
def Compra():
    if 'nombre' in session:
        return compraInicio()
    else:
        return render_template('login.html')

# Pagina Compra add
@app.route('/AddCompra', methods=["POST"])
def AddCompra():
    print("COMPRA ADD")
    if 'nombre' in session:
        fecha = request.form['fechaCompra']
        idAnimal = request.form['idAnimalCompra']
        precio = request.form['precioCompra']
        return compraAdd(fecha, idAnimal, precio)
    else:
        return render_template('login.html')

# Pagina Compra delete
@app.route('/DeleteCompra/<string:id>')
def DeleteCompra(id):
    print("Compra DELETE")
    if 'nombre' in session:
        return compraDelete(id)
    else:
        return render_template('login.html')

# Pagina Compra Update
@app.route('/UpdateCompra', methods=["POST"])
def UpdateCompra():
    print("Compra UPDATE")
    if 'nombre' in session:
        id = request.form['idCompraModal']
        fecha = request.form['fechaCompraModal']
        animalId = request.form['idAnimalCompraModal']
        precio = request.form['precioCompraModal']
        return compraUpdate(fecha, animalId, precio, id)
    else:
        return render_template('login.html')


#################### SALIR ####################
@app.route("/salir")
def salir():
    print("SALIENDO:")
    # limpiar session
    session.clear()
    # A login
    return redirect(url_for('inicio'))


# FUNCION PRINCIPAL VA ULTIMA
if __name__ == "__main__":
    app.run(debug=True)
