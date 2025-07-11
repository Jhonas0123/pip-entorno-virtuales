# gracion de grafica con matplotlib
import matplotlib.pyplot as plt


def generate_pie_chart():
    labels = ['a', 'b', 'c']
    values = [200, 34, 200]

    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig("pie.png")
    plt.close() 