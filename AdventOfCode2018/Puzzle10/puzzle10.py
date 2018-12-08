#Day5 Puzzle2
#run once to reduce file size
inputfile = [line.rstrip('\n') for line in open('p10.txt')][0]
flag = True
while (flag):
    flag=False
    for i in range(len(inputfile)-1):
        if (abs(ord(inputfile[i])-ord(inputfile[i+1]))==32): #ASCII difference between uppercase and lowercase is 32
            inputfile = inputfile[:i]+inputfile[i+2:]
            flag = True
            break
####
temp = inputfile
for j in range(26): #for each letter of the alphabet
    inputfile = temp
    flag = True
    while (flag):
        flag=False
        for i in range(len(inputfile)-1):
            if ((ord(inputfile[i])== 65+j) or (ord(inputfile[i]) == 97+j)):
                flag = True
                letter = inputfile[i]
                inputfile = inputfile[:i]+inputfile[i+1:]
                break
    print(letter)
    flag = True
    while (flag):
        flag=False
        for i in range(len(inputfile)-1):
            if ((abs(ord(inputfile[i])-ord(inputfile[i+1]))==32)): #ASCII difference between uppercase and lowercase is 32
                flag = True
                letter = inputfile[i]
                inputfile = inputfile[:i]+inputfile[i+2:]
                break
    print(len(inputfile))
