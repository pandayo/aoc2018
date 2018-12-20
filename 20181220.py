from collections import defaultdict
import operator

lines = open("input.txt").read().splitlines()

def create_ways(regex, spoint=(0,0), sdistance = 0, ival=-1):
    #print(regex, spoint, sdistance)
    ways = defaultdict(list)
    point = (0 + spoint[0], 0 + spoint[1]) 
    distance = 0 + sdistance
    for i in range(len(regex)):
        val = regex[i]
        if i <= ival:
            continue
        if val == "N":
            point = (point[0] - 1, point[1] + 0)
            distance += 1
            ways[point].append(distance)
        elif val == "E":
            point = (point[0] + 0, point[1] + 1)
            distance += 1
            ways[point].append(distance)
        elif val == "S":
            point = (point[0] + 1, point[1] + 0)
            distance += 1
            ways[point].append(distance)
        elif val == "W":
            point = (point[0] + 0, point[1] - 1)
            distance += 1
            ways[point].append(distance)
        elif val == "(":
            #start new way
            ipoint = (point[0] + 0, point[1] + 0)
            iways, ival = create_ways(regex, ipoint, distance, i)
            for key, value in iways.items():
                ways[key].extend(value)
        elif val == "|":
            point = (0 + spoint[0], 0 + spoint[1])
            distance = 0 + sdistance
        elif val == ")":
            return(ways, i)
    return(ways, i)
for line in lines:
    print(line)
    ways, counter = create_ways(line[1:-1])
    print(max([min(v[1]) for v in ways.items()]))
    print(sum([1 for v in ways.items() if min(v[1]) >= 1000]))
    #print(ways)
