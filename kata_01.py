def semaforo(color):
    if color == "verde":
        print("Cruzar la calle")
    elif color == "rojo":
        print("Esperar")
    else:
        print("Sigue esperando")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    semaforo("verde")