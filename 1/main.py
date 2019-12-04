f = open('input.txt', 'r')
int_input = []
for line in f:
    int_input.append(int(line.strip('\n')))

print (sum(([int(((x / 3) - 2)) for x in int_input])))
