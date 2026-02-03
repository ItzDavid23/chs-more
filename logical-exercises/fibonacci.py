""" #def fibonnaci(rango):
    for i in rango:
        if i == 0:
            return(i)
        elif i == 1:
            return(i)
        else:
            return(i + (i - 1))


numero = int(input("Ingrese un numero entero: "))
print(fibonnaci(numero)) """


def fibonnaci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonnaci(num - 2) + fibonnaci(num - 1) # -> 0, 1,  

numero = int(input("Ingrese un número: "))

for i in range(numero + 1):
    print(fibonnaci(i))


""" for i in range(0, 51):
        if i == 0:
            print(i)
        elif i == 1:
            print(i)
        else:
             c = a + b
             print(c)
             a, b = b, c

 """