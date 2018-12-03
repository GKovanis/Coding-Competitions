# Find sum of all numbers in file
sum = 0
inputfile = [line.rstrip('\n') for line in open('p1.txt')]
for i in range(len(inputfile)):
    sum = sum + int(inputfile[i])
print(sum)
