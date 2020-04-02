from mysqlDb import mysql
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import *

def makeGraph(idAnimal):
    print("entro a hacer la grafica")
    #print( plt.style.available )
    #plt.style.use('fivethirtyeight')
    
    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT animalHistoriaFecha, animalHistoriaPeso FROM animalHistoria Where animalId = {0} ORDER BY animalHistoriaFecha'.format(idAnimal))
    data = list(cur.fetchall())
    cur.close()
    print(data)
    plt.style.use('ggplot')

    ages_x = []

    weight_y = []
    
    for animal in enumerate(data):
        listAnimal = list(animal)
        datos = animal[1]

        fechaStr = datos[0]
        fecha = datos[0]
        fecha = fechaStr.strftime('%Y-%m-%d')
        peso = datos[1]

        ages_x.append(fecha)
        weight_y.append(peso)

    plt.plot(ages_x, weight_y, linestyle='--', marker='o', label='Relación Peso/Fecha')
    plt.axis('auto')
    plt.ylabel('Peso en kg')
    plt.xlabel('Fecha')
    plt.title('Historial engorde del animal')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("static/grafica{0}.png".format(idAnimal))

    #Cierro la figura y limpio plt
    plt.cla()
    plt.clf()
    plt.close()
    plt.close('all')
    # plt.show()
