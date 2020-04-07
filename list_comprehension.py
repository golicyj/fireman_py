gretting = 'hello'
gretting_list = [letter for letter in gretting]
#print(gretting_list)

#for letter in gretting:
 #   gretting_list.append(letter)

#print(gretting_list)


num_dict = {'fisrt': 1, 'second': 2, 'third': 3}
new_dict = {key: value ** 3 for key, value in num_dict.items()}
print(new_dict)