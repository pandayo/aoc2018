from collections import defaultdict

def manhattanDistance(p1, p2):
    return(abs(p1[0]-p2[0])+abs(p1[1]-p2[1]))

file = open("input.txt", "r")
lines = file.read().splitlines()

coords = set()
maxx = -1
maxy = -1
minx = 10000
miny = 10000

for line in lines:
    xi, yi = [int(key) for key in line.split(", ")]
    if maxx < xi:
        maxx = xi
    if maxy < yi:
        maxy = yi
    if minx > xi:
        minx = xi
    if miny > yi:
        miny = yi
    coords.add((xi, yi))

coords_count = defaultdict(int)
infinite_coords = set()
region = 0

for x in range(maxx+1):
    for y in range(maxy+1):        
        vals = sorted([(manhattanDistance(p, (x,y)), p) for p in coords])
        sum_vals = 0
        for dist_tuple in vals:
            sum_vals += dist_tuple[0]
        if sum_vals < 10000:
            region += 1
        if vals[1][0] != vals[0][0]:
            coords_count[vals[0][1]] += 1
            if x == 0 or y == 0 or x == maxx or y == maxy:
                infinite_coords.add(vals[0][1])

print(max([coords_count[p] for p in coords if p not in infinite_coords]))
print(region)
