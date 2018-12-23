from collections import defaultdict

def man_dist(p1, p2):
    return(
        abs(p1[0]-p2[0])+
        abs(p1[1]-p2[1])+
        abs(p1[2]-p2[2])
        )

def in_max_range(max_pos, max_range, nanobots):
    counter = 0
    for key in nanobots:
        dist = man_dist(max_pos, key)
        if dist <= max_range:
            counter += 1
    return(counter)

def optimize(bots):
    ''' A binary search in 3 dimensions.

    Thanks /u/seligman99 for the help :)

    Had to adjust the solution a little for me to work.'''
    xs = [x[0] for x in bots]
    ys = [x[1] for x in bots]
    zs = [x[2] for x in bots]

    dist = 1
    while dist < min(max(xs) - min(xs), max(ys) - min(ys), max(zs) - min(zs)):
        dist *= 2

    while True:
        target_count = -1
        best = None
        best_val = None
        print("Distance is:", dist)
        for x in range(min(xs), max(xs) + 1, dist):
            for y in range(min(ys), max(ys) + 1, dist):
                for z in range(min(zs), max(zs) + 1, dist):
                    count = 0
                    for bcoords, brange in bots.items():
                        (bx, by, bz) = bcoords
                        idist = abs(x-bx) + abs(y-by) + abs(z-bz)
                        if (idist - brange)/dist <= 0:
                            count +=1
                    if count > target_count:
                        target_count = count
                        best_val = abs(x) + abs(y) + abs(z)
                        best = (x, y, z)
                    elif count == target_count:
                        if abs(x) + abs(y) + abs(z) < best_val:
                            best_val = abs(x) + abs(y) + abs(z)
                            best = (x, y, z)
        if dist == 1:
            return best, best_val
        else:
            xs = [best[0] - dist, best[0] + dist]
            ys = [best[1] - dist, best[1] + dist]
            zs = [best[2] - dist, best[2] + dist]
            dist = int(dist / 2)

lines = open("input.txt").read().splitlines()

nanobots = defaultdict(int)
max_range = 0
max_pos = None
max_x = max_y = max_z = 0
min_x = min_y = min_z = 1000000000

for line in lines:
    pos, r = line.split(", ")
    x, y, z = pos[5:-1].split(",")
    r = int(r[2:])
    x, y, z = int(x), int(y), int(z)
    nanobots[(x,y,z)] = r
    if r > max_range:
        max_range = r
        max_pos = (x, y, z)
    if x > max_x:
        max_x = x
    if x < min_x:
        min_x = x
    if y > max_y:
        max_y = y
    if y < min_y:
        min_y = y
    if z > max_z:
        max_x = x
    if z < min_z:
        min_z = z

print(len(nanobots), min_x, max_x, min_y, max_y, min_z, max_z)

#part 1
print("There is a total number of", in_max_range(max_pos, max_range, nanobots),
      "nanobots in the radius of", max_pos)

#part 2
best, val = optimize(nanobots)
print("The best location is ({0}, {1}, {2}) with a distance of {3}.".
      format(best[0], best[1], best[2], val))
