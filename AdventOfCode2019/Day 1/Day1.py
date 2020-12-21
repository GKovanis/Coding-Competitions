sum = 0
inputfile = [line.rstrip('\n') for line in open('p1.txt')]
for line in inputfile:
    fuel = line
    while True:
        fuel = (int(fuel) // 3) - 2
        if fuel <= 0:
            break
        sum = sum + fuel
print (sum)
