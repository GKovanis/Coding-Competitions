#Day4 Puzzle2
sleepmin = dict()
for i in range(59):
    sleepmin[i]=dict()
inputfile = [line.rstrip('\n') for line in open('p8.txt')]
inputfile = sorted(inputfile)
#Run again to find which minute he was sleeping the most
for line in range(len(inputfile)):
    temp = inputfile[line].split()
    minute = int(temp[1].split(":")[1][:-1]) #remove last character from string
    action = temp[2]
    if action == "Guard":
        id = int(temp[3][1:])
    elif action == "wakes":
        for i in range(asleepmin,minute):
            if id not in sleepmin[i]:
                sleepmin[i][id] = 1 # he was sleeping at that minute
            else:
                sleepmin[i][id] = sleepmin[i][id] + 1 # he was sleeping at that minute
    else:
        asleepmin = minute
maxminute = 0
maxvalue = 0
for i in range(59):
    maxx = max(sleepmin[i],key=sleepmin[i].get)
    if (sleepmin[i][maxx]>maxvalue):
        maxvalue = sleepmin[i][maxx]
        maxminute = i
#Print result
print(maxminute*[key for (key,value) in sleepmin[maxminute].items() if value == maxvalue][0])
