T = int(input())

for test in range(T):
    # Read input
    N = input()
    L = [int(l) for l in input().split(" ")]
    # Create sorted list
    sortL = sorted(L)

    score = 0
    # Calculate score of each element and add it
    for l in L:
        element_score = L.index(l) - sortL.index(l) + 1
        print(L, element_score)
        score = score + element_score
    print ("Case #" + str(test + 1) + ": " + str(score))
