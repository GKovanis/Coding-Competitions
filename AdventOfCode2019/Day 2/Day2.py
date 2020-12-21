opcodes = [line.rstrip('\n').split(',') for line in open('p2.txt')][0]
opcodes = [int(x) for x in opcodes]

"""
Part 1
pointer = 0
opcodes[1] = 12
opcodes[2] = 2
while (opcodes[pointer] != 99):
    if (opcodes[pointer] == 1):
        opcodes[opcodes[pointer+3]] = opcodes[opcodes[pointer+1]] + opcodes[opcodes[pointer+2]]
    else:
        opcodes[opcodes[pointer+3]] = opcodes[opcodes[pointer+1]] * opcodes[opcodes[pointer+2]]
    pointer += 4
print(opcodes[0])
"""

# Part 2
flag = False
input = opcodes[:]
for noun in range(100):
    for verb in range(100):
        opcodes = input[:]
        opcodes[1] = noun
        opcodes[2] = verb
        pointer = 0
        while (opcodes[pointer] != 99):
            if (opcodes[pointer] == 1):
                opcodes[opcodes[pointer+3]] = opcodes[opcodes[pointer+1]] + opcodes[opcodes[pointer+2]]
            else:
                opcodes[opcodes[pointer+3]] = opcodes[opcodes[pointer+1]] * opcodes[opcodes[pointer+2]]
            pointer += 4
        if opcodes[0] == 19690720:
            flag = True
            break
    if flag:
        break

print (100*noun+verb)
