#Day 7 Part 2
#Initializations
from string import ascii_uppercase
Needs = dict()
for char in ascii_uppercase:
    Needs[char] = []
WorkAvail = 5
steps = 0
#Read File
inputfile = [line.rstrip('\n') for line in open('p14.txt')]
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
    print(CanDelete)
    #Remove step to be deleted from prerequisite and then delete it
    for i in range(len(CanDelete)):
        for key,value in Needs.items():
            if CanDelete[i] in Needs[key]:
                Needs[key].remove(CanDelete[i])
        order.append(CanDelete[i])
        del Needs[CanDelete[i]]
for i in range(len(order)):
    print(order[i],end='')
print('\n')
#ran by hand to find answer
