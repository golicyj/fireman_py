color_base = ['red', 'green', 'blue']

with open('colors.txt', 'a') as colors:
    for color in color_base:
        print(color, file=colors)
