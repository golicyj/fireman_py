def sum_of_two_umbers(a):
    return(a+a)



number_list = [1,2,3,4,5,6,7,8,9]
result = map(sum_of_two_umbers, number_list)
print(result)

for x in result:
    print(x)

for x in map(sum_of_two_umbers, number_list):
    print(x)

def symbol_checker(string):
    if 'a' in string:
        print('A is in string')
        return True
    else:
        print('Not found A in the string')
        return False

string_list = ['hi', 'lol', 'max', 'low']

print(list(map(symbol_checker, string_list)))



print(list(filter(lambda num: num % 2 == 1, number_list)))

for x in filter(lambda num: num % 2 == 1, number_list):
    print(x)

#lambda



number_list_for_cube = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda num: num ** 3,number_list_for_cube)))