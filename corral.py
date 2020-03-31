from mysqlDb import mysql
from flask import Flask, render_template, url_for, request, redirect, session, flash


def corralInicio():
    print("CORRAL:")
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM corral')
    data = cur.fetchall()
    cur.close()
    return render_template("corral.html", corrales=data)


def corralAdd(nombre, capacidad, ubicacion):
    # Crear cursor
    cur = mysql.connection.cursor()
    # Preparar el query y ejecutar query
    query = "INSERT INTO corral (corralNom, corralCap, corralUbi) VALUES ('" + nombre + "', '" + capacidad + "', '" + ubicacion + "')"
    cur.execute(query)
    mysql.connection.commit()

    # Cerramos Conexion
    cur.close()

    flash("El corral se ingreso correctamente", "alert-success")
    return redirect(url_for('Corral'))


def corralDelete(id):
    cur = mysql.connection.cursor()
    cur.execute(
        'DELETE FROM corral WHERE corralId = {0}'.format(id))
    mysql.connection.commit()
    cur.close()
    flash("El corral se elimino correctamente", "alert-success")
    return redirect(url_for('Corral'))


def corralUpdate(nombre, capacidad, ubicacion, idCorral):
    cur = mysql.connection.cursor()
    print(nombre)
    print(idCorral)
    cur.execute(
        'UPDATE corral SET corralNom = %s, corralCap = %s, corralUbi = %s WHERE corralId = %s', (nombre, capacidad, ubicacion, idCorral))
    mysql.connection.commit()
    cur.close()
    flash("El corral se actualizó correctamente", "alert-success")
    return redirect(url_for('Corral'))
