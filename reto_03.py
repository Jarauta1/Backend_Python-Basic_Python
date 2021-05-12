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
fin_platos = False

plato = ""
precio = ""
continuar = ""

def introducir_menu():
  global plato
  plato = input("Plato a introducir al menú: ")
  global precio
  precio = input("Precio del plato: ")

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
    menu[key] = plato
    precios[key] = precios
    num_plato += 1
    continuar = ""
    print(continuar)
  elif continuar == "N" or continuar == "n":
    continuar = ""
    fin_platos = True

print(menu)
print(precios)
