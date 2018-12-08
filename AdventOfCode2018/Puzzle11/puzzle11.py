#Day6 Puzzle1
#get the coordinates of each point
coordinates = dict()
inputfile = [line.rstrip('\n') for line in open('p11.txt')]
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
        distance = 10000
        for id in range(len(coordinates)):
            coord = coordinates[id]
            coord_dist = abs(coord[0]-i) + abs(coord[1]-j)
            if coord_dist < distance:
                distance = coord_dist
                grid[i][j] = id
            elif coord_dist == distance: #same distance for multiple coordinates
                grid[i][j] = '.'
# calculate area for each coordinate
area = dict()
for i in range(len(coordinates)):
    area[i] = 0
for i in range(1000):
    for j in range(1000):
        if (grid[i][j] != '.'):
            if (grid[i][j] > 0):
                area[grid[i][j]] = area[grid[i][j]] +1
#value in the borders of the grid will have infinite area
inf = []
for i in range(min_x,max_x+1):
    inf.append(grid[i][min_y])
    inf.append(grid[i][max_y])
for j in range(min_y,max_y+1):
    inf.append(grid[min_x][j])
    inf.append(grid[max_x][j])
inf = list(set(inf))
inf.remove('.')
# remove infinite values from area dictionary
for i in range(len(inf)):
    del area[inf[i]]
#find maximum value from remaining areas
print (max(area.values()))
