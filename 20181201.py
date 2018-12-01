file = open("input.txt", "r")
lines = file.readlines()
maya = []
for line in lines:
	maya.append(int(line))
#Print end frequency
print(sum(maya))

values = set()
sum = 0
i = 0
while(not sum in values):
  values.add(sum)
  sum = sum + maya[i]
  i = (i+1)%len(maya)
#print first sum already in set
print(sum)
