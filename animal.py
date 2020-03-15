from mysqlDb import mysql
from flask import Flask, render_template, url_for, request, redirect, session, flash


def animalInicio():
    print("PAGINA DE ANIMAL:")
    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT * FROM animal')
    data = list(cur.fetchall())
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT * FROM tipoanimal')
    tiposAnimal = list(cur.fetchall())
    cur.close()

    #Tremendo codigo para que el tipo de animal se vea el nombre y no el codigo en pantalla
    # tengo lista de tuplas inmutables, recorro cada tupla, paso a lista, modifico lista luego la paso a tubla y por ultimo la remplazo
    for index, animal in enumerate(data):
        listAnimal =  list(animal)
        for tanimal in tiposAnimal:
            if listAnimal[1] == tanimal[0]:
               listAnimal.insert(3, tanimal[1])
        animal = tuple(listAnimal)
        data[index] = animal

    return render_template("animal.html", animales=data, tipoanimales=tiposAnimal)


def animalAdd(identificador, tipoAnimal):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO animal (tipoAnimalId, identificadorAnimal)  VALUES (%s, %s)",
                (tipoAnimal, identificador))
    mysql.connection.commit()
    cur.close()

    flash("El animal se ingreso correctamente", "alert-success")
    return redirect(url_for('Animal'))


def animalDelete(id):
    cur = mysql.connection.cursor()
    cur.execute(
        'DELETE FROM animal WHERE animalId = {0}'.format(id))
    mysql.connection.commit()
    cur.close()
    flash("El animal se elimino correctamente", "alert-success")
    return redirect(url_for('Animal'))


def animalUpdate(identificador, tipoAnimal, id):
    cur = mysql.connection.cursor()
    cur.execute(
        'UPDATE animal SET tipoAnimalId = %s, identificadorAnimal = %s  WHERE animalId = %s', (tipoAnimal, identificador,  id))
    mysql.connection.commit()
    cur.close()
    flash("El animal se actualizó correctamente", "alert-success")
    return redirect(url_for('Animal'))
