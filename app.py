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
from corral import *
from sellAnimal import *
from animalHistory import *
from cattleFattening import *
from corralAnimal import *
from datetime import date
from dateutil import parser
from animalDetail import *

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

# Pagina detalle animal
@app.route('/detalleAnimal/<string:id>', methods=["GET", "POST"])
def detalleAnimal(id):
    if 'nombre' in session:
        print(id + ' IDDDDDDDDDDDDDDDDD')
        makeGraph(id)
        data = getAnimalDetail(id)
        source = "../static/grafica{0}.png".format(id)
        return render_template("animalHistoryGraph.html", details = data, source=source)
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
        nombre = request.form['nombrefrigorificoModal']
        return frigorificoUpdate(nombre, idFrigorifico)
    else:
        return render_template('login.html')


#################### CORRAL ####################
# Pagina corral listar todo
@app.route('/Corral', methods=["GET", "POST"])
def Corral():
    if 'nombre' in session:
        return corralInicio()
    else:
        return render_template('login.html')

# Pagina Corral add
@app.route('/AddCorral', methods=["POST"])
def AddCorral():
    print("CORRAL ADD")
    if 'nombre' in session:
        nombre = request.form['nombreCorral']
        capacidad = request.form['capacidadCorral']
        ubicacion = request.form['ubicacionCorral']
        return corralAdd(nombre, capacidad, ubicacion)
    else:
        return render_template('login.html')

# Pagina Corral delete
@app.route('/DeleteCorral/<string:id>')
def DeleteCorral(id):
    print("CORRAL DELETE")
    if 'nombre' in session:
        return corralDelete(id)
    else:
        return render_template('login.html')

# Pagina Corral Update
@app.route('/UpdateCorral', methods=["POST"])
def UpdateCorral():
    print("CORRAL UPDATE")
    if 'nombre' in session:
        idCorral = request.form['idCorralModal']
        nombre = request.form['nombreCorralModal']
        capacidad = request.form['capacidadCorralModal']
        ubicacion = request.form['ubicacionCorralModal']
        return corralUpdate(nombre, capacidad, ubicacion, idCorral)
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
    print("ANIMAL UPDATE")
    if 'nombre' in session:
        id = request.form['idAnimalModal']
        tipoAnimal = request.form['idTipoAnimalModal']
        identificador = request.form['identificadorAnimalModal']
        return animalUpdate(identificador, tipoAnimal, id)
    else:
        return render_template('login.html')


#################### HISTORIA ANIMAL ####################
# Pagina HistoriaAnimal listar todo
@app.route('/AnimalHistoria', methods=["GET", "POST"])
def AnimalHistoria():
    if 'nombre' in session:
        return historiaInicio()
    else:
        return render_template('login.html')

# Pagina Historia add
@app.route('/AddHistoria', methods=["POST"])
def AddHistoria():
    print("HISTORIA ADD")
    if 'nombre' in session:
        idAnimal = request.form['idAnimal']
        fecha = request.form['fechaHistoria']
        peso = request.form['pesoHistoria']
        obs = request.form['obsHistoria']
        return historiaAdd(idAnimal, fecha, peso, obs)
    else:
        return render_template('login.html')

# Pagina Historia delete
@app.route('/DeleteHistoria/<idAnimal>/<fechaHistoria>')
def DeleteHistoria(idAnimal, fechaHistoria):
    print("Historia DELETE")
    if 'nombre' in session:
        return historiaDelete(idAnimal, fechaHistoria)
    else:
        return render_template('login.html')

# Pagina Historia Update
@app.route('/UpdateHistoria', methods=["POST"])
def UpdateHistoria():
    print("Historia UPDATE")
    if 'nombre' in session:
        idAnimal = request.form['idAnimalModal']
        fecha = request.form['fechaHistoriaModal']
        peso = request.form['pesoHistoriaModal']
        obs = request.form['obsHistoriaModal']
        return historiaUpdate(idAnimal, fecha, peso, obs)
    else:
        return render_template('login.html')


#################### CORRALANIMAL ####################
# Pagina corralanimal listar todo
@app.route('/CorralAnimal/<idCorral>', methods=["GET", "POST"])
def CorralAnimal(idCorral):
    if 'nombre' in session:
        return corralAnimalInicio(idCorral)
    else:
        return render_template('login.html')

# Pagina CorralAnimal add
@app.route('/AddCorralAnimal', methods=["POST"])
def AddCorralAnimal():
    print("CORRALANIMAL ADD")
    if 'nombre' in session:
        corral = request.form['idCorral']
        animal = request.form['idAnimal']
        fecha = request.form['corralFecha']
        fechaFinStr = request.form['corralFechaFin']
        if fechaFinStr == '':
            fechaFin = date.min
        else:
            fechaFin = request.form['corralFechaFin']
        
        print(fechaFin)
        return corralAnimalAdd(corral, animal, fecha, fechaFin)
    else:
        return render_template('login.html')

# Pagina CorralAnimal delete
@app.route('/DeleteCorralAnimal/<idCorral>/<idAnimal>/<corralAnimalFecha>')
def DeleteCorralAnimal(idCorral, idAnimal, corralAnimalFecha):
    print("CORRAL ANIMAL DELETE")
    if 'nombre' in session:
        return corralAnimalDelete(idCorral, idAnimal, corralAnimalFecha)
    else:
        return render_template('login.html')

# Pagina CorralAnimal Update
@app.route('/UpdateCorralAnimal', methods=["POST"])
def UpdateCorralAnimal():
    print("CORRAL Animal UPDATE")
    if 'nombre' in session:
        corral = request.form['idCorralModal']
        animal = request.form['idAnimalModal']
        fecha = request.form['corralFechaModal']
        fechaFin = request.form['corralFechaFinModal']
        return corralAnimalUpdate(corral, animal, fecha, fechaFin)
    else:
        return render_template('login.html')


#################### COMPRA ####################
# Pagina Compra listar todo
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


#################### VENTA ####################
# Pagina Venta listar todo
@app.route('/Venta', methods=["GET", "POST"])
def Venta():
    if 'nombre' in session:
        return ventaInicio()
    else:
        return render_template('login.html')

# Pagina Venta add
@app.route('/AddVenta', methods=["POST"])
def AddVenta():
    print("VENTA ADD")
    if 'nombre' in session:
        fecha = request.form['fechaVenta']
        idAnimal = request.form['idAnimalVenta']
        idFrigorifico = request.form['idFrigorificoVenta']
        precio = request.form['precioVenta']
        return ventaAdd(fecha, idAnimal, idFrigorifico, precio)
    else:
        return render_template('login.html')

# Pagina Venta delete
@app.route('/DeleteVenta/<string:id>')
def DeleteVenta(id):
    print("Venta DELETE")
    if 'nombre' in session:
        return ventaDelete(id)
    else:
        return render_template('login.html')

# Pagina Venta Update
@app.route('/UpdateVenta', methods=["POST"])
def UpdateVenta():
    print("Venta UPDATE")
    if 'nombre' in session:
        id = request.form['idVentaModal']
        fecha = request.form['fechaVentaModal']
        animalId = request.form['idAnimalVentaModal']
        idFrigorifico = request.form['idFrigorificoVenta']        
        precio = request.form['precioVentaModal']
        return ventaUpdate(fecha, animalId, idFrigorifico, precio, id)
    else:
        return render_template('login.html')


#################### ENGORDE ####################
# Pagina Engorde listar todo
@app.route('/Engorde', methods=["GET", "POST"])
def Engorde():
    if 'nombre' in session:
        return engordeInicio()
    else:
        return render_template('login.html')

# Pagina Engorde add
@app.route('/AddEngorde', methods=["POST"])
def AddEngorde():
    print("Engorde ADD")
    if 'nombre' in session:
        idCorral = request.form['idCorral']
        #idEngorde = request.form['idEngorde']
        tipoRacion = request.form['tipoRacion']
        fechaEngorde = request.form['fechaEngorde']
        return engordeAdd(idCorral, tipoRacion, fechaEngorde)
    else:
        return render_template('login.html')

# Pagina Engorde delete
@app.route('/DeleteEngorde/<idCorral>/<idEngorde>')
def DeleteEngorde(idCorral, idEngorde):
    print("Engorde DELETE")
    if 'nombre' in session:
        return engordeDelete(idCorral, idEngorde)
    else:
        return render_template('login.html')

# Pagina Engorde Update
@app.route('/UpdateEngorde', methods=["POST"])
def UpdateEngorde():
    print("Engorde UPDATE")
    if 'nombre' in session:
        idCorral = request.form['idCorralModal']
        idEngorde = request.form['idEngordeModal']
        tipoRacion = request.form['tipoRacionModal']
        fechaEngorde = request.form['fechaEngordeModal']
        return engordeUpdate(idCorral, idEngorde, tipoRacion, fechaEngorde)
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
