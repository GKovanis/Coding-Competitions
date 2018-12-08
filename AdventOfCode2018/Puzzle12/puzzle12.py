#Day6 Puzzle1
#get the coordinates of each point
coordinates = dict()
inputfile = [line.rstrip('\n') for line in open('p12.txt')]
for i in range(len(inputfile)):
    coordinates[i] = list(map(int,inputfile[i].split(", ")))
#find limits of the grid (min and max x,y)
x_values = [x[0] for x in coordinates.values()]
min_x,max_x = min(x_values), max(x_values)
y_values = [y[0] for y in coordinates.values()]
min_y,max_y = min(y_values),max(y_values)
#fill the grid appropriately
#initialize 2D-grid
grid = []
for i in range(1000):
    column=[]
    for j in range(1000):
        column.append(0)
    grid.append(column)
#fill grid appropriately
for i in range(min_x,max_x+1):
    for j in range(min_y,max_y+1):
        #calculate distance for each point for all coordinates
        distance = 0
        for id in range(len(coordinates)):
            coord = coordinates[id]
            coord_dist = abs(coord[0]-i) + abs(coord[1]-j)
            distance = distance + coord_dist
        grid[i][j] = distance
area = 0
for i in range(1000):
    for j in range(1000):
        if (grid[i][j] <10000 and grid[i][j]>0):
            area = area + 1
print(area)
