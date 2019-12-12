f = open('input.txt', 'r')
int_input = []
int_res = []
summary = 0
for line in f:
    int_input.append(int(line.strip('\n')))

for x in int_input:
    while x > 0:
        x = int((( x / 3) - 2))
        if x < 0:
            int_res.append(summary)
            summary = 0
            break
        summary += x
print(sum(int_res))
