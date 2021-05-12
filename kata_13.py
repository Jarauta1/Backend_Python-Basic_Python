lista = [6,5,2,1,7]
pares = []
impares= []

def ordenar(lista):
  lista.sort()
  longitud = len(lista)
  indice = 0
  while indice < longitud:
    probar = lista[indice] % 2
    valor = lista[indice]
    if probar != 0:
      impares.append(valor)
    else:
      pares.append(valor)
    indice += 1

ordenar(lista)
print(pares)
print(impares)
