"""
Ejemplo de uso de extensiones regulares
"""

import re

phone = '657980418 # esto es numero de telefono'

#borrar comentarios
number = re.sub(r'#.*$', '', phone)
print('telefono', number)

