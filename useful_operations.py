from random import  shuffle
for x in range(0, 150, 5):
    print(x)

letter_index = 0
my_string= 'qwertyuio'

for letter in my_string:
    print(letter + ' is at index' + str(letter_index))
    letter_index = letter_index + 1


