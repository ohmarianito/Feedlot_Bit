from mysqlDb import mysql
from flask import Flask, render_template, url_for, request, redirect, session, flash


def racionTipoInicio():
    print("TIPO RACION:")
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tiporacion')
    data = cur.fetchall()
    cur.close()
    return render_template("tipoRacion.html", raciones=data)


def racionTipoAdd(nombre):

    # Crear cursor
    cur = mysql.connection.cursor()
    # Preparar el query y ejecutar query
    query = "INSERT INTO tiporacion (TipoRacionNom) VALUES ('" + \
        nombre + "')"
    cur.execute(query)
    mysql.connection.commit()

    # Cerramos Conexion
    cur.close()

    flash("El tipo de ración se ingreso correctamente", "alert-success")
    return redirect(url_for('TipoRacion'))


def racionTipoDelete(id):
    cur = mysql.connection.cursor()
    cur.execute(
        'DELETE FROM tiporacion WHERE TipoRacionid = {0}'.format(id))
    mysql.connection.commit()
    cur.close()
    flash("El tipo de ración se elimino correctamente", "alert-success")
    return redirect(url_for('TipoRacion'))


def racionTipoUpdate(nombre, id):
    cur = mysql.connection.cursor()
    cur.execute(
        'UPDATE tiporacion SET TipoRacionNom = %s WHERE TipoRacionid = %s', (nombre, id))
    mysql.connection.commit()
    cur.close()
    flash("El tipo de ración se actualizó correctamente", "alert-success")
    return redirect(url_for('TipoRacion'))
