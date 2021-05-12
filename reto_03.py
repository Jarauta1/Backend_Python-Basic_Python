billete_cinco = 0
billete_diez = 0
billete_veinte = 0
billete_cincuenta = 0
billete_cien = 0
billete_quinientos = 0
coste_total = 0

menu = {}
precios = {}
num_plato = 1
num_pedido = 1
fin_platos = False
fin_pedido = False
pedido_correcto = False

plato = ""
precio = ""
continuar = ""
pedido = ""

indice_pedido = 0
pedido_realizado = {}

precio_pedido = 0
indice_pagar = 0


def introducir_menu():
  global plato
  plato = input("Plato a introducir al menú: ")
  menu[key] = plato
  global precio
  precio = input("Precio del plato: ")
  precios[key] = precio

def mostrar_menu():
  print("Tenemos estos platos en el menú:")
  for key,value in menu.items():
    print(key, value)

def introducir_pedido():
  global pedido
  global precio_pedido
  global pedido_correcto
  global indice_pedido
  pedido = input("¿Qué desea tomar?: ")
  
  for key,value in menu.items():
    if value == pedido:
      opcion_plato = key
      pedido_realizado["Plato"+str(indice_pedido)] = pedido
      for key,value in precios.items():
        if opcion_plato == key:
          pedido_realizado["Precio"+str(indice_pedido)] = value
          indice_pedido += 1
          pedido_correcto = True
    if pedido_correcto ==  False:
      print("No tenemos ese plato.")
      introducir_pedido()
      

def comprobar():
  global continuar
  while continuar != "N" and continuar != "S" and continuar != "n" and continuar != "s":
    continuar = input("¿Más para añadir?(S/N): ")
   

while not fin_platos:
  num_plato = str(num_plato)
  key = "Opcion" + num_plato
  num_plato = int(num_plato)
  introducir_menu()
  comprobar()
  if continuar == "S" or continuar == "s":
    num_plato += 1
    continuar = ""
    print("\n")
  elif continuar == "N" or continuar == "n":
    continuar = ""
    print("\n")
    fin_platos = True

mostrar_menu()

while not fin_pedido:
  num_pedido = str(num_pedido)
  key = "Pedido" + num_pedido
  num_pedido = int(num_pedido)
  introducir_pedido()
  comprobar()
  if continuar == "S" or continuar == "s":
    num_pedido += 1
    continuar = ""
    print("\n")
  elif continuar == "N" or continuar == "n":
    continuar = ""
    print("\n")
    fin_pedido = True

for key,value in pedido_realizado.items():

  if key == "Precio"+str(indice_pagar):
    precio_pedido = precio_pedido + int(value)
    indice_pagar += 1

print("La cuenta asciende a: " + str(precio_pedido) + "€.")
