Objetivo:
Desarrollar un programa en Python que encuentre el número faltante en una lista de enteros secuenciales que va desde 0 hasta n. La lista está desordenada y falta exactamente un número.

Contexto:
Se te da una lista de números enteros que empieza en 0 y termina en n, pero uno de los números en el rango está ausente. La lista puede estar en cualquier orden. El objetivo es encontrar el número que falta.

Prototipo de salida por el terminal:
La lista es: [3, 7, 1, 2, 8, 4, 5, 0]
El número faltante es: 6

Pistas:
1. La suma de una serie de números enteros desde 0 hasta n se puede calcular con la fórmula n*(n+1)/2.
2. Calcula la suma esperada de la lista completa (incluyendo el número faltante) usando la fórmula mencionada.
3. Suma todos los números presentes en la lista dada.
4. Resta la suma de los números presentes en la lista de la suma esperada para encontrar el número faltante.
