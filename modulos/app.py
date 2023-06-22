#from usuarios.acciones import guardar // ESTA ES UNA FORMA DE IMPORTAR LOS PAQUETES
#import usuarios.acciones # ESTA ES OTRA FORMA DE IMPORTAR LOS PAQUETES
#from usuarios import acciones // Y ESTA ES OTRA FORMA DE IMPORTAR LOS PAQUETES

from usuarios.acciones.utilidades import guardar

# primero coloco from (nombre del archivo) luego import (nombre de la función)
# es recomendale usar un import nombrado y no con el asterisco *
# los móidulos apuntan a archivos y los módulos a carpetas
guardar()