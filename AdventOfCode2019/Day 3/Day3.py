import sys
from math import sqrt

wires = [line.rstrip('\n').split(',') for line in open('p3.txt')]
wire_points = [[],[]]

# Create a list
for wire in range(len(wires)):
    x,y = 0,0
    for path in range(len(wires[wire])):
        direction = wires[wire][path][0] #R,L,U,D
        for steps in range((int(wires[wire][path][1:]))):
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y += 1
            else:
                y -= 1
            wire_points[wire].append((x,y))

""" Part 1
# Find interesection
common_points = list(set(wire_points[0]) & set(wire_points[1]))
min_dis = sys.maxsize
for point in common_points:
    distance = sqrt(point[0]**2 + point[1]**2)
    if distance < min_dis:
        min_dis = distance
print(min_dis)
"""

# Part 2
common_points = list(set(wire_points[0]) & set(wire_points[1]))
min_steps = sys.maxsize
for point in common_points:
    steps = wire_points[0].index(point) + wire_points[1].index(point)
    if steps < min_steps:
        min_steps = steps
print(min_steps)
