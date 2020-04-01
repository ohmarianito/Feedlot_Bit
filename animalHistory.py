from mysqlDb import mysql
from flask import Flask, render_template, url_for, request, redirect, session, flash
from datetime import date
from dateutil import parser

def historiaInicio():
    print("PAGINA DE HISTORIA:")
    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT * FROM animalHistoria ORDER BY animalHistoriaFecha DESC')
    data = list(cur.fetchall())
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT * FROM animal')
    dataAnimal = list(cur.fetchall())

    # Tremendo codigo para que el tipo de animal se vea el nombre y no el codigo en pantalla
    # tengo lista de tuplas inmutables, recorro cada tupla, paso a lista, modifico lista luego la paso a tubla y por ultimo la remplazo
    for index, historia in enumerate(data):
        listHistoria = list(historia)
        for animal in dataAnimal:
            if listHistoria[0] == animal[0]:
                listHistoria.insert(4, animal[2])
        historia = tuple(listHistoria)
        data[index] = historia

    return render_template("animalHistoria.html", historias=data, animales=dataAnimal)


def historiaAdd(idAnimal, fechaAnimal, pesoAnimal, obsAnimal):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO animalHistoria (animalId, animalHistoriaFecha, animalHistoriaPeso, animalHistoriaObs)  VALUES (%s, %s, %s, %s)", (idAnimal, fechaAnimal, pesoAnimal, obsAnimal))
    mysql.connection.commit()
    cur.close()

    flash("La historia se ingreso correctamente", "alert-success")
    return redirect(url_for('AnimalHistoria'))


def historiaDelete(idAnimal, fechaAnimal):
    fecha = parser.parse(fechaAnimal)

    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM animalHistoria WHERE animalId = {0} And animalHistoriaFecha = '{1}'".format(idAnimal, fecha.date()))
    mysql.connection.commit()
    cur.close()
    flash("La historia se elimino correctamente", "alert-success")
    return redirect(url_for('AnimalHistoria'))


def historiaUpdate(idAnimal, fechaAnimal, pesoAnimal, obsAnimal):
    cur = mysql.connection.cursor()
    cur.execute(
        'UPDATE animalHistoria SET animalHistoriaPeso = %s, animalHistoriaObs = %s WHERE animalId = %s and animalHistoriaFecha = %s', (pesoAnimal, obsAnimal, idAnimal,  fechaAnimal))
    mysql.connection.commit()
    cur.close()
    flash("La historia se actualizó correctamente", "alert-success")
    return redirect(url_for('AnimalHistoria'))
