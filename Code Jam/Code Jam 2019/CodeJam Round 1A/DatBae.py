#!/usr/bin/env python3
import sys

#Read from judge
def read_judge_input():
    inputt = input()
    if inputt == '-1':
        sys.exit(0)
    return inputt

#Create questions to send
def questions(line,n):
    question = []
    line = str(line)
    if line == '0':
        for binary_num in range(n):
            question.append(binary_num%2)
    elif line == '1':
        for binary_num in range(1,n+1):
            question.append(binary_num%2)
    elif line == '2':
        for binary_num in range(n):
            if (binary_num%4>1):
                temp = 0
            else:
                temp = 1
            question.append(temp)
    elif line == '3':
        for binary_num in range(n):
            if (binary_num%4>1):
                temp = 1
            else:
                temp = 0
            question.append(temp)
    elif line =='4':
        for binary_num in range(n):
            if (binary_num%3==0):
                temp = 1
            else:
                temp = 0
            question.append(temp)
    elif line =='5':
        for binary_num in range(n):
            if (binary_num%3==0):
                temp = 0
            else:
                temp = 1
            question.append(temp)
    elif line =='6':
        for binary_num in range(n):
            if (binary_num%4==0):
                temp = 0
            else:
                temp = 1
            question.append(temp)
    elif line =='7':
        for binary_num in range(n):
            if (binary_num%4==0):
                temp = 1
            else:
                temp = 0
            question.append(temp)
    elif line =='8':
        for binary_num in range(n):
            if (binary_num%5==0) or (binary_num%4>1):
                temp = 1
            else:
                temp = 0
            question.append(temp)
    else:
        for binary_num in range(n):
            if (binary_num%5==0) or (binary_num%4>1):
                temp = 0
            else:
                temp = 1
            question.append(temp)
    question = [str(x) for x in question]
    question = ''.join(question)
    return question


def main():
    #Read input
    debug = open('debug','w')
    t = int(input())
    for i in range(1, t + 1):
        n,b,f = [int(s) for s in input().split(" ")]
        #Exchange with judge
        sending = []
        answer = []
        for line in range(9):
            sending.append(questions(line,n))
            sys.stdout.write(sending[line]+ '\n')
            sys.stdout.flush()
            answer.append(read_judge_input())
        #Compare columns to find broken workers
        broken = []
        col_out = 0
        col_in = 0
        while(True):
            for j in range(9):
                flag = True
                if (answer[j][col_out] == sending[j][col_in]):
                    continue
                else:
                    flag = False
                    break
            if not flag: #column is not the same
                broken.append(col_in)
            else:
                col_out = col_out + 1
            col_in = col_in + 1
            if len(broken) == b:
                break
            if col_out == n-b:
                for k in range(col_in,n):
                    broken.append(k)
                break
        #Send Solution
        broken = [str(x) for x in broken]
        solution = ' '.join(broken)
        #debug.write(str(solution)+ '\n')
        sys.stdout.write(solution+ '\n')
        sys.stdout.flush()
        verdict = input()

if __name__ == '__main__':
    main()
