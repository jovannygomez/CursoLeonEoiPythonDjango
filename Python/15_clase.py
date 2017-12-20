"""
trabajando con clases
"""

class thing:
    pass 



#contructor sin argumentos parametros

class Fruit:
    def __init__(self):
        print('objeto fruta')

fruit = Fruit()

#argumentos del constructor

class CustomFruit:

"""esta clase no vale para mucho pero me gusta escribir"""

    COUNTER=0

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.juices = 0
    	CustomFruit.COUNTER += 1

    def __str__(self):
        return 'Soy fruta, me llamo {} y mi color es {}.\hHay{} frutas en total'\
            .format(self.name, self.color, CustomFruit.COUNTER)

    def make_juice(self, count):
        for n in range(count):
            print('Haciendo zumo de', self.name)
            self.juices += 1

custom =  CustomFruit('pera', 'verde')
print(custom)
custom.make_juice(2)

c2 = CustomFruit('Limon', 'Amarillo')
print(c2)
c2.make_juice(4)
print('Zumos hechos', c2.juices)





