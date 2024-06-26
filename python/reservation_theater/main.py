#sistema de reserva para un teatro
#main hub
#1. mostrar los asientos
#2. reservar asientos
#3. cancelar  reserva
#4. salir

#opcion 1
'''
Estado del teatro
0 1 0 0 0 0 0 1 0 0
0 0 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 1 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 1 0 1 1
elige una opcion
'''
# si es posible ponerle del 1 al 10 y de a a la j

exit = True
def  main():
    print('Bienvenido al sistema de reservas del teatro')
    while exit:
        respuesta = presentacion()     
        comprobar_respuesta(respuesta)  
#se muestra el menu
def presentacion ():
    print('1. Mostrar asientos')
    print('2. Reservar asientos')
    print('3. Cancelar asientos')
    print('4. Salir')
    try:
        respuesta = int(input('Opcion: '))
    except:
        print('Respuesta invalida')
    return respuesta
#comprueba la respuesta
def comprobar_respuesta(respuesta):
    global exit
    if respuesta == 1:
        mostrar_asientos()
    elif respuesta == 2:
        reservar_asientos()
    elif respuesta == 3:
        cancelar_asiento()
    elif respuesta == 4:
        exit = False
        input('Gracias por usar nuestros servicios')
    else:
        print('Respuesta invalida')
def mostrar_asientos():
    print('mostando asientos')
    input()
def reservar_asientos():
    mostrar_asientos()
    input('que asiento quieres reservar:')
def cancelar_asiento():
    mostrar_asientos()
    input('Que asiento quieres cancelar: ')
if __name__ == '__main__':
    main()