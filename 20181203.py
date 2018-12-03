file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

inches = [[list() for i in range(1000)] for j in range(1000)]
overlap = 0
id_list = []

for line in lines:
    id_number = int(line.split('@')[0].strip().replace('#',''))
    coordinates, size = (line.split('@')[1].strip()).split(': ')
    x_start, y_start = coordinates.split(',')
    x_start = int(x_start)
    y_start = int(y_start)
    x_length, y_length = size.split('x')
    x_length = int(x_length)
    y_length = int(y_length)
    for i in range(x_start, x_start+x_length):
        for j in range(y_start, y_start+y_length):
            inches[i][j].append(id_number)
            if len(inches[i][j]) == 2:
                overlap = overlap + 1
    id_list.append({"id":id_number, "x_s":x_start, "x_l":x_length,
                    "y_s":y_start, "y_l":y_length})

print(overlap)
    
for id_type in id_list:
    solo = True
    x_start = id_type["x_s"]
    y_start = id_type["y_s"]
    x_length = id_type["x_l"]
    y_length = id_type["y_l"]
    for i in range(x_start, x_start+x_length):
        for j in range(y_start, y_start+y_length):
            if len(inches[i][j]) > 1:
                solo = False
    if solo:
        print(id_type["id"])
