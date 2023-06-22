try:
    
    numero = int(input("Introducí un valor numérico: "))

except NameError as ex:
    print(f"ocurrrió un error")
except ValueError as ex:
    print("Ocurrió un error nuevamente")    