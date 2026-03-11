#!/usr/bin/env python

import matplotlib.pyplot as plt
from models import calc_error, modelo_geom, modelo_circ
from data import read_data


def plot_data():
    data = read_data()

    long = data[0]
    peso = data[1]

    vol = []
    for elem in long:
        vol.append((elem * elem * elem) / 1000)

    fig, ax = plt.subplots()
    ax.plot(vol, peso, "o")
    ax.set_title("Datos de los Peces")
    ax.set_xlabel("Volumen en $1000cm²$ por unidad")
    ax.set_ylabel("Peso en kg")
    ax.grid()
    plt.savefig("media/data.png")
    plt.close()


def make_plot():
    """
    (Si no modificas esta cadena de texto lloro)
    Si repites mucho tu código para
    graficar puedes guardarlo en una función
    """
    ...  # Esto significa implementación pendiente, lo puedes eliminar


def main():
    plot_data()


if __name__ == "__main__":
    main()
