money = float(input("¿Qué cantidad desea invertir?: "))
percent = float(input("¿Qué interés porcentual anual quiere?: "))
years = float(input("¿Cuántos años desea invertir?: "))

benefits = round(money * (percent/100+1) ** years,2)
print("Usted invirtió " + str(round(money,2)) + "€.")
print("Ahora tiene " + str(round(benefits,2)) + "€.")