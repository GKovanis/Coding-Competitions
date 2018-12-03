# in each line, count if there is a letter that appears exactly twice or three times
# in the end, multiply # of lines where at least one letter appeared twice with # of lines where at least one letter appeared three times
# multiple letters appearing two or three time still count only once
from collections import Counter

sum2 = 0
sum3 = 0
inputfile = [line.rstrip('\n') for line in open('p3.txt')]
for i in range(len(inputfile)): #iterate through lines
    counter = Counter(inputfile[i])
    if 2 in counter.values():
        sum2 = sum2 + 1
    if 3 in counter.values():
        sum3 = sum3 + 1
print(sum2*sum3)
