with open('test_bin', 'bw') as compfile:
    for x in range(30):
        compfile.write(bytes([x]))

with open('test_bin', 'br') as compfile:
    for x in compfile:
        print(x)
