inputfile = [line.rstrip('\n') for line in open('p4.txt')]
for i in range(len(inputfile)): #index for 1st line
    for j in range(i,len(inputfile)): #index for 2nd line
        line1 = inputfile[i]
        line2 = inputfile[j]
        diff = 0
        #count different letters between 2 lines
        for char in range(len(line1)):
            if line1[char] != line2[char]:
                diff += 1
        if diff == 1:
            print(line1,line2)
            exit()
