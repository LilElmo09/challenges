Objetivo:
Crear un programa en Python que simule un sistema de reservas para un pequeño teatro. El teatro tiene 5 filas con 10 asientos cada una. El programa debe permitir al usuario reservar asientos, cancelar reservas y mostrar el estado actual del teatro.

Contexto:
El teatro se representa como una matriz 5x10, donde cada elemento puede ser 0 (asiento disponible) o 1 (asiento reservado). El programa debe ofrecer un menú con opciones para reservar un asiento, cancelar una reserva y mostrar el estado actual de los asientos.

Prototipo de salida por el terminal:
Bienvenido al sistema de reservas del teatro.
1. Mostrar asientos
2. Reservar asiento
3. Cancelar reserva
4. Salir
Elige una opción: 1

Estado del teatro:
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

Elige una opción: 

Pistas:
1. Utiliza una matriz para representar los asientos del teatro.
2. Implementa una función para mostrar el estado actual de los asientos.
3. Implementa una función para reservar asientos. Asegúrate de verificar si el asiento ya está reservado.
4. Implementa una función para cancelar reservas. Verifica si el asiento está actualmente reservado antes de cancelar.
5. Usa un bucle para mostrar el menú de opciones y ejecutar la acción seleccionada hasta que el usuario decida salir.