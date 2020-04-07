#immutable
first_name = 'Jane'
print(first_name[1])
#first_name[1] = 'n'
#print(first_name)

first_two_letters = first_name[:2]
print(first_two_letters)
last_letter = first_name[-1:]
print(last_letter)

#concatenable
new_first_name = first_two_letters + 'k' + last_letter
print(new_first_name)

#miltiplication
yummy = 'Yum'
print(yummy * 10)

print(yummy.upper())
print(yummy.lower())

long_string = 'This is the long string'
print(long_string.split('s'))