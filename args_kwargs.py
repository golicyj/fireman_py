def percent_of_number (a, b, z):
    return (a * b * z ) * 0.1

#print(percent_of_number(10, 20, 5))


def percent_of_number_with_args (percent, *args):
    product = 1
    for number in args:
        product = product * number
    return product / 100 * percent

print(percent_of_number_with_args(10, 50))

def func_with_kwargs(**kwargs):
    print(kwargs)

func_with_kwargs(first = 1, second = 2, third = 3)

def heelo_with_kwargs(greting, **kwargs):
    if 'name' in kwargs:
        print('{}! so, {}?'.format(greting, kwargs['name']))
    else:
        print('{}! What is your name?'.format(greting))

heelo_with_kwargs('Joou', name='Jan')
