# numero = 8

from random import *

def generarNumeroAleatorio(minimo,maximo):
    try:
        if minimo > maximo:
            aux = minimo
            minimo = maximo
            maximo = aux
        return randint(minimo,maximo)
    except TypeError:
        print("Debes escribir numeros")
        return -1

numero = generarNumeroAleatorio(1,10)

intento = 0
encontrado = False

while not encontrado:
    valor = int(input("Introduce un número: "))
    if valor < numero:
        intento = intento + 1
        print("El número que has introducido es menor.")
    elif valor > numero:
        intento += 1
        print("El número que has introducido es mayor.")
    else:
        intento += 1
        encontrado = True
        print("¡Has acertado!")
        print("El número es el " + str(numero))
        print("Tan solo te ha costado " + str(intento) + " intentos.")