def division(n = int(input("ingresa un valor: "))):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return 5 / n
    

       
try:
    print(division())
except ZeroDivisionError as ex:
    print("Ocurrió un error", ex)    