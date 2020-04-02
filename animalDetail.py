from mysqlDb import mysql
from flask import Flask, render_template, url_for, request, redirect, session, flash


def getAnimalDetail(animalId):
    print("DETALLE DEL ANIMAL:")
    cur = mysql.connection.cursor()

    cur.execute(""" SELECT animalIdInt, tipoAnimalNom, compraFecha, compraPrecio, corralNom 
                      FROM feedlot.animal, feedlot.tipoanimal, feedlot.compra, feedlot.corralanimal, feedlot.corral 
                      WHERE animal.animalId = {0}
                      AND  animal.tipoAnimalId = tipoanimal.tipoAnimalId 
                      AND animal.animalId = compra.animalId 
                      AND animal.animalId = corralanimal.animalId 
                      AND corral.corralId = corralanimal.corralId """.format(animalId))

    data = cur.fetchall()
    cur.close()
    return data
