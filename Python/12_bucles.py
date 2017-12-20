def print_everything(*args):
    for n in args:
        print(n)

print_everything('manzana', 'platano', 'pera')

def print_all_with_position(*args):
    for count, thing in enumerate(args):
        print('{}.{}'.format(count, thing))

print_all_with_position('manzana', 'platano', 'pera')

def show_keyword_arguments(**kwards):
    for name, value in kwars.items():
        print('{}:{}'.formate(name, value))

show_keyword_arguments(uno=1, dos=2, )
























counter = 0
while True:
    counter += 1 
    print(counter)
    if counter > 300:
        break

counter = 0
while True:
    counter += 1 
    print(counter)
    if counter > 800:
        break



