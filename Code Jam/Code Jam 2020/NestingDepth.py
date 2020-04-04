T = int(input())

for test in range(T):
    S = input()
    output = [int(S[0])*'('] #Put initial opening parenthesis based on first digit
    for pos in range(len(S)-1):
        output.append(S[pos]) #Put the digit in the string
        if S[pos+1] > S[pos]: # 12
            output.append((int(S[pos+1])-int(S[pos]))*'(')
        elif S[pos+1] < S[pos]: # 21
            output.append((int(S[pos])-int(S[pos+1]))*')')
        else: # 11, do nothing
            pass
    # Last digit left
    output.append(S[-1]) # Append last digit
    output.append(int(S[-1])*')') #Append last closing parenthesis based on last digit
    solution = ''.join(output)

    #print result
    print("Case #" + str(test+1) + ": " + solution)
