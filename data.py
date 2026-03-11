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
    return long, peso
