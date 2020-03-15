from mysqlDb import mysql
from flask import Flask, render_template, url_for, request, redirect, session, flash


def ingresoUsuario(correo, password):
    # Crear cursor
    cur = mysql.connection.cursor()

    # Preparar el query
    sQuery = "SELECT usuarioEmail, usuarioPass, usuarioNom FROM usuario WHERE usuarioEmail = %s"

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


def registrarUsuario(nombre, correo, password):
    try:
        # Preparar el query
        sQuery = "INSERT INTO usuario (usuarioEmail, usuarioPass, usuarioNom) VALUES (%s, %s, %s)"

        # Crear cursor
        cur = mysql.connection.cursor()

        # Ejecutar query
        cur.execute(sQuery, (correo, password, nombre))
        # Commit
        mysql.connection.commit()

        # Registrar en session
        session['nombre'] = nombre
        session['correo'] = correo
    except:
        # limpiar session
        flash("Error al registar usuario", "alert-warning")
        return render_template('login.html')

    cur.close()
    session.clear()
    # Redireccion
    flash("Usuario registrado correctamente", "alert-success")
    return render_template('login.html')
