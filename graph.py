import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def makeGraph():
    print("entro a hacer la grafica")
    #print( plt.style.available )
    #plt.style.use('fivethirtyeight')
    plt.style.use('ggplot')

    ages_x = [6, 12, 24, 36, 48]

    weight_y = [50, 70, 85, 105, 120]

    plt.plot(
        ages_x,
        weight_y,
        linestyle='--',
        marker='o',
        label='Relación Peso/Edad')

    plt.ylabel('Peso en kg')
    plt.xlabel('Edad en meses')
    plt.title('Historial del animal')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("static/grafica.png")

    #Cierro la figura y limpio plt
    plt.cla()
    plt.clf()
    plt.close()
    plt.close('all')
    # plt.show()
