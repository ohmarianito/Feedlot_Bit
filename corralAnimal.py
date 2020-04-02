from mysqlDb import mysql
from flask import Flask, render_template, url_for, request, redirect, session, flash

def corralAnimalInicio(corralId):
    print("CORRAL:")
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM corralAnimal WHERE corralId = {0}'.format(corralId))
    data = list(cur.fetchall())
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT * FROM corral WHERE corralId = {0}'.format(corralId))
    dataCorral = list(cur.fetchall())
    cur.close()
    
    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT * FROM animal')
    dataAnimal = list(cur.fetchall())
    cur.close()
    
    # Tremendo codigo para que el tipo de animal se vea el nombre y no el codigo en pantalla
    # tengo lista de tuplas inmutables, recorro cada tupla, paso a lista, modifico lista luego la paso a tubla y por ultimo la remplazo
    for index, corralAnimal in enumerate(data):
        listCorralAnimal = list(corralAnimal)

        for corral in dataCorral:
            if listCorralAnimal[0] == corral[0]:
                listCorralAnimal.insert(4, corral[1])
        
        for animal in dataAnimal:
            if listCorralAnimal[1] == animal[0]:
                listCorralAnimal.insert(5, animal[2])

        corralAnimal = tuple(listCorralAnimal)
        data[index] = corralAnimal
        
    return render_template("corralAnimal.html", corralAnimales=data, corrales=dataCorral, animales=dataAnimal)


def corralAnimalAdd(corralId, animalId, corralFecha, corralFechaFin):
    # Crear cursor
    cur = mysql.connection.cursor()
    # Preparar el query y ejecutar query
    query = "INSERT INTO corralAnimal (corralId, animalId, corralFecha, corralFechaFin) VALUES ({0}, {1}, '{2}', '{3}')".format(corralId, animalId, corralFecha, corralFechaFin)
    cur.execute(query)
    mysql.connection.commit()

    # Cerramos Conexion
    cur.close()

    flash("El animal se ingreso al corral correctamente", "alert-success")

    #return redirect(url_for('CorralAnimal/{0}').format(corralId))
    return redirect(url_for('CorralAnimal', idCorral=corralId))


def corralAnimalDelete(corralId, animalId, corralFecha):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM corralAnimal WHERE corralId = {0} and animalId = {1} And corralFecha = '{2}'".format(corralId, animalId, corralFecha))
    mysql.connection.commit()
    cur.close()
    flash("El animal se elimino del corral correctamente", "alert-success")
    return redirect(url_for('CorralAnimal', idCorral=corralId))


def corralAnimalUpdate(corralId, animalId, corralFecha, corralFechaFin):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE corralAnimal SET corralFechaFin = '{3}' WHERE corralId = {0} And animalId = {1} And corralFecha = '{2}'".format(corralId, animalId, corralFecha, corralFechaFin))
    mysql.connection.commit()
    cur.close()
    flash("El corral se actualizó correctamente", "alert-success")
    return redirect(url_for('CorralAnimal', idCorral=corralId))
