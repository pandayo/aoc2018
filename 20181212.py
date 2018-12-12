lines = open("input.txt").read().splitlines()

initial_state = lines[0][15:]
rules = {}

for line in lines[2:]:
    rule, plant = line.split(" => ")
    rules[rule] = plant
#print(rules)

zero_index = 0

state = initial_state
if state[0:3] != "...":
    state = "..."+state
    zero_index += 3
print(state)
sums = []

for i in range(2000):
    sums.append(sum([index for index, value
                                   in enumerate(state, start = -zero_index)
                                   if value == "#"]))
    if state[-4:] != "....":
        state = state+"...."
    if state[0:3] != "...":
        state = "..."+state
        zero_index += 3
    if state[0:5] == ".....":
        state = state[2:]
        zero_index -= 2
    next_state = state[0:2]
    for j in range(2,len(state)-2):
        ruler = state[j-2:j+3]
        if ruler in rules:
            next_state += rules[ruler]
        else:
            next_state += "."
    state = next_state

sums.append(sum([index for index, value
                 in enumerate(state, start = -zero_index)
                 if value == "#"]))
differences = [sums[i]-sums[i-1] for i in range(1, len(sums))]

print(sums[20])

var = 2001

for i in range(1, len(differences)-1):
    if differences[i-1] == differences[i] and differences[i] == differences[i+1]:
        var = (i-1)
        break

multiplicator = 50000000000
product = (multiplicator - var)*differences[var] + sums[var]

print(product)
