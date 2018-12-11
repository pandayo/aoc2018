import numpy as np
puzzle_input = 1723

def power_level(x, y):
    rack_id = x+10
    power_level = (x+10)*y
    return ((((power_level+puzzle_input)*rack_id)//100) % 10 - 5)

grid = np.fromfunction(power_level, (300,300))

for i in range(3, 300):
    x_max = -1
    y_max = -1
    max_power = -1
    for x in range(300-i):
        for y in range(300-i):
            ttl_pwr = sum(sum(grid[x:x+i,y:y+i]))
            if ttl_pwr > max_power:
                x_max = x
                y_max = y
                max_power = ttl_pwr
                max_size = 1
    print(x_max, y_max, max_power, i)
