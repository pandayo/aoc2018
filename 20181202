def hashSum(lines):
    symbol = 'abcdefghijklmnopqrstuvwxyz'
    amounts = {2 : 0, 3 : 0}
    for line in lines:
        two = False
        three = False
        for key in symbol:
            count = line.count(key)
            if count == 2 and not two:
                two = True
                amounts[count] = amounts[count]+1
            if count == 3 and not three:
                three = True
                amounts[count] = amounts[count]+1
    return(amounts[2]*amounts[3])

def distance(line1, line2):
    if len(line1) == len(line2):
        distance = 0
        for i in range(len(line1)):
            if line1[i] != line2[i]:
                distance = distance+1
        return distance
    else:
        print("--------------------")
        print(line1+", "+line2)
        print(str(len(line1))+", "+str(len(line2)))

def sameChars(line1, line2):
    returning = ""
    for i in range(len(line1)):
        if line1[i] == line2[i]:
            returning = returning + line1[i]
    return(returning)

file = open("input.txt", "r")
lines = file.readlines()
lines = [line.strip() for line in lines]

print(hashSum(lines))

for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        line1 = lines[i]
        line2 = lines[j]
        if distance(line1, line2) == 1:
            print(line1+", "+line2)
            print(sameChars(line1, line2))
