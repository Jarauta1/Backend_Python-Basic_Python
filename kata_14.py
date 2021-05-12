inicio = int(input("Indica el inicio de la cuenta regresiva: "))

def cuenta_atras(inicio):
  while inicio > -1:
    if inicio != 0:
      print(inicio)
    else:
      print("BOOM")
    inicio -= 1

cuenta_atras(inicio)
