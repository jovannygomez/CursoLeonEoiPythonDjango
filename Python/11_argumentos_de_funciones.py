"""
Diferentes maneras de usar argumentos
"""

#Argumentos posicionales obligatorios

def hi(name):
    print('Hi', name)



#hi() #esto falla porque 'name' es obligatorio

def f(n='uno'):
    print(n)

f()

def f2(one = 1 , two = 2, three=3 ):
    print(one, two, three)    

#usar argumentos por orden

f2(45, 10, 22)

#usar argumentos como keywords


def dime_cosas(*args):
    print(args)

dime_cosas(20, 30, 90, True,False, 'hola')

def f3(name, *args):
    print('hola', name)
    print(args)

f3('pedro', 20, 30, 90, True, False,'hola')


def f4(**kwars): 
    print(kwars)

f4(C = 'uno', B = 'tres', f = True, A = 'manolo')

O = {'C': 'uno', 'B': 'tres', 'F': True, 'A': 'manolo'}
f4(**O)
