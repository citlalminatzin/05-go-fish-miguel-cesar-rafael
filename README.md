[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/jw8MUQHd)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23030697)
# Pon aquí el título de tu práctica o no, no soy tu papá

(Si no eliminas esta línea lloro) Este es un archivo de ejemplo donde debes de colocar la respuesta a tus ejercicios, piénsalo como tu reporte de práctica. Aquí puedes introducir el problema y definir los términos que consideres apropiados de forma concisa.

## Integrantes

(Si no eliminas esta línea lloro) Escribe tus integrantes iniciando por apellido de forma alfabética

- (Si no modificas esta línea lloro) Babilonia, Aureliano
- (Si no modificas esta línea lloro) Buendía, Aureliano
- (Si no modificas esta línea lloro) Segundo, Aureliano


## Uso e instalación

(Si no eliminas esta línea lloro) Aquí escribe qué necesitas que instale para ejecutar tu código, por ejemplo:

- `matplotlib`

(Si no eliminas esta línea lloro) Y dime cómo debería ejecutar tu código y en qué orden. Recuerda que antes de ejecutar tu código leeré tu `README.md`. Por ejemplo la manera en la que propongo que organizes tu código es

- `main.py`: Contiene el código para graficar cada uno de los tres ejercicios
- `` (Por favor modifica esta línea)

## Ejercicio 1

(Por favor modifica esta línea, lo suplico por piedad) Aquí puedes colocar la discusión del modelo, tu interpretación, el efecto de las condiciones iniciales. No tiene que ser perfecto, pero entre más casos puedas cubrir mejor

## Ejercicio 2

(Por favor modifica esta línea, tú puedes yo creo en ti) Puedes darle formato de **negritas**, *itálicas*, incluir texto matemático $x\approx 1, \epsilon > 0$, [enlaces](https://www.markdownguide.org/cheat-sheet/), `código`,

```python
# Esto es un ejemplo, lo puedes quitar
print("Código en bloque")
```

(Si no eliminas esta línea lloro) También puedes incluir citas

> Por favor elimina esta cita

(Si no eliminas esta línea lloro) Puedes incluir notas al pie [^1].


## Ejercicio 3

Planteamiento: Ahora añadiremos una dimensión extra a nuestra tabla anterior. Supongamos que además
de los datos anteriores también tenemos disponible la circunferencia máxima de cada pez
Realice el ajuste del nuevo modelo en términos de la circunferencia ¿Cómo queda la
fórmula explicita del modelo?¿Qué tan bueno es el ajuste?

Para esta solucion considera la Tabla siguiente: 

| Medida | Pez 1 | Pez 2 | Pez 3 | Pez 4 | Pez 5 | Pez 6 | Pez 7 |
| ------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Longitud (cm) | 36.81 | 31.77 | 43.82 | 36.82 | 32.07 | 45.07 | 35.89 |
| Peso (kg) | 0.78 | 0.47 | 1.16 | 0.74 | 0.44 | 1.40 | 0.64 |
| Circunferencia máxima (cm) | 31.00 | 29.50 | 35.70 | 31.10 | 28.80 | 38.10 | 30.50 |

A partir de los nuevos supuestos,

$$V \propto l_e A_{prom}, \quad l_e \propto l, \quad A_{prom} \propto A_{max}$$

y usando que

$$C = 2\pi r,$$

se tiene que

$$A_{max} = \pi r^2 = \frac{C^2}{4\pi}.$$

Por tanto,

$$A_{max} \propto C^2,$$

y entonces:

$$V \propto l C^2.$$

Para el nuevo modelo se considera que el peso del pez es proporcional a su volumen y que dicho volumen puede aproximarse mediante la longitud y la circunferencia máxima.

El modelo propuesto es:

$$
W = K\ l\ C^2
$$

donde:

- $W$ es el peso del pez
- $l$ es la longitud del pez
- $C$ es la circunferencia máxima
- $K$ es una constante que se estima con los datos

Para ajustar el modelo se define:

$$
x_i = l_i\ C_i^2
$$

y se calcula $K$ por mínimos cuadrados con la fórmula:

$$
K = \frac{\sum (x_i W_i)}{\sum (x_i^2)}
$$

Con los datos de la tabla se obtuvo:

$$
K \approx 2.0502 \times 10^{-5}
$$

Por lo tanto, la fórmula explícita del modelo queda:

$$
W \approx 2.0502 \times 10^{-5}\ l\ C^2
$$

Los pesos estimados con este modelo son cercanos a los pesos reales, por lo que el ajuste puede considerarse bueno. Esto indica que, en esta muestra, incorporar la circunferencia máxima mejora la estimación del peso, ya que permite distinguir mejor entre peces más delgados y peces más anchos.




## Conclusión

(Por favor modifica esta línea bro, es la última que tienes que modificar bro, por favor bro) Es buena práctica concluir tus prácticas. ¿Qué te llevas? ¿Sientes que fue relevante para ti? ¿Se te complicó algún aspecto? ¿Hubo algún resultado que contradijera tu intuición? 

---

[^1]: Sólo soy una nota al pie, elimíname bro, por favor bro.
