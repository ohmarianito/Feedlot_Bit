from mysqlDb import mysql
from flask import Flask, render_template, url_for, request, redirect, session, flash


def ventaInicio():
    print("PAGINA DE VENTA:")
    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT * FROM venta ORDER BY ventaFecha DESC')
    data = list(cur.fetchall())
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT * FROM animal')
    dataAnimal = list(cur.fetchall())
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT * FROM frigorifico')
    dataFrigorifico = list(cur.fetchall())
    cur.close()

    # Tremendo codigo para que el tipo de animal se vea el nombre y no el codigo en pantalla
    # tengo lista de tuplas inmutables, recorro cada tupla, paso a lista, modifico lista luego la paso a tubla y por ultimo la remplazo
    for index, venta in enumerate(data):
        listVenta = list(venta)
        for animal in dataAnimal:
            if listVenta[2] == animal[0]:
                listVenta.insert(5, animal[2])

        for frigorifico in dataFrigorifico:
            if listVenta[3] == frigorifico[0]:
                listVenta.insert(6, frigorifico[1])

        venta = tuple(listVenta)
        data[index] = venta

    return render_template("ventaAnimal.html", ventas=data, animales=dataAnimal, frigorificos=dataFrigorifico)


def ventaAdd(fecha, idAnimal, idFrigorifico, precio):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO venta (ventaFecha, animalId, frigorificoId, ventaPrecio)  VALUES (%s, %s, %s, %s)",
                (fecha, idAnimal, idFrigorifico, precio))
    mysql.connection.commit()
    cur.close()

    flash("La venta se ingreso correctamente", "alert-success")
    return redirect(url_for('Venta'))


def ventaDelete(id):
    cur = mysql.connection.cursor()
    cur.execute(
        'DELETE FROM venta WHERE ventaId = {0}'.format(id))
    mysql.connection.commit()
    cur.close()
    flash("La venta se elimino correctamente", "alert-success")
    return redirect(url_for('Venta'))


def ventaUpdate(fecha, animalId, frigorificoId, precio, id):
    cur = mysql.connection.cursor()
    cur.execute(
        'UPDATE venta SET ventaFecha = %s, animalId = %s, frigorificoId = %s, ventaPrecio = %s WHERE ventaId = %s', (fecha, animalId, frigorificoId, precio, id))
    mysql.connection.commit()
    cur.close()
    flash("La venta se actualizó correctamente", "alert-success")
    return redirect(url_for('Venta'))
