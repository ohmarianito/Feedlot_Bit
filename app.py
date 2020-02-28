from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_mysqldb import MySQL
from graph import makeGraph


# Objeto Flask
app = Flask(__name__)

# Llave secreta
app.secret_key = "appLogin"

# BD config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'feedlotdb'


# Objeto MySQL
mysql = MySQL(app)

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
        print(nombre + " " + correo + " " + password)

        # Preparar el query
        sQuery = "INSERT INTO login (correo, password, nombre) VALUES (%s, %s, %s)"

        # Crear cursor
        cur = mysql.connection.cursor()

        # Ejecutar query
        cur.execute(sQuery, (correo, password, nombre))

        try:
            # Commit
            mysql.connection.commit()

            # Registrar en session
            session['nombre'] = nombre
            session['correo'] = correo
        except:
            # limpiar session
            print('ERRORR')

        cur.close()
        session.clear()
        # Redireccion
        flash("Usuario registrado correctamente", "alert-success")
        return render_template('login.html')


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
        print("LOS DATOS INGRESADOS SON:")
        print(correo + " " + password)

        # Crear cursor
        cur = mysql.connection.cursor()

        # Preparar el query
        sQuery = "SELECT correo, password, nombre FROM login WHERE correo = %s"

        # Ejecutar query
        cur.execute(sQuery, [correo])

        # Obtener los datos
        usuario = cur.fetchone()
        cur.close()

        # Verificar los datos
        if(usuario != None):
            correoDB = usuario[0]
            passwordDB = usuario[1]
            userDB = usuario[2]
            print("Correo: " + correoDB)
            print("Pass: " + passwordDB)
            print("Nombre: " + userDB)
            if (password == passwordDB):
                # Registrar en session
                session['nombre'] = userDB
                session['correo'] = correoDB
                # Redireccion todo OK
                return redirect(url_for('inicio'))
            else:
                # Erro al password, msj error
                flash("El password no es correcto", "alert-warning")
                return render_template("login.html")

        else:
            # No existe enviar msj
            flash("El correo no existe", "alert-warning")
            return render_template("login.html")

# Pagina ingreso usuario
@app.route('/historiaAnimal', methods=["GET", "POST"])
def historiaAnimal():
    if 'nombre' in session:
        print("HISTORIA DEL ANIMAL:")
        makeGraph()
        return render_template("animalHistory.html")
    else:
        return render_template('login.html')


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
