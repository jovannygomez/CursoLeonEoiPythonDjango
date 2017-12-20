"""
Ejemplos para trabajar con LISTAas
"""

LISTA = [1, 2, 3, 4, 5, "seis"]
print(LISTA)
print(LISTA[0])
print(LISTA[4])
print(LISTA[2:5])
print(LISTA[3:])
print(LISTA[:2])

size = len(LISTA)
print('tamaño de la LISTAa', size)

del LISTA[2]
print(LISTA)

LISTA[2] = 'tres'
print(LISTA)

#Concatenar dos listas

LISTA += ['siete', 8, True, False]
print(LISTA)

#Añadir elemento a la lista

LISTA.append('elemento nuevo')
print(LISTA)

LISTA.remove('seis')
print(LISTA)

LISTA.reverse()
print(LISTA)

LISTA.insert(1, 'PC')
print(LISTA)