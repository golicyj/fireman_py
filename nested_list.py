nested_list = [[1,2,3], [3, 2, 3, 3], [0, 1, 1, 0, 1, 1, 0]]
#print(nested_list)
#print(len(nested_list))
#print(len(nested_list[1]))
#print(len(nested_list[-1]))
#print(nested_list[1][1])

for x in nested_list:
    print(x)

for x in nested_list:
    for number in x:
        print(number)