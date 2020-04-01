from mysqlDb import mysql
from flask import Flask, render_template, url_for, request, redirect, session, flash
from datetime import date
from dateutil import parser

def engordeInicio():
    print("PAGINA DE ENGORDE:")
    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT * FROM engorde ORDER BY engordeFecha DESC')
    data = list(cur.fetchall())
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT * FROM corral')
    dataCorral = list(cur.fetchall())
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT * FROM tipoRacion')
    dataRaciones = list(cur.fetchall())
    cur.close()

    # Tremendo codigo para que el tipo de animal se vea el nombre y no el codigo en pantalla
    # tengo lista de tuplas inmutables, recorro cada tupla, paso a lista, modifico lista luego la paso a tubla y por ultimo la remplazo
    for index, engorde in enumerate(data):
        listEngorde = list(engorde)

        for corral in dataCorral:
            if listEngorde[0] == corral[0]:
                listEngorde.insert(4, corral[1])
        
        for tipoRacion in dataRaciones:
            if listEngorde[2] == tipoRacion[0]:
                listEngorde.insert(5, tipoRacion[1])
        engorde = tuple(listEngorde)
        data[index] = engorde

    return render_template("engorde.html", engordes=data, corrales=dataCorral, raciones=dataRaciones)


def engordeAdd(idCorral, idTipoRacion, fechaEngorde):
    cur = mysql.connection.cursor()
    cur.execute('SELECT MAX(engordeId) FROM engorde WHERE corralId = {0}'.format(idCorral))
    idEngordeList = cur.fetchall()
    cur.close()    

    idEngordeTupla = idEngordeList[0]
    if idEngordeTupla[0] == None:
        idEngorde = 1
    else:
        idEngorde = idEngorde + 1

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO engorde (corralId, engordeId, tipoRacionId, engordeFecha)  VALUES (%s, %s, %s, %s)", (idCorral, idEngorde, idTipoRacion, fechaEngorde))
    mysql.connection.commit()
    cur.close()

    flash("El engorde se ingreso correctamente", "alert-success")
    return redirect(url_for('Engorde'))


def engordeDelete(idCorral, idEngorde):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM engorde WHERE corralId = {0} And engordeId = {1}".format(idCorral, idEngorde))
    mysql.connection.commit()
    cur.close()
    flash("El engorde se elimino correctamente", "alert-success")
    return redirect(url_for('Engorde'))


def engordeUpdate(idCorral, idEngorde, idTipoRacion, fechaEngorde):
    cur = mysql.connection.cursor()
    cur.execute(
        'UPDATE engorde SET tipoRacionId = %s, engordeFecha = %s WHERE corralId = %s and engordeId = %s', (idTipoRacion, fechaEngorde, idCorral,  idEngorde))
    mysql.connection.commit()
    cur.close()
    flash("El engorde se actualizó correctamente", "alert-success")
    return redirect(url_for('Engorde'))
