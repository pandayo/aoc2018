def printMap(arr_of_arr):
    output = ""
    for arr in arr_of_arr:
        for v in arr:
            output+=v
        output+="\n"
    print(output)

def printCarsOnMap(track, cars):
    printTrack = [[""+x for x in cL] for cL in track]
    for car in cars:
        printTrack[car[0]][car[1]] = car[2]
    printMap(printTrack)

def move(track, cars, counter):
    cars = sorted(cars, key = lambda el: (el[0], el[1]))
    newCars = []
    pos = set()
    destroyed = set()
    for car in cars:
        node = (car[0],car[1])
        pos.add(node)
    for car in cars:
        x = car[0]
        y = car[1]
        pos.remove((x,y))
        direction = car[2]
        count = car[3]
        car_destroyed=False
        if not (x,y) in destroyed:
            if direction == "<":
                y = y-1
                if not (x,y) in pos:
                    pos.add((x,y))
                else:
                    print("{0}: cars hit at ({1},{2})".
                          format(counter,y,x))
                    destroyed.add((x,y))
                    car_destroyed = True
                if track[x][y] == "\\":
                    direction = "^"
                if track[x][y] == "/":
                    direction = "v"
                if track[x][y] == "+":
                    if count % 3 == 0:
                        direction = "v"
                    if count % 3 == 2:
                        direction = "^"
                    count += 1
                if not car_destroyed:
                    newCars.append((x,y,direction,count))
                continue
            if direction == ">":
                y = y+1
                if not (x,y) in pos:
                    pos.add((x,y))
                else:
                    print("{0}: cars hit at ({1},{2})".
                          format(counter,y,x))
                    destroyed.add((x,y))
                    car_destroyed = True
                if track[x][y] == "/":
                    direction = "^"
                if track[x][y] == "\\":
                    direction = "v"
                if track[x][y] == "+":
                    if count % 3 == 0:
                        direction = "^"
                    if count % 3 == 2:
                        direction = "v"
                    count += 1
                if not car_destroyed:
                    newCars.append((x,y,direction,count))
                continue
            if direction == "^":
                x = x-1
                if not (x,y) in pos:
                    pos.add((x,y))
                else:
                    print("{0}: cars hit at ({1},{2})".
                          format(counter,y,x))
                    destroyed.add((x,y))
                    car_destroyed = True
                if track[x][y] == "\\":
                    direction = "<"
                if track[x][y] == "/":
                    direction = ">"
                if track[x][y] == "+":
                    if count % 3 == 0:
                        direction = "<"
                    if count % 3 == 2:
                        direction = ">"
                    count += 1
                if not car_destroyed:
                    newCars.append((x,y,direction,count))
                continue
            if direction == "v":
                x = x+1
                if not (x,y) in pos:
                    pos.add((x,y))
                else:
                    print("{0}: cars hit at ({1},{2})".
                          format(counter,y,x))
                    destroyed.add((x,y))
                    car_destroyed = True
                if track[x][y] == "\\":
                    direction = ">"
                if track[x][y] == "/":
                    direction = "<"
                if track[x][y] == "+":
                    if count % 3 == 0:
                        direction = ">"
                    if count % 3 == 2:
                        direction = "<"
                    count += 1
                if not car_destroyed:
                    newCars.append((x,y,direction,count))
                continue
    nC = [car for car in newCars if (car[0], car[1]) not in destroyed]
    return(nC)

lines = open("input.txt").read().splitlines()

cLines = [[x for x in y] for y in lines]
cars = {">":"-", "<":"-", "v":"|", "^":"|"}

carPos = []

for i, cL in enumerate(cLines):
    for j, c in enumerate(cL):
        if c in cars:
            carPos.append((i,j,c,0))
            if c in ("<",">"):
                cLines[i][j] = "-"
                if i > 0:
                    if cLines[i-1][j] == "|":
                        cLines[i][j] = "+"
                if i < len(cLines)-1:
                    if cLines[i+1][j] == "|":
                        clines[i][j] = "+"
            if c in ("v","^"):
                cLines[i][j] = "|"
                if j > 0:
                    if cLines[i][j-1] == "-":
                        cLines[i][j] = "+"
                if j < len(cL)-1:
                    if cLines[i][j+1] == "-":
                        clines[i][j] = "+"
printMap(cLines)
print(carPos)
print(len(carPos))
counter = 0

while len(carPos) > 1:
    carPos = move(cLines, carPos, counter)
    counter += 1
    #printCarsOnMap(cLines, carPos)
print(carPos)
