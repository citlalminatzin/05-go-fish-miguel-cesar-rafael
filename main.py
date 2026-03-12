#!/usr/bin/env python

import matplotlib.pyplot as plt
from models import calc_error, modelo_geom, modelo_circ
from data import read_data, rls


def plot_data(x: list[float], y: list[float]):
    x3k = [(xi**3) / 1000 for xi in x]

    fig, ax = plt.subplots()
    ax.plot(x3k, y, "o")
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
    data: list[list] = read_data()
    plot_data(data[0], data[1])


if __name__ == "__main__":
    main()
