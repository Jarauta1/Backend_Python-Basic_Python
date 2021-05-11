peso = input("¿Cuánto pesas?(en kg): ")
altura = input("¿Cuánto mides?(en metros): ")

imc = round((float(peso)/(float(altura)**2)),2)

print("Tu indice de masa corporal es: " + str(imc))