def impar(inicio,fin):
    num = inicio
    while num < fin:
        resto = num % 2
        if resto != 0:
            print(num)
        num += 1

impar(4,10)