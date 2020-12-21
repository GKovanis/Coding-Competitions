def get_opcode_params (code):
    opcode = code % 100
    prm1 = code // 100 % 10
    prm2 = code // 1000 % 10
    prm3 = code // 10000 % 10
    return (opcode,prm1,prm2,prm3)

codes = [line.rstrip('\n').split(',') for line in open('p9.txt')][0]
codes = [int(x) for x in codes]
for i in range(len(codes),10000):
    codes.append(0)
input = 1
output = 0
pointer = 0
rel_base = 0

while True:
    # Halt in 99
    if (codes[pointer] == 99):
        break
    # Split opcode and parameter modes
    opcode,prm1,prm2,prm3 = get_opcode_params(codes[pointer])
    # Do appropriate instruction based on opcode
    # opcode 1 -> Addition (3 Parameters)
    if (opcode == 1):
        value1 = codes[codes[pointer+1]]  if prm1 == 0 else (codes[pointer+1] if prm1 == 1 else codes[codes[pointer+1]+rel_base])
        value2 = codes[codes[pointer+2]]  if prm2 == 0 else (codes[pointer+2] if prm2 == 1 else codes[codes[pointer+2]+rel_base])
        codes[codes[pointer+3]] = value1 + value2
        pointer += 4
    # opcode 2 -> Multiplication (3 parameters)
    elif (opcode == 2):
        value1 = codes[codes[pointer+1]]  if prm1 == 0 else (codes[pointer+1] if prm1 == 1 else codes[codes[pointer+1]+rel_base])
        value2 = codes[codes[pointer+2]]  if prm2 == 0 else (codes[pointer+2] if prm2 == 1 else codes[codes[pointer+2]+rel_base])
        codes[codes[pointer+3]] = value1 * value2
        pointer += 4
    # opcode 3 -> Save input in parameter position (1 parameter)
    elif (opcode == 3):
        codes[codes[pointer + 1]] = input
        pointer += 2
    # opcode 4 -> Output value of position (1 parameter)
    elif (opcode == 4):
        output = codes[codes[pointer+1]] if prm1 == 0 else (codes[pointer+1] if prm1 == 1 else codes[codes[pointer+1]+rel_base])
        pointer += 2
    # opcode 5 -> jump-if-true (2 parameters)
    elif (opcode == 5):
        value1 = codes[codes[pointer+1]]  if prm1 == 0 else (codes[pointer+1] if prm1 == 1 else codes[codes[pointer+1]+rel_base])
        if value1 != 0:
            pointer = codes[codes[pointer+2]]  if prm2 == 0 else (codes[pointer+2] if prm2 == 1 else codes[codes[pointer+2]+rel_base])
        else:
            pointer += 3
    # opcode 6 -> jump-if-false (2 parameters)
    elif (opcode == 6):
        value1 = codes[codes[pointer+1]]  if prm1 == 0 else (codes[pointer+1] if prm1 == 1 else codes[codes[pointer+1]+rel_base])
        if value1 == 0:
            pointer = codes[codes[pointer+2]]  if prm2 == 0 else (codes[pointer+2] if prm2 == 1 else codes[codes[pointer+2]+rel_base])
        else:
            pointer += 3
    # opcode 7 -> less than (3 parameters)
    elif (opcode == 7):
        value1 = codes[codes[pointer+1]]  if prm1 == 0 else (codes[pointer+1] if prm1 == 1 else codes[codes[pointer+1]+rel_base])
        value2 = codes[codes[pointer+2]]  if prm2 == 0 else (codes[pointer+2] if prm2 == 1 else codes[codes[pointer+2]+rel_base])
        codes[codes[pointer+3]] = 1 if value1 < value2 else 0
        pointer += 4
    # opcode 8 -> equal (3 parameters)
    elif (opcode == 8):
        value1 = codes[codes[pointer+1]]  if prm1 == 0 else (codes[pointer+1] if prm1 == 1 else codes[codes[pointer+1]+rel_base])
        value2 = codes[codes[pointer+2]]  if prm2 == 0 else (codes[pointer+2] if prm2 == 1 else codes[codes[pointer+2]+rel_base])
        codes[codes[pointer+3]] = 1 if value1 == value2 else 0
        pointer += 4
    # opcode 9 -> adjust relative base (1 parameter)
    elif (opcode == 9):
        rel_base = rel_base + (codes[codes[pointer+1]] if prm1 == 0 else (codes[pointer+1] if prm1 == 1 else codes[codes[pointer+1]+rel_base]))
        pointer += 2
    else:
        print ('Error')


print(output)
