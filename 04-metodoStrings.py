animal = "  jirafa  "
print(animal)
print(animal.split()) # agrega la variable entre cadenas
print(animal.capitalize()) # le agrega la letra mayúscula al inicio
print(animal.title()) #Convierte la primer letra de cada palabra en mayúscula
print(animal.upper()) # convierte en mayúscula
print(animal.lower()) # convierte en minúscula
print(animal.strip().capitalize()) #quita espacios y convierte la primera en mayúscula
print(animal.lstrip()) #quita espacio hacia la izquierda
print(animal.rstrip()) # quita espacio hacia la derecha
print(animal.find("ji")) # busca un valor y te devuelve el índice de la cadena de caracteres
print(animal.replace("ji", "pi")) # reemplaza un valor por otro
print("ji" in animal) # me devuelve True o False si el valor existe en la cadena
print("ji" not in animal) # hace lo contrario al código anterior
