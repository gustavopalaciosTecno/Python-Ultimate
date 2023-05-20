n1 = input("Ingresa primer número: ")
n2 = input("Ingresa segundo número: ")

suma = int(n1) + int(n2)
resta = int(n1) - int(n2)
multi = int(n1) * int(n2)
div = int(n1) / int(n2)

resultado = f"""
 para los números {n1} y {n2}
 el resultado de la suma es {suma}
 el resultado de la resta es {resta}
 el resultado de la multiplicación es {multi}
 el resultado de la división es {div}
"""
print(resultado)

