#Day 7 Part 1
from string import ascii_uppercase
Needs = dict()
for char in ascii_uppercase:
    Needs[char] = []
inputfile = [line.rstrip('\n') for line in open('p13.txt')]
for i in range(len(inputfile)):
    #parsing
    temp = inputfile[i].split()
    FinStep = temp[1]
    BegStep = temp[7]
    #Create a list with each step needed before the one in the key
    Needs[BegStep].append(FinStep)
#Run until all steps in order
order = []
while(Needs):
    #Go through all the steps to see the ones that do not have a prerequisite
    CanDelete = []
    for key,value in Needs.items():
        if not Needs[key]: #List of prerequisites is empty
            CanDelete.append(key)
    CanDelete.sort() #Delete in Alphabetical Order
    #Remove step to be deleted from prerequisite and then delete it
    for key,value in Needs.items():
        if CanDelete[0] in Needs[key]:
            Needs[key].remove(CanDelete[0])
    order.append(CanDelete[0])
    del Needs[CanDelete[0]]
for i in range(len(order)):
    print(order[i],end='')
print('\n')
