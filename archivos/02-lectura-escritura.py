from pathlib import Path

archivo = Path("archivos/archivo-prueba.txt")
texto = archivo.read_text("utf-8").split("\n")
texto.insert(0, "programación orientada a objetos")
archivo.write_text("\n".join(texto),"utf-8")
print(texto)
