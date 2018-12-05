file = open("input.txt", "r")

### Part 1 ###

line = file.read().splitlines()[0]
oldline = None
while(line != oldline):
    oldline = line
    for key in "abcdefghijklmnopqrstuvwxyz":
        line = line.replace(key+key.upper(),"")
        line = line.replace(key.upper()+key,"")
print("--------------------")
print("-------Part 1-------")
print("--------------------")
print("-       "+str(len(line))+"      -")
print("--------------------")

### Part 2 ###

lenDict = {}
bestLine = line
for key in "abcdefghijklmnopqrstuvwxyz":
    valueLine = line.replace(key, "").replace(key.upper(),"")
    oldline = None
    while(valueLine != oldline):
        oldline = valueLine
        for key in "abcdefghijklmnopqrstuvwxyz":
            valueLine = valueLine.replace(key+key.upper(),"")
            valueLine = valueLine.replace(key.upper()+key,"")
    if len(valueLine) < len(bestLine):
        bestLine = valueLine
print("-------Part 2-------")
print("--------------------")
print("-        "+str(len(bestLine))+"      -")
print("--------------------")
