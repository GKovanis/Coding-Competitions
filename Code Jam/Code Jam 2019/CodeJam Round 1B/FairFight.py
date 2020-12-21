import numpy as np
#Read input
t = int(input()) #number of test cases
for i in range(1, t + 1):
    n,k = [int(x) for x in input().split(" ")]
    #Read each one's skills
    c_skills = np.array([int(x) for x in input().split(" ")])
    d_skills = np.array([int(x) for x in input().split(" ")])
    # Calculate swordsmen's difference with each weapon
    skill_diff = c_skills - d_skills
    skill_diff = [abs(x) for x in skill_diff]
    skill_diff_bin = skill_diff.copy()
    #Prepare for segment tree, if 1 then condition is met
    for j in range(0,n):
        if skill_diff[j] <= k:
            skill_diff_bin[j] = '1'
        else:
            skill_diff_bin[j] = '0'
    #Create all possible subsets
    subs = ''.join(skill_diff_bin)
    subs = list(subs[i:j+1] for i in range (len(subs)) for j in range(i,len(subs)))
    print(subs)
    #Find all subsets that have at least one "1"
    counter = 0
    for subset in subs:
        if '1' in subset:
            counter = counter + 1
    #Print solution
    print("Case #{}: {}".format(i,counter))
