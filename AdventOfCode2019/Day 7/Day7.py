from itertools import permutations

def get_opcode_params (code):
    opcode = code % 100
    prm1 = code // 100 % 10
    prm2 = code // 1000 % 10
    prm3 = code // 10000 % 10
    return (opcode,prm1,prm2,prm3)

codes = [line.rstrip('\n').split(',') for line in open('p7.txt')][0]
codes = [int(x) for x in codes]

# Get all possible phase combinations
phases = '01234'
poss_phases = [''.join(p) for p in permutations(phases)]

loop_phases = '56789'
poss_loop_phases = [''.join(p) for p in permutations(loop_phases)]

max_output = 0
# Run an instance for each possible phase order
for phase_order in poss_phases:
    phase_output = 0
    pointer = 0
    # Run 5 times for each amplifier
    for k in range(len(phase_order)):
        phase_input = int(phase_order[k])
        input_flag = True
        output_input = phase_output
        pointer = 0
        while True:
            # Halt in 99
            if (codes[pointer] == 99):
                break
            # Split opcode and parameter modes
            opcode,prm1,prm2,prm3 = get_opcode_params(codes[pointer])

            # Do appropriate instruction based on opcode
            # opcode 1 -> Addition (3 Parameters)
            if (opcode == 1):
                value1 = codes[codes[pointer+1]]  if prm1 == 0 else codes[pointer+1]
                value2 = codes[codes[pointer+2]]  if prm2 == 0 else codes[pointer+2]
                codes[codes[pointer+3]] = value1 + value2
                pointer += 4
            # opcode 2 -> Multiplication (3 parameters)
            elif (opcode == 2):
                value1 = codes[codes[pointer+1]]  if prm1 == 0 else codes[pointer+1]
                value2 = codes[codes[pointer+2]]  if prm2 == 0 else codes[pointer+2]
                codes[codes[pointer+3]] = value1 * value2
                pointer += 4
            # opcode 3 -> Save input in parameter position (1 parameter)
            elif (opcode == 3):
                if input_flag:
                    codes[codes[pointer + 1]] = phase_input
                    input_flag = False
                else:
                    codes[codes[pointer + 1]] = output_input
                pointer += 2
            # opcode 4 -> Output value of position (1 parameter)
            elif (opcode == 4):
                phase_output = codes[codes[pointer+1]] if prm1 == 0 else codes[pointer+1]
                pointer += 2
            # opcode 5 -> jump-if-true (2 parameters)
            elif (opcode == 5):
                value1 = codes[codes[pointer+1]]  if prm1 == 0 else codes[pointer+1]
                if value1 != 0:
                    pointer = codes[codes[pointer+2]]  if prm2 == 0 else codes[pointer+2]
                else:
                    pointer += 3
            # opcode 6 -> jump-if-false (2 parameters)
            elif (opcode == 6):
                value1 = codes[codes[pointer+1]]  if prm1 == 0 else codes[pointer+1]
                if value1 == 0:
                    pointer = codes[codes[pointer+2]]  if prm2 == 0 else codes[pointer+2]
                else:
                    pointer += 3
            # opcode 7 -> less than (3 parameters)
            elif (opcode == 7):
                value1 = codes[codes[pointer+1]]  if prm1 == 0 else codes[pointer+1]
                value2 = codes[codes[pointer+2]]  if prm2 == 0 else codes[pointer+2]
                codes[codes[pointer+3]] = 1 if value1 < value2 else 0
                pointer += 4
            # opcode 8 -> equal (3 parameters)
            elif (opcode == 8):
                value1 = codes[codes[pointer+1]]  if prm1 == 0 else codes[pointer+1]
                value2 = codes[codes[pointer+2]]  if prm2 == 0 else codes[pointer+2]
                codes[codes[pointer+3]] = 1 if value1 == value2 else 0
                pointer += 4
            else:
                print ('Error')
        # Does this phase order produce maximum possible output?
        if k == 4 and phase_output >= max_output:
            max_output = phase_output
            max_phase = phase_order

print(max_output)
