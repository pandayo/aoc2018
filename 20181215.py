###############################################################################
# Walkable Path
###############################################################################

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return(self.position == other.position)

    def __str__(self):
        if not (self.parent is None):
            return("({0},{1},({2},{3},{4}))".format(self.parent.position, self.position,
                                                    self.g, self.h, self.f))
        else:
            return("( - ,{0},({1},{2},{3}))".format(self.position, self.g, self.h, self.f))

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

def astar(maze, start, end, debug = False):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    if debug: printMaze(maze, start, end)
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)
    counter = 1
    
    # Loop until you find the end
    while len(open_list) > 0:
        if counter % 10000 == 0:
            printMaze(maze, start, end)
            print(start," has not found ",end)
            return
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node.position == end_node.position:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return(path[::-1]) # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1)\
               or node_position[0] < 0\
               or node_position[1] > (len(maze[len(maze)-1]) -1)\
               or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) + (child.position[1] - end_node.position[1]))
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            if child not in open_list:
                open_list.append(child)
        counter += 1
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
        paths[rs] = astar(maze, (s_y, s_x), rs)
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
    closest = {}
    distance = len(area)**2
    for rpos, rpath in reachable_squares.items():
        if rpath is None:
            continue
        rdis = len(rpath)-1
        if rdis < distance:
            closest = {}
            distance = rdis
            closest[rpos] = rpath
        elif rdis == distance:
            closest[rpos] = rpath
    if len(closest) > 0:
        return(closest)

def chose_square(nearest_squares):
    future_position = list(nearest_squares.keys())
    return(nearest_squares[sorted(future_position)[0]][1])
                    
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
    if i % 100 == 0:
        print(printMap(area, units))        
    units = new_units
print(printMap(area, units))
rounds = i-1
sum_of_healths = sum([unit[1]["HP"] for unit in units.items()])
print(sum_of_healths)
print(sum_of_healths*rounds)
