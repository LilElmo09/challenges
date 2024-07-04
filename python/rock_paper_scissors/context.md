Objetivo:
Desarrollar un programa en Python que implemente el juego "Piedra, Papel o Tijera" contra la computadora. El juego debe permitir al usuario jugar múltiples rondas contra la computadora, manteniendo un registro de las victorias del usuario, las victorias de la computadora y los empates.

Contexto:
El usuario puede elegir entre piedra, papel o tijera en cada ronda, mientras que la computadora elige de manera aleatoria. El juego compara las elecciones para determinar el ganador de cada ronda. El juego termina cuando el usuario decide no jugar más, mostrando el resultado final.

Reglas:
- Piedra gana a Tijera.
- Tijera gana a Papel.
- Papel gana a Piedra.

Prototipo de salida por el terminal:

Elige: Piedra, Papel o Tijera (o escribe 'salir' para terminar el juego): Piedra
Computadora elige: Tijera
¡Ganaste esta ronda!

Elige: Piedra, Papel o Tijera (o escribe 'salir' para terminar el juego): salir
Resultados finales: Ganaste 1 vez(es), la computadora ganó 0 vez(es), empates: 0.
Gracias por jugar.

Pistas:
1. Utiliza la biblioteca random para que la computadora elija entre piedra, papel o tijera.
2. Implementa un bucle para permitir múltiples rondas de juego.
3. Usa condicionales para determinar el ganador de cada ronda.
4. Mantén un registro del número de victorias del usuario, victorias de la computadora y empates.
5. Proporciona una opción para que el usuario pueda salir del juego en cualquier momento.