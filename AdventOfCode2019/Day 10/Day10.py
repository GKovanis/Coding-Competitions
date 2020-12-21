from math import atan2,pi

# Arctan between points a and b
def angle(a, b):
    return atan2(b[0] - a[0], a[1] - b[1]) % (2 * pi)

# Asteroid is visible if arctan is unique
def visible(asteroids, a):
    return len(set(angle(a, b) for b in asteroids if a != b))

def part1(asteroids):
    return max(visible(asteroids, a) for a in asteroids)


lines = [line.rstrip('\n') for line in open('p10.txt')]
# Find all asteroids / coordinates with '#'
asteroids = [(x, y) for y in range(len(lines))
    for x in range(len(lines[0])) if lines[y][x] == '#']

print(part1(asteroids))
print(part2(asteroids))
