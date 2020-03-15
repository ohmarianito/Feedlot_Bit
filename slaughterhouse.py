from mysqlDb import mysql
from flask import Flask, render_template, url_for, request, redirect, session, flash


def frigorificoInicio():
    print("FRIGORÍFICO:")
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM frigorifico')
    data = cur.fetchall()
    cur.close()
    return render_template("frigorifico.html", frigorificos=data)


def frigorificoAdd(nombre):
    # Crear cursor
    cur = mysql.connection.cursor()
    # Preparar el query y ejecutar query
    query = "INSERT INTO frigorifico (frigorificoNom) VALUES ('" + \
        nombre + "')"
    cur.execute(query)
    mysql.connection.commit()

    # Cerramos Conexion
    cur.close()

    flash("El tipo de animal se ingreso correctamente", "alert-success")
    return redirect(url_for('Frigorifico'))


def frigorificoDelete(id):
    cur = mysql.connection.cursor()
    cur.execute(
        'DELETE FROM frigorifico WHERE frigorificoId = {0}'.format(id))
    mysql.connection.commit()
    cur.close()
    flash("El tipo de animal se elimino correctamente", "alert-success")
    return redirect(url_for('Frigorifico'))


def frigorificoUpdate(nombre, idfrigorifico):
    cur = mysql.connection.cursor()
    cur.execute(
        'UPDATE frigorifico SET frigorificoNom = %s WHERE frigorificoId = %s', (nombre, idfrigorifico))
    mysql.connection.commit()
    cur.close()
    flash("El tipo de animal se actualizó correctamente", "alert-success")
    return redirect(url_for('Frigorifico'))
