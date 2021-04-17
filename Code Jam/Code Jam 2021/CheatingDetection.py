
input = open('revinput.txt','r')
lines = input.readlines()

lines = [line.strip() for line in lines]

T = int(lines[0])
P = int(lines[1])

for test in range(T):
    player_percentage = []
    question_percentage = [0]*10000

    for line in range(2,len(lines)):
        questions_answered = lines[line].count('1')
        player_percentage.append(questions_answered/10000)
        for j in range(10000):
            question_percentage[j] = question_percentage[j] + int(lines[line][j])
    question_percentage = [percentage/100 for percentage in question_percentage]
    print(sorted(question_percentage))


    #max_correct = max(player_percentage)
    #player = player_percentage.index(max_correct) + 1
    #print("Case #"  + str(T) + ": " + str(player))
    #print(sorted(player_percentage))





"""
T = int(input())
P = int(input())

for test in range(T):
    player_percentage = []
    for i in range(100):
        answers = input()
        questions_answered = answers.count('1')
        player_percentage.append(questions_answered/10000)
    max_correct = max(player_percentage)
    player = player_percentage.index(max_correct) + 1
    print("Case #"  + str(T+1) + ": " + str(player))
"""
