#Read input
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    p,q = [int(x) for x in input().split(" ")]
    #Create possiblity tables
    row = [0]* (q+1)
    col = [0]* (q+1)
    #Read each person
    for j in range(0,p):
        x,y,dir = input().split(' ')
        x = int(x)
        y = int(y)
        #Check direction and increase possibility tables
        if dir == 'N':
            for k in range(y+1,q+1):
                col[k] = col[k]+1
        elif dir == 'S':
            for k in range(0,y):
                col[k] = col[k]+1
        elif dir == 'W':
            for k in range(0,x):
                row[k] = row[k]+1
        else:
            for k in range(x+1,q+1):
                row[k] = row[k]+1
        #Find max column and row
        y_max = max(col)
        x_max = max(row)
        #Find position of max
        for pos in range(0,q+1):
            if row[pos] == x_max:
                pos_x_max = pos
                break
        for pos in range(0,q+1):
            if col[pos] == y_max:
                pos_y_max = pos
                break
    #Print solution
    print("Case #{}: {} {}".format(i,pos_x_max,pos_y_max))
