###############################################################################
#                               Functions                                     #
###############################################################################
def partI(part, codes, debug = False):
    commands = {"addr":addr, "addi":addi, "mulr":mulr, "muli":muli,
                "banr":banr, "bani":bani, "borr":borr, "bori":bori,
                "setr":setr, "seti":seti, "gtir":gtir, "gtri":gtri,
                "gtrr":gtrr, "eqir":eqir, "eqri":eqri, "eqrr":eqrr}
    register = part["Before"]
    cmd = part["Instructions"]
    result = part["After"]
    possible = 0
    for command in commands:
        start = [r for r in register]
        if commands[command](start, cmd[1], cmd[2], cmd[3]) == result:
            possible += 1
            codes[command][cmd[0]] += 1
    if debug:
        for line in codes:
            print(line, codes[line])
    return(possible, codes)

def partII(register, cmd, cmds):
    commands = {"addr":addr, "addi":addi, "mulr":mulr, "muli":muli,
                "banr":banr, "bani":bani, "borr":borr, "bori":bori,
                "setr":setr, "seti":seti, "gtir":gtir, "gtri":gtri,
                "gtrr":gtrr, "eqir":eqir, "eqri":eqri, "eqrr":eqrr}
    return(commands[cmds[cmd[0]]](register, cmd[1], cmd[2], cmd[3]))

def addr(register, A, B, C):
    register[C] = register[A]+register[B]
    return(register)

def addi(register, A, B, C):
    register[C] = register[A]+B
    return(register)

def mulr(register, A, B, C):
    register[C] = register[A]*register[B]
    return(register)

def muli(register, A, B, C):
    register[C] = register[A]*B
    return(register)

def banr(register, A, B, C):
    register[C] = register[A]&register[B]
    return(register)

def bani(register, A, B, C):
    register[C] = register[A]&B
    return(register)

def borr(register, A, B, C):
    register[C] = register[A]|register[B]
    return(register)

def bori(register, A, B, C):
    register[C] = register[A]|B
    return(register)

def setr(register, A, B, C):
    register[C] = register[A]
    return(register)

def seti(register, A, B, C):
    register[C] = A
    return(register)

def gtir(register, A, B, C):
    if A > register[B]:
        register[C] = 1
    else:
        register[C] = 0
    return(register)

def gtri(register, A, B, C):
    if B < register[A]:
        register[C] = 1
    else:
        register[C] = 0
    return(register)

def gtrr(register, A, B, C):
    if register[A] > register[B]:
        register[C] = 1
    else:
        register[C] = 0
    return(register)

def eqir(register, A, B, C):
    if register[A] == B:
        register[C] = 1
    else:
        register[C] = 0
    return(register)

def eqri(register, A, B, C):
    if register[B] == A:
        register[C] = 1
    else:
        register[C] = 0
    return(register)

def eqrr(register, A, B, C):
    if register[A] == register[B]:
        register[C] = 1
    else:
        register[C] = 0
    return(register)

def interpret_cmd(register, cmd):
    return

###############################################################################
#                                Script                                       #
###############################################################################
lines = open("input.txt").read().splitlines()

inputPartI = []
before = None
instruction = None
after = None
last_line = ""
end_of_example = 0
codes = {"addr":[0 for i in range(16)], "addi":[0 for i in range(16)],
         "mulr":[0 for i in range(16)], "muli":[0 for i in range(16)],
         "banr":[0 for i in range(16)], "bani":[0 for i in range(16)],
         "borr":[0 for i in range(16)], "bori":[0 for i in range(16)],
         "setr":[0 for i in range(16)], "seti":[0 for i in range(16)],
         "gtir":[0 for i in range(16)], "gtri":[0 for i in range(16)],
         "gtrr":[0 for i in range(16)], "eqir":[0 for i in range(16)],
         "eqri":[0 for i in range(16)], "eqrr":[0 for i in range(16)]}

for v, line in enumerate(lines):
    if line[:8] == "Before: ":
        before = line[9:-1].split(", ")
        for i, c in enumerate(before):
            before[i] = int(c)
    elif line[:8] == "After:  ":
        after = line[9:-1].split(", ")
        for i, c in enumerate(after):
            after[i] = int(c)
    elif len(line) != 0:
        instruction = line.split(" ")
        for i, c in enumerate(instruction):
            instruction[i] = int(c)
    if len(line) == 0 and len(last_line) != 0:
        inputPartI.append({"Before":before,
                           "After":after,
                           "Instructions":instruction})
    if len(line) == 0 and len(last_line) == 0:
        end_of_example = v
        break
    last_line = line
print("INPUT")
print(len(inputPartI))
print(end_of_example)

part_I = 0

test = {"Before": [3, 2, 1, 1],
"Instructions": [9, 2, 1, 2],
"After":  [3, 2, 2, 1]}

for part in inputPartI:
    val, codes = partI(part, codes)
    if val > 2:
        part_I += 1
print("PART I")
print(part_I)

print("PART II")
print(sorted(codes.items(),
                   key = lambda v: len([k for k in v[1] if k])))
inst = [None for i in range(16)]

list_of_combs = sorted(codes.items(),
                       key = lambda v: len([k for k in v[1] if k]))
while None in inst:
    new_list = []
    for comb in list_of_combs:
        open_pos = 0
        if sum(comb[1]) > 0:
            for i, v in enumerate(comb[1]):
                if comb[1][i] != 0:
                    if inst[i] is None and comb[1][i] != 0:
                        comb[1][i] = v
                        open_pos += 1
                    else:
                        comb[1][i] = 0
            new_list.append(comb)
            if open_pos > 1:
                continue
            for i, v in enumerate(comb[1]):
                if v and inst[i] is None:
                    inst[i] = comb[0]
    list_of_combs = new_list

print(inst)

instructions = []
for v, line in enumerate(lines):
    if v > end_of_example:
        if len(line) != 0:
            instruction = line.split(" ")
            for i, c in enumerate(instruction):
                instruction[i] = int(c)
            instructions.append(instruction)
print(len(instructions))

register = [0, 0, 0, 0]
for i, cmd in enumerate(instructions):
    register = partII(register, cmd, inst)
    if i % 250 == 0:
        print(i, register)
print(register)
