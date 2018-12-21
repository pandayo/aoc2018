from datetime import datetime
from collections import defaultdict

###############################################################################
#                               Functions                                     #
###############################################################################

def interpret_cmd(register, cmd, ip, ippos = 0):
    commands = {"addr":addr, "addi":addi, "mulr":mulr, "muli":muli,
                "banr":banr, "bani":bani, "borr":borr, "bori":bori,
                "setr":setr, "seti":seti, "gtir":gtir, "gtri":gtri,
                "gtrr":gtrr, "eqir":eqir, "eqri":eqri, "eqrr":eqrr}
    register[ippos] = ip
    register = commands[cmd[0]](register, cmd[1], cmd[2], cmd[3])
    ip = register[ippos]
    ip += 1
    return(register,ip)

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
    if register[B] == A:
        register[C] = 1
    else:
        register[C] = 0
    return(register)

def eqri(register, A, B, C):
    if register[A] == B:
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

def do_stuff(cmdset):
    ip = 0
    register = [0,0,0,0,0,0]
    counter = 0
    print(datetime.now(), register)
    while 0<=ip <len(cmdset):
        register, ip = interpret_cmd(register, cmdset[ip], ip, ippos)
        counter += 1
        if ip == 28:
            if register[3] in values:
                return(values)
            else:
                print(register[3], counter, len(values))
                values[register[3]] = counter

lines = open("test.txt").read().splitlines()

values = defaultdict(int)

ipconfig = lines[0]
lines.remove(ipconfig)
cmdset =[]


ippos = int(ipconfig.split(" ")[1])

for line in lines:
    cmd = line.split(" ")
    cmd[1] = int(cmd[1])
    cmd[2] = int(cmd[2])
    cmd[3] = int(cmd[3])
    cmdset.append(cmd)
    
values = do_stuff(cmdset)           

# Part I
print(datetime.now(),
      sorted(values.items(), key = lambda v: v[1], reverse=False)[0])

# Part II
print(datetime.now(),
      sorted(values.items(), key = lambda v: v[1], reverse=True)[0])

