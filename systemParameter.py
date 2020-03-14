from mysqlDb import mysql
from flask import Flask, render_template, url_for, request, redirect, session, flash


def parametroInicio():
    print("PARAMETROS:")
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM parametro')
    data = cur.fetchall()
    cur.close()
    return render_template("parametros.html", parametros=data)


def parametroAdd(nombre, valor):
    # Crear cursor
    cur = mysql.connection.cursor()

    # Preparar el query y ejecutar query
    cur.execute(
        "INSERT INTO parametro (parametroNom, parametroValor) VALUES (%s, %s)", (nombre, valor))
    mysql.connection.commit()

    # Cerramos Conexion
    cur.close()

    flash("El parámetro se ingreso correctamente", "alert-success")
    return redirect(url_for('Parametros'))


def parametroDelete(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM parametro WHERE parametroId = {0}'.format(id))
    mysql.connection.commit()
    cur.close()
    flash("El parámetro se elimino correctamente", "alert-success")
    return redirect(url_for('Parametros'))


def parametroUpdate(nombre, valor, idParametro):
        cur = mysql.connection.cursor()
        cur.execute(
            'UPDATE parametro SET parametroNom = %s, parametroValor = %s WHERE parametroId = %s', (nombre, valor, idParametro))
        mysql.connection.commit()
        cur.close()
        flash("El parámetro se actualizó correctamente", "alert-success")
        return redirect(url_for('Parametros'))
