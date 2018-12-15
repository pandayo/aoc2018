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


def astar(imaze, units, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    maze = []

    for y in range(len(imaze)):
        xmaze = []
        for x in range(len(imaze[y])):
            if imaze[y][x] == "#" or (x,y) in units:
                xmaze.append(1)
            else:
                xmaze.append(0)
        maze.append(xmaze)

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

    # Loop until you find the end
    while len(open_list) > 0:

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
            child.h = ((child.position[0] - end_node.position[0])) + ((child.position[1] - end_node.position[1]))
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
###############################################################################

def take_turn(unit, area, units):
    targets = identify_targets(unit, units)
    open_squares = identify_range(area, units, targets)
    if (unit.x, unit.y) in open_squares:
        return(attack(area, units, unit, open_squares[(unit.x, unit.y)]))
    else:
        return(move(area, units, unit, open_squares))

def move(area, units, unit, open_squares):
    range_squares = in_range(area, units, unit, open_squares)
    reachable_squares = is_reachable(area, units, unit, range_squares)
    nearest_squares = is_nearest(area, units, unit, reachable_squares)
    chosen_square = chose_square(area, units, unit, nearest_squares)
    return(mutcs(area, units, unit, chosen_square))

def printMap(area, units):
    output = ""
    for y in range(len(area)):
        line_units = []
        for x in range(len(area[y])):
            if (x,y) in units:
                line_units.append(units[(x,y)])
                output += units[(x,y)]["Type"]
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
        (x,y) = targets[target]["Position"]
        for i in range(-1,0,2):
            if not area[y+i][x] == "#":
                if (x,y+i) not in units:
                    ranges.append((x,y+i))
            if not area[y][x+i] == "#":
                if (x+i,y) not in units:
                    ranges.append((x+i,y))
    return(ranges)

def is_reachable(area, units, unit, range_squares):
    (s_x, s_y) = unit[1]["Position"]
    paths = {}
    for rs in range_squares:
        paths[rs] = astar(area, units, (s_x, s_y), rs)
    return(paths)
        
def is_nearest(area, units, unit, reachable_squares):
    closest = {}
    for rs in reachable_squares:
        print(rs)
    
                    
file_name = "test.txt"
area = [[x for x in line] for line in open(file_name, "r").read().splitlines()]

elves = {}
goblins = {}

for y in range(len(area)):
    for x in range(len(area[y])):
        if area[y][x] == "E":
            elves[(x,y)] = {"Type":"E", "HP":200,
                          "AP":3, "Position":(x, y)}
            area[y][x] = "."
        elif area[y][x] == "G":
            goblins[(x,y)] = {"Type":"G", "HP":200,
                          "AP":3, "Position":(x, y)}
            area[y][x] = "."

units = {**elves, **goblins}

print(printMap(area, units))
#print(sorted(units.items(), key=lambda z: z[1]["Position"]))
##while len(elves) > 0 and len(goblins) > 0:
##    new_units = units
for unit in sorted(units.items(), key=lambda z: z[1]["Position"]):
    if unit[0] in list(units.keys()):
        t = identify_targets(unit, units)
        r = identify_range(area, units, t)
        reachable_squares = is_reachable(area, units, unit, r)
        is_nearest(area, units, unit, reachable_squares)
        
##            area, new_units = take_turn(unit, area, units)
##    print(printMap(area, units))
##    units = new_units
##    elves = [units[unit] for unit in units if units[unit]["Type"] == "E"]
##    goblins = [units[unit] for unit in units if units[unit]["Type"] == "G"]
