"""
Ejemplo para trabajar con cadenas de texto
"""

TEXTO = 'Hola mundo'
print(TEXTO[0])
print(TEXTO[1])
print(TEXTO[2])
print(TEXTO[3])
print(TEXTO[4])
print(TEXTO[5])
print(TEXTO[6])
print(TEXTO[7])
print(TEXTO[8])
print(TEXTO[9])

print(TEXTO[5:8])
print(TEXTO[6:])
print(TEXTO[:3])

#Concatenacion

print(TEXTO + ' ' + TEXTO)

print(TEXTO.upper())
print(TEXTO.capitalize())
print(len(TEXTO))
print(TEXTO.split())
print(TEXTO.split('m'))