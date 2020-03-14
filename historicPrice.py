from mysqlDb import mysql
from flask import Flask, render_template, url_for, request, redirect, session, flash


def precioHistoriaInicio():
    print("HISTORIA DEL PRECIO:")
    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT * FROM precioreferencia ORDER BY precioReferenciaFecha DESC')
    data = cur.fetchall()
    cur.close()
    return render_template("priceReference.html", historias=data)


def precioHistoriaAdd(fecha, precio):
    # Crear cursor
    cur = mysql.connection.cursor()

    # Preparar el query y ejecutar query
    cur.execute(
        "INSERT INTO precioreferencia (precioReferenciaFecha, precioReferenciaPrecio) VALUES (%s, %s)", (fecha, precio))
    mysql.connection.commit()

    # Cerramos Conexion
    cur.close()

    flash("El registro se ingreso correctamente", "alert-success")
    return redirect(url_for('PrecioHistoria'))


def precioHistoriaDelete(id):
    cur = mysql.connection.cursor()
    cur.execute(
        'DELETE FROM precioreferencia WHERE precioReferenciaId = {0}'.format(id))
    mysql.connection.commit()
    cur.close()
    flash("El registro se elimino correctamente", "alert-success")
    return redirect(url_for('PrecioHistoria'))


def precioHistoriaUpdate(fecha, precio, idPrecioHistoria):
    cur = mysql.connection.cursor()
    cur.execute('UPDATE precioreferencia SET precioReferenciaFecha = %s, precioReferenciaPrecio = %s WHERE precioReferenciaId = %s', (fecha, precio, idPrecioHistoria))
    mysql.connection.commit()
    cur.close()
    flash("El registro se actualizó correctamente", "alert-success")
    return redirect(url_for('PrecioHistoria'))
