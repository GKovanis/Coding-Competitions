#Day5 Puzzle1
inputfile = [line.rstrip('\n') for line in open('p9.txt')][0]
flag = True
while (flag):
    flag=False
    for i in range(len(inputfile)-1):
        if (abs(ord(inputfile[i])-ord(inputfile[i+1]))==32): #ASCII difference between uppercase and lowercase is 32
            inputfile = inputfile[:i]+inputfile[i+2:]
            flag = True
            break
print(len(inputfile))
