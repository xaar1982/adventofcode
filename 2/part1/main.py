f = open('input.txt', 'r')
int_input = []
opcode_step = 4
save_index = 0
start = 0

for i in f:
    int_input = i.split(',')

int_input = [int(x.replace('\n', '')) for x in int_input]

while start <= len(int_input)-1:
        if int_input[start] == 1:
            save_index = start
            first_int = int_input[start+1]
            second_int = int_input[start+2]
            int_input[int_input[start+3]] = int_input[first_int] + int_input[second_int]
            start = save_index + opcode_step
        elif int_input[start] == 2:
            save_index = start
            first_int = int_input[start+1]
            second_int = int_input[start+2]
            int_input[int_input[start+3]] = int_input[first_int] * int_input[second_int]
            start = save_index + opcode_step
        elif int_input[start] == 99:
            break
        else:
            print('Something is wrong')

print(int_input)
