from mysqlDb import mysql
from flask import Flask, render_template, url_for, request, redirect, session, flash


def tipoAnimalInicio():
    print("TIPO ANIMAL:")
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tipoanimal')
    data = cur.fetchall()
    cur.close()
    return render_template("tipoAnimal.html", animales=data)


def tipoAnimalAdd(nombre):
    # Crear cursor
    cur = mysql.connection.cursor()
    # Preparar el query y ejecutar query
    query = "INSERT INTO tipoanimal (tipoAnimalNom) VALUES ('" + \
        nombre + "')"
    cur.execute(query)
    mysql.connection.commit()

    # Cerramos Conexion
    cur.close()

    flash("El tipo de animal se ingreso correctamente", "alert-success")
    return redirect(url_for('TipoAnimal'))


def tipoAnimalDelete(id):
    cur = mysql.connection.cursor()
    cur.execute(
        'DELETE FROM tipoanimal WHERE tipoAnimalId = {0}'.format(id))
    mysql.connection.commit()
    cur.close()
    flash("El tipo de animal se elimino correctamente", "alert-success")
    return redirect(url_for('TipoAnimal'))


def tipoAnimalUpdate(nombre, idTipoAnimal):
    cur = mysql.connection.cursor()
    cur.execute(
        'UPDATE tipoanimal SET tipoAnimalNom = %s WHERE tipoAnimalId = %s', (nombre, idTipoAnimal))
    mysql.connection.commit()
    cur.close()
    flash("El tipo de animal se actualizó correctamente", "alert-success")
    return redirect(url_for('TipoAnimal'))
