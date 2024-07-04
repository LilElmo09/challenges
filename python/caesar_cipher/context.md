Objetivo:
Crear un programa en Python que implemente el algoritmo de cifrado César. El programa debe ser capaz de cifrar y descifrar texto basado en un desplazamiento (clave) proporcionado por el usuario.

Contexto:
El cifrado César es una técnica de cifrado muy simple utilizada en criptografía. Consiste en desplazar cada letra del texto original un número determinado de posiciones en el alfabeto. Por ejemplo, con un desplazamiento de 3, la A se convierte en D, la B en E, y así sucesivamente. El descifrado se realiza invirtiendo el desplazamiento.

Requisitos:
- El programa debe solicitar al usuario si desea cifrar o descifrar.
- Luego, debe pedir el texto a procesar y el valor de desplazamiento (clave).
- El alfabeto debe considerar tanto mayúsculas como minúsculas.
- Los caracteres que no sean letras deben permanecer inalterados.
- El programa debe mostrar el texto resultante después de aplicar el cifrado o descifrado.

Prototipo de salida por el terminal:

¿Deseas cifrar o descifrar? cifrar
Introduce el texto: Hola, Mundo!
Introduce el desplazamiento (clave): 3
Texto cifrado: Krod, Pxqgr!


Pistas:
1. Puedes usar las funciones ord() y chr() para convertir entre caracteres y sus correspondientes valores ASCII.
2. Considera el alfabeto como un ciclo, donde después de la 'Z' viene la 'A', y lo mismo para las minúsculas.
3. Asegúrate de tratar de manera diferente las mayúsculas y las minúsculas.
4. Para los caracteres que no son letras, simplemente mantenlos igual sin aplicar el desplazamiento.