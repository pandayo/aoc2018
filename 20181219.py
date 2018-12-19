from datetime import datetime

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

def do_ip11(r):
    while r[5] == 10:
        # ip = 11
        r[5] = 2
        # ip = r[5]+1 = 3
        r[3] = r[4] * r[1]
        # ip = 4 .. 7
        if r[2] == r[3]:
            r[0] += r[4]
        # ip = 8
        r[1] += 1
        # ip = 9
        r[3] = 1 if r[1] > r[2] else 0
        # ip = 10
        r[5] = 10 + r[3]
    
    return(r, r[5]+1)

def do_ip12(register):
    register[4]+=1
    if register[4] > register[2]:
        register[5] = 16**2
        print(register)
        return(register, register[5]+1)
    else:
        # ip 2
        register[1] = 1
        # ip 3
        register[3] = register[4]
        if register[3] == register[2]:
            register[0] += register[4]
        # ip 8
        register[1] += 1
        if register[1] > register[2]:
            register[5] = 10
        else:
            register[5] = 11
        return(register, register[5]+1)
    
        


lines = open("test.txt").read().splitlines()

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
print(cmdset[2])

ip = 0
register = [0,0,0,0,0,0]



while 0<=ip <len(cmdset):
#for i in range(100):
    if ip == 11:
        register, ip = do_ip11(register)
    #elif ip == 12:
    #    register, ip = do_ip12(register)
    else:
        if register[2]==register[3]: print("ip", ip, register, cmdset[ip])
        register, ip = interpret_cmd(register, cmdset[ip], ip, ippos)

print(datetime.now(), register)

ip = 0
register = [1,0,0,0,0,0]

while 0<=ip <len(cmdset):
#for i in range(100):
    if ip == 11:
        register, ip = do_ip11(register)
        #print("-----{0:2d}-----".format(ip))
##        #print(register)
    #elif ip == 12:
    #    register, ip = do_ip12(register)
    else:
        print(ip, register)
        register, ip = interpret_cmd(register, cmdset[ip], ip, ippos)
print(datetime.now(), register)
