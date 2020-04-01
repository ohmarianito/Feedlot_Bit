from mysqlDb import mysql
from graph import makeGraph
from flask import Flask, render_template


def historiaAnimal():
    makeGraph()
    return render_template("animalHistory.html")
