def impar(tope):
    num = 1
    while num < tope:
        resto = num % 2
        if resto != 0:
            print(num)
        num += 1

impar(10)