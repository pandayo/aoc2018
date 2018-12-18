from collections import defaultdict

def renderMinute(fields, x, y):
    counter = defaultdict(int)
    for iy in range(y-1, y+2):
        for ix in range(x-1, x+2):
            if (ix != x or iy != y) and\
               0 <= ix < len(fields[y]) and\
               0 <= iy < len(fields):
                counter[fields[iy][ix]] += 1
    if fields[y][x] == ".":
        if counter["|"] > 2:
            return("|")
        else:
            return(".")
    elif fields[y][x] == "|":
        if counter["#"] > 2:
            return("#")
        else:
            return("|")
    else:
        if counter["#"] > 0 and counter["|"] > 0:
            return("#")
        else:
            return(".")

def printField(fields):
    for line in fields:
        output = ""
        for v in line:
            output += v
        print(output)

lines = open("input.txt").read().splitlines()

fields = []

for line in lines:
    il = []
    for v in line:
        il.append(v)
    fields.append(il)

printField(fields)
fieldOfValues = []
for i in range(829):
    nf = []
    for y in range(len(fields)):
        nfl = []
        for x in range(len(fields[y])):
            nfl.append(renderMinute(fields, x, y))
        nf.append(nfl)
    fields = nf

    countdict = defaultdict(int)
    for y in fields:
        for x in y:
            countdict[x]+=1
    fieldOfValues.append(countdict["#"]*countdict["|"])
    print(i, fieldOfValues[i])

distance = 0

for i in range(800,829):
    if fieldOfValues[799] == fieldOfValues[i]:
        distance = i-799
        break

print(distance)

print((1000000000-800)/distance%1*distance)
print(800+(1000000000-800)/distance%1*distance)
print(fieldOfValues[int(800+(1000000000-800)/distance%1*distance)])


