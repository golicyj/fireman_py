lorem_ipsum_open = open('lorem.txt', 'r')
for line in lorem_ipsum_open:
    if 'tor' in line:
        pass
        #print(line)

lorem_ipsum_open.close()

with open('lorem.txt', 'r') as loremtext:
    line = loremtext.readline()
    while line:
        pass
        #print(line, end='')
        line = loremtext.readline()

with open('lorem.txt', 'r') as loremtext:
    lines = loremtext.readlines()
#print(lines)


for line  in lines[::-1]:
    print(line)