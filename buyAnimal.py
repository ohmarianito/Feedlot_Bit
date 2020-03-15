from mysqlDb import mysql
from flask import Flask, render_template, url_for, request, redirect, session, flash


def compraInicio():
    print("PAGINA DE COMPRA:")
    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT * FROM compra ORDER BY compraFecha DESC')
    data = list(cur.fetchall())
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT * FROM animal')
    dataAnimal = list(cur.fetchall())
    cur.close()

    # Tremendo codigo para que el tipo de animal se vea el nombre y no el codigo en pantalla
    # tengo lista de tuplas inmutables, recorro cada tupla, paso a lista, modifico lista luego la paso a tubla y por ultimo la remplazo
    for index, compra in enumerate(data):
        listCompra = list(compra)
        for animal in dataAnimal:
            if listCompra[2] == animal[0]:
                listCompra.insert(4, animal[2])
        compra = tuple(listCompra)
        data[index] = compra

    return render_template("compraAnimal.html", compras=data, animales=dataAnimal)


def compraAdd(fecha, idAnimal, precio):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO compra (compraFecha, animalId, compraPrecio)  VALUES (%s, %s, %s)",
                (fecha, idAnimal, precio))
    mysql.connection.commit()
    cur.close()

    flash("La compra se ingreso correctamente", "alert-success")
    return redirect(url_for('Compra'))


def compraDelete(id):
    cur = mysql.connection.cursor()
    cur.execute(
        'DELETE FROM compra WHERE compraId = {0}'.format(id))
    mysql.connection.commit()
    cur.close()
    flash("La compra se elimino correctamente", "alert-success")
    return redirect(url_for('Compra'))


def compraUpdate(fecha, animalId, precio, id):
    cur = mysql.connection.cursor()
    cur.execute(
        'UPDATE compra SET compraFecha = %s, animalId = %s, compraPrecio = %s WHERE compraId = %s', (fecha, animalId, precio,  id))
    mysql.connection.commit()
    cur.close()
    flash("La compra se actualizó correctamente", "alert-success")
    return redirect(url_for('Compra'))
