#SOLUTION: JNOIKSYABEQRUVWXGTZFDMHLPC

def innerCheck(ilist, icheck, pre, req, counter):
        print("innerCheck "+str(counter))
        print(ilist)
        print(icheck)
        counter+=1
        for key in ilist:
                print("KEY: "+key)
                print(req[key])
                if all(rq in list(icheck) for rq in req[key]) and\
                   key not in list(icheck):
                        icheck+=key
                        icheck = innerCheck(sorted(pre[key]),
                                            icheck, pre, req, counter)
        return icheck

from collections import defaultdict

lines = open("input.txt", "r").read().splitlines()

pre = defaultdict(list)
req = defaultdict(list)
time = defaultdict(int)
allkey = set()

# define requirements per step
for line in lines:
	value = line[5]
	key = line[-12]
	# define requirements
	req[key].append(value)
	# define following steps
	pre[value].append(key)
	allkey.add(value)
	allkey.add(key)

ltf = sorted(req, key= lambda k: len(req[k]), reverse=True)
ftl = sorted(pre, key= lambda k: len(pre[k]))

for key in allkey:
	time[key] = 61+ord(key)-ord("A")        

output = ""
available = sorted(allkey.difference(ltf))

while len(available) != 0 and len(output) != len(allkey):
        key = sorted(available)[0]
        output += key
        for ikey in sorted(pre[key]):
                if all(rq in list(output) for rq in req[ikey]) and\
                   ikey not in list(output):
                        available.append(ikey)
        available.remove(key)
        
print(output)
print(time)
timePast = 0
for key in output:
        if key in req:
                zwPast = 0
                for ik in req[key]:
                        zwPast = max(zwPast, time[ik])
                time[key]+=zwPast
print(time["C"])
