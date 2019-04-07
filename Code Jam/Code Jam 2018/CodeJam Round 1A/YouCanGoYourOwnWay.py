#Read input
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    grid_size = int(input())
    path = list(input())
    for letter in range(len(path)):
        if path[letter] == 'E':
            path[letter] = 'S'
        else:
            path[letter] = 'E'
    path = ''.join(path)
    #Print Solution
    print("Case #{}: {}".format(i,path))
