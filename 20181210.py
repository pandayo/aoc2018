import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lines = open("input.txt").read().splitlines()

points = np.empty((0,4), int)

for line in lines:
    position = line.split("> ")[0][len("position=<"):].split(", ")
    position[0], position[1] = int(position[0]), int(position[1])
    velocity = line.split("> ")[1][len("velocity=<"):-1].split(", ")
    velocity[0], velocity[1] = int(velocity[0]), int(velocity[1])
    adding = np.array(
        [[position[0], -position[1], velocity[0], -velocity[1]]]
        )
    points = np.append(points, adding)

points = np.reshape(points, (len(lines), 4))

mx = max(points[:,0])
lx = min(points[:,0])
my = max(points[:,1])
ly = min(points[:,1])

dx = mx-lx+1
dy = mx-ly+1

counter = 0

while (mx-lx, my-ly) < (dx, dy):
    (dx, dy) = (mx-lx, my-ly)
    points[:,0:2] += points[:,2:]
    
    mx = max(points[:,0])
    lx = min(points[:,0])
    my = max(points[:,1])
    ly = min(points[:,1])
    counter += 1

points[:,0:2] -= points[:,2:]
plt.scatter(points[:,0], points[:,1])
plt.show()
print(counter-1)
