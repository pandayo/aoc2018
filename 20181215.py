###############################################################################
# Walkable Path
###############################################################################
import collections

def printMaze(maze, start, end):
    output = ""
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if (y,x) == start or (y,x) == end:
                if (y,x) == start:
                    output += "s"
                else:
                    output += "e"
            else:
                output += str(maze[y][x])
        output += "\n"
    print(output)

def bfs(maze, start, end, wall = 1):
    width = len(maze[0])
    height = len(maze)    
    queue = collections.deque([[start]])
    seen = set([start])
    paths = []
    while queue:
        path = queue.popleft()
        y, x = path[-1]
        if (y,x) == end:
            paths.append(path)
            continue
        for (yi,xi) in [(y-1, x), (y, x-1), (y, x+1), (y+1, x)]:
            if width > xi >= 0 and maze[yi][xi] != wall and (yi,xi) not in seen:
                queue.append(path + [(yi, xi)])
                seen.add((yi,xi))
    if len(paths) == 1:
        return(paths[0])
    elif len(paths) > 1:
        paths = sorted(paths, key = lambda k : len(k))
        l_k = len(paths[0])
        paths = [path for path in paths if len(path) == l_k]
###############################################################################

def printMap(area, units):
    output = ""
    for y in range(len(area)):
        line_units = []
        for x in range(len(area[y])):
            if (y,x) in units:
                line_units.append(units[(y,x)])
                output += units[(y,x)]["Type"]
            else:
                output += area[y][x]
        if len(line_units) > 0:
            output += "   "
        for unit in line_units:
            output += "{0}({1:3d}) ".format(unit["Type"], unit["HP"])
        output += "\n"
    return(output)

def identify_targets(unit, units):
    targets = {}
    for enemy in units.items():
        if enemy[1]["Type"] != unit[1]["Type"]:
            targets[enemy[0]] = enemy[1]
    return(targets)

def identify_range(area, units, targets):
    ranges = []
    for target in targets:
        (y,x) = targets[target]["Position"]
        for i in [-1,1]:
            if not area[y+i][x] == "#":
                if (y+i,x) not in units:
                    ranges.append((y+i,x))
            if not area[y][x+i] == "#":
                if (y,x+i) not in units:
                    ranges.append((y,x+i))
    return(ranges)

def is_reachable(area, units, unit, range_squares):
    maze = []
    for y in range(len(area)):
        xmaze = []
        for x in range(len(area[y])):
            if area[y][x] == "#" or (y,x) in units:
                xmaze.append(1)
            else:
                xmaze.append(0)
        maze.append(xmaze)
    (s_y, s_x) = unit[1]["Position"]
    paths = {}
    for rs in range_squares:
        paths[rs] = bfs(maze, (s_y, s_x), rs)
    return(paths)

def find_attackable(pos, targets, debug = False):
    attackable = None
    attackableHP = 300
    for key in sorted(targets.keys()):
        if debug: print(key)
        if debug: print(pos)
        if debug: print("dis:",abs(key[0]-pos[0])+abs(key[1]-pos[1]))
        if (abs(key[0]-pos[0]) == 0 and abs(key[1]-pos[1]) == 1) or\
           (abs(key[0]-pos[0]) == 1 and abs(key[1]-pos[1]) == 0):
            if attackableHP > targets[key]["HP"]:
                attackableHP = targets[key]["HP"]
                attackable = key
            elif attackableHP == targets[key]["HP"]:
                if attackable > key:
                    attackable = key
    return(attackable)
        
def is_nearest(area, units, unit, reachable_squares):
    closest = []
    distance = len(area)**2
    for rpos, rpath in reachable_squares.items():
        if rpath is None:
            continue
        rdis = len(rpath)-1
        if rdis < distance:
            closest = []
            distance = rdis
            closest.append((rpos, rpath))
        elif rdis == distance:
            closest.append((rpos, rpath))
    if len(closest) > 0:
        return(closest)

def chose_square(nearest_squares):
    l_k = sorted(nearest_squares, key = lambda v: v[0])[0][0]
    n_s = sorted([v for v in nearest_squares if v[0] == l_k], key = lambda v: v[1][1])
    return(n_s[0][1][1])
                    
file_name = "input.txt"
area = [[x for x in line] for line in open(file_name, "r").read().splitlines()]

elves = {}
goblins = {}

for y in range(len(area)):
    for x in range(len(area[y])):
        if area[y][x] == "E":
            elves[(y,x)] = {"Type":"E", "HP":200,
                          "AP":3, "Position":(y, x)}
            area[y][x] = "."
        elif area[y][x] == "G":
            goblins[(y,x)] = {"Type":"G", "HP":200,
                          "AP":3, "Position":(y, x)}
            area[y][x] = "."

units = {**elves, **goblins}
elves = len(elves)
goblins = len(goblins)
i = 1

print(printMap(area, units))
while elves > 0 and goblins > 0:
#for j in range(29):
    print("-----{0:2d}-----".format(i))
    new_units = units
    for unit in sorted(units.items(), key=lambda z: z[1]["Position"]):
        if unit[0] in new_units:
            #print("unit :", unit)
            t = identify_targets(unit, new_units)
            a = find_attackable(unit[0], t)
            if not(a is None):
                units[a]["HP"] -= unit[1]["AP"]
                if units[a]["HP"] < 1:
                    if units[a]["Type"] == "E":
                        elves -= 1
                    else:
                        goblins -= 1
                    del new_units[a]
            else:
                r = identify_range(area, new_units, t)
                reachable_squares = is_reachable(area, new_units, unit, r)
                if len(reachable_squares) > 0:
                    nearest_squares = is_nearest(area, new_units, unit, reachable_squares)
                    if not(nearest_squares is None):
                        cs = chose_square(nearest_squares)
                        if not (cs is None):
                            new_units[cs] = unit[1]
                            new_units[cs]["Position"] = cs
                            del new_units[unit[0]]
                            t = identify_targets(unit, new_units)
                            a = find_attackable(cs, t)
                            if not(a is None):
                                units[a]["HP"] -= unit[1]["AP"]
                                if units[a]["HP"] < 1:
                                    if units[a]["Type"] == "E":
                                        elves -= 1
                                    else:
                                        goblins -= 1
                                    del new_units[a]
    i += 1
    print(printMap(area, units))        
    units = new_units
print(printMap(area, units))
rounds = i-1
sum_of_healths = sum([unit[1]["HP"] for unit in units.items()])
print(sum_of_healths)
print(sum_of_healths*rounds)
