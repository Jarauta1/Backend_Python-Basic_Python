def compra(cantidad):
    if cantidad > 100:
        cuenta = cantidad - ((cantidad*10)/100)
    else:
        cuenta = cantidad
    print("La cuenta es: " + str(cuenta) + "€")

if __name__ == '__main__':
    compra(1000)