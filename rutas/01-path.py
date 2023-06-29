from pathlib import Path

# Path(r"C:\Program Files\JetBrains")
# # ruta para Linux --> Path("/usr/bin")
# Path()
# Path.home()
# Path("one/__init__.py")

path = Path("mi-carpeta/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
    
)

p = path.with_name("garzas felices")
print(p)
p = path.with_suffix(".bat")
print(p)
p = path.with_stem("Happy")
print(p)
