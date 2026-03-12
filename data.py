#!/usr/bin/env python

import csv


def read_data(path="data/pescados.csv"):
    """Lee los datos del csv y los devuelve en una tupla de dos listas"""
    long = []
    peso = []
    with open(path, newline="") as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader, None)
        for row in spamreader:
            long.append(float(row[0]))
            peso.append(float(row[1]))
    return [long, peso]


# De https://github.com/LeninPA/tm1-2026-2/tree/main/01-regresion
def rls(x: list[float], y: list) -> float:
    n = len(x)

    xy = [xi * yi for xi, yi in zip(x, y)]
    x2 = [xi**2 for xi in x]

    suma_x = sum(x)
    avg_x = suma_x / n
    suma_y = sum(y)
    avg_y = suma_y / n
    suma_xy = sum(xy)
    suma_x2 = sum(x2)

    alfa = (suma_xy - avg_y * suma_x) / (suma_x2 - avg_x * suma_x)

    return alfa
