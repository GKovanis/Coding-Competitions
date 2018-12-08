#Day4 Puzzle1
guards = dict() #key = ID, value = minutes slept
inputfile = [line.rstrip('\n') for line in open('p7.txt')]
inputfile = sorted(inputfile)
#Run once to find who slept the most
for line in range(len(inputfile)):
    temp = inputfile[line].split()
    minute = int(temp[1].split(":")[1][:-1]) #remove last character from string
    action = temp[2]
    if action == "Guard":
        asleep = False
        id = int(temp[3][1:])
        if id in guards:
            continue
        else:
            guards[id]=0
    elif action == "wakes":
        guards[id] = guards[id] + (minute - asleepmin) #the time he was sleeping
    else:
        asleepmin = minute
#Find guard who slept the most
sleepyguard = max(guards, key=guards.get)
#Initializations to find minute he was sleeping the most
sleepmin = dict()
correctGuard = False
for i in range(59):
    sleepmin[i]=0
inputfile = [line.rstrip('\n') for line in open('p7.txt')]
inputfile = sorted(inputfile)
#Run again to find which minute he was sleeping the most
for line in range(len(inputfile)):
    temp = inputfile[line].split()
    minute = int(temp[1].split(":")[1][:-1]) #remove last character from string
    action = temp[2]
    if action == "Guard":
        id = int(temp[3][1:])
        if (id == sleepyguard):
            correctGuard = True
        else:
            correctGuard = False
    elif action == "wakes":
        if correctGuard:
            for i in range(asleepmin,minute):
                sleepmin[i] = sleepmin[i] + 1 # he was sleeping at that minute
    else:
        if correctGuard:
            asleepmin = minute
MostSleep = max (sleepmin,key=sleepmin.get)
print(sleepyguard*MostSleep)
