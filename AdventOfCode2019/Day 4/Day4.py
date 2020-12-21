pws = [line.rstrip('\n') for line in open('p4.txt')]
pws = pws[0].split('-')
sum = 0

for password in range(int(pws[0]),int(pws[1])):
    password = str(password)
    #Check order, password should be similar to ordered digits
    if password != "".join(sorted(password)):
        continue
    # Check similar digits
    flag = False
    for i in range(len(password)-1):
        #Part 1 -> if password[i] == password[i+1]:
        if password[i] == password[i+1]:
            #if (password[i] != password[min(i+2,5)] if i<6 else True) and (password[i] != password[max(0,i-1)] if i>0 else True):
            if (password[i] != password[i+2] if i < 4 else True) and ((password[i] != password[i-1] if i > 0 else True)):
                sum += 1
                break
print(sum)
