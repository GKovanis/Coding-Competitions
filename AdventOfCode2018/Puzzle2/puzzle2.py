# Find the first sum number that appears twice
# If file finished with no number appearing twice, reiterate file
sum = 0
appearedonce = []
flag = True
while (flag):
    inputfile = [line.rstrip('\n') for line in open('p2.txt')]
    for i in range(len(inputfile)):
        appearedonce.append(sum)
        sum = sum + int(inputfile[i])
        if sum in appearedonce:
            flag = False
            answer = sum
            break
print(answer)
