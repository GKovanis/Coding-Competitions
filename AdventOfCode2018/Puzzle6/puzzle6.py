#Find the only line that doesn't overlap
# @x,y coordinates : (x*y) size

#initialize 2D-grid
grid = []
for i in range(1100):
    column=[]
    for j in range(1100):
        column.append(0)
    grid.append(column)

#Parse coordinates and size
inputfile = [line.rstrip('\n') for line in open('p6.txt')]
for line in range(len(inputfile)):
    temp = inputfile[line].split()
    #x,y coordinates
    x,y = [int(x) for x in temp[2].rstrip(':').split(',')]
    #get size of field
    sizeX,sizeY = [int(x) for x in temp[3].split('x')]
    #mark field in grid
    for i in range(sizeX):
        for j in range(sizeY):
            if grid[x+i][y+j]==1:
                grid[x+i][y+j] +=1
            else:
                grid[x+i][y+j] +=1
#Run again to find ID
inputfile = [line.rstrip('\n') for line in open('p6.txt')]
for line in range(len(inputfile)):
    temp = inputfile[line].split()
    #x,y coordinates
    x,y = [int(x) for x in temp[2].rstrip(':').split(',')]
    #get size of field
    sizeX,sizeY = [int(x) for x in temp[3].split('x')]
    #if flag = true at end of iteration, grid doesn't overlap
    flag = True
    for i in range(sizeX):
        for j in range(sizeY):
            if grid[x+i][y+j]>1:
                flag = False
    if flag:
        print(temp[0])
