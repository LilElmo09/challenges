Objetivo:
Crear un programa en Python que simule un juego de adivinanzas donde el usuario debe adivinar un número secreto generado aleatoriamente entre 1 y 100. El programa debe indicar al usuario si su intento es demasiado alto, demasiado bajo, o correcto. Además, debe contar y mostrar el número de intentos realizados hasta adivinar el número.

Contexto:
El juego genera un número secreto al azar entre 1 y 100 al inicio. Luego, el usuario intenta adivinar este número. Después de cada intento, el programa informa al usuario si su adivinanza es correcta, o si debe intentar con un número más alto o más bajo. El juego termina cuando el usuario adivina el número secreto.

Prototipo de salida por el terminal:

Intenta adivinar el número entre 1 y 100.
Tu intento: 50
Demasiado bajo.
Tu intento: 75
Demasiado alto.
Tu intento: 62
¡Correcto! Adivinaste el número en 3 intentos.


Pistas:
1. Utiliza la biblioteca random para generar el número secreto.
2. Implementa un bucle para permitir al usuario hacer múltiples intentos hasta adivinar el número.
3. Usa condicionales para comparar el intento del usuario con el número secreto y dar pistas.
4. Mantén un contador de intentos y muéstralo cuando el usuario adivine el número.