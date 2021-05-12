num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))

def menorque(a,b):
  if a < b:
    return "El menor es: " + str(a)
  elif b < a:
    return "El menor es: " + str(b)
  else:
    return "Son iguales"

print(menorque(num1,num2))
