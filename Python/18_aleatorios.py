"""
Generando numeros aleatorios
"""


import random

for n in range(10):
    print('entero aleatorio:', random.randint(0, 10000))

#numeros aleatorios entre 0 y 1

for n in range(4):
    print(random.random())


L = ['oscar', 'jovanny', 'jaime', 'pepe', 'ciudadano', 'otro pepe', 'caca']

#Elemto aleatorio de una lista
for n in range(8):
print(random.choice(L))

#Elemntos aleatorios de una lista (pueden llegar repeticiones)
r = random.choices(L, K=2)# K es el numero de elemntos que queremos
print(r)

#Cambiar orden de elementos de una lista, de forma aleatoria

random.shuffle(L)
print(L)
random.shuffle(L)
print(L)

#A partir de una lista crear otra con K elementos que no esten repetidos

print(random.sample(L, K=2))
print(random.sample(L, K=2))
print(random.sample(L, K=2))
print(random.sample(L, K=2))
print(random.sample(L, K=2))
print(random.sample(L, K=2))
print(random.sample(L, K=2))
print(random.sample(L, K=2))
print(random.sample(L, K=2))
print(random.sample(L, K=2))



