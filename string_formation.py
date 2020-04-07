age = 23
print('Jake is ' + str(age) + ' years old')
print('Jake is ' + str(24) + ' years old')

name = 'Jack'
age = 23
name_and_age = 'My name is Jak {0}. I\'m {1} years old.'.format(name, age)
print(name_and_age)
name_and_age = 'My name is Jak {0}. I\'m {1} years old.'.format('Jack', 23)
print(name_and_age)

float_results = 1000 / 7
print(float_results)
print('The result of division is {0:4.3f}'.format(float_results))
