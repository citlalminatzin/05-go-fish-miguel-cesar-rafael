#!/usr/bin/env python

import matplotlib.pyplot as plt
from models import calc_error, modelo_geom, modelo_circ
from data import read_data, rls


def plot_data(x: list[float], y: list[float]):
    x3 = [xi**3 for xi in x]

    fig, ax = plt.subplots()
    ax.plot(x3, y, "o")
    ax.set_title("Datos de los Peces")
    ax.set_xlabel("Volumen en cm²")
    ax.set_ylabel("Peso en kg")
    ax.grid()
    plt.savefig("media/data.png")
    plt.close()

    return None


def plot_model(model: list[float], longitudes: list[float], pesos: list[float]):
    x3 = [xi**3 for xi in longitudes]

    fig, ax = plt.subplots()
    ax.plot(x3, model, "-ro", label="datos del modelo geometrico")
    ax.plot(x3, pesos, "o", label="peso")
    ax.set_title("Modelo geometrico vs datos")
    ax.set_xlabel("Volumen en $cm²$")
    ax.set_ylabel("Peso en kg")
    ax.grid()
    plt.savefig("media/geometrico.png")


def make_plot():
    """
    (Si no modificas esta cadena de texto lloro)
    Si repites mucho tu código para
    graficar puedes guardarlo en una función
    """
    ...  # Esto significa implementación pendiente, lo puedes eliminar


def main():
    data: list[list[float]] = read_data()

    longitudes: list[float] = data[0]
    pesos: list[float] = data[1]
    longitudes_cubo: list[float] = [longitud**3 for longitud in longitudes]

    plot_data(longitudes, pesos)

    k = rls(longitudes_cubo, pesos)
    aprox = modelo_geom(longitudes, k)

    plot_model(aprox, longitudes, pesos)


if __name__ == "__main__":
    main()
