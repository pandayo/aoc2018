from collections import defaultdict

depth = 3558
target = (15, 740)

el = defaultdict(int)

#test input
depth = 510
target = (10, 10)


for x in range(target[0]+5):
    for y in range(target[1]+5):
        geo_index = 0
        if x == 0 and y == 0:
            geo_index = 0
        elif y == 0:
            geo_index = x * 16807
        elif x == 0:
            geo_index = y * 48271
        elif (x, y) == target:
            geo_index = 0
        else:
            geo_index = el[(x-1, y)] * el[(x, y-1)]
        el[(x,y)] = (geo_index + depth) % 20183
print("Risk level: ", sum([value[1]%3 for value in el.items()
                           if value[0][0] <= target[0] and value[0][1] <= target[1]]))
