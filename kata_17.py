frase = input("Introduce una frase: ")
caracter = input("Indica un caracter: ")
frase_salida = ""
for i in frase:
  if i == caracter:
    frase_salida = frase_salida + "-"
  else:
    frase_salida = frase_salida + i

print(frase_salida)
