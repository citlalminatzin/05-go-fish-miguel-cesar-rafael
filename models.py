#!/usr/bin/env python
"""
models.py
Modelos a utilizar para modelos de similitud geométrica
"""


def modelo_geom(longitudes: list[float], k: float) -> list[float]:
    """
    longitudes: list[float] lista de las lonigutudes de los peces
    k: float, pendiente aproximada
    """
    return [k * (long**3) for long in longitudes]


def modelo_circ(longitudes: list[float]) -> list[float]:
    """
    longitudes: list[float] ¿Qué significa longitudes?
    (Por favor elimina la pregunta y reemplazala con su respuesta)
    ...
    """
    ...  # Puedes eliminar esta línea


def pearson(x: list[float], y: list[float]):
    """Calcula el coeficiente de pearson"""
    n = len(x)

    sum_x = sum(x)
    sum_y = sum(y)
    sum_xx = sum([xi**2 for xi in x])
    sum_yy = sum([yi**2 for yi in y])
    sum_xy = sum([x[i]*y[i] for i in range(n)])

    num = (n * sum_xy) - (sum_x * sum_y)
    den = ((n * sum_xx - sum_x**2) * (n * sum_yy - sum_y**2)) ** 0.5

    return num / den


def calc_error(pred: list[float], truth: list[float]):
    """Calcula el error entre una predicción y la verdad del dataset"""

    n = len(pred)

    error = sum([(pred[i] - truth[i])**2 for i in range(n)]) / n

    return error

def main(): ...  # Puedes eliminar esta línea


if __name__ == "__main__":
    # Si necesitas hacer pruebas de tu función las puedes escribir acá
    main()
