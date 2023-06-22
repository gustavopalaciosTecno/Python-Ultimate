class MiError(Exception):
    "esta clase es para representar mi error"

def division(n = int(input("ingresa un valor: "))):
    if n == 0:
        raise MiError("No se puede dividir entre cero")
    return 5 / n
    

       
try:
    print(division())
except MiError as ex:
    print("Ocurrió un error", ex)    