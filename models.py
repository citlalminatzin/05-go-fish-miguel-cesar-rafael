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
    ...


def calc_error(pred: list[float], truth: list[float]):
    """Calcula el error entre una predicción y la verdad del dataset"""


def main(): ...  # Puedes eliminar esta línea


if __name__ == "__main__":
    # Si necesitas hacer pruebas de tu función las puedes escribir acá
    main()
