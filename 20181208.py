def createNode(data, totalMeta, counter = 0):
    kids = data[0]
    meta = data[1]
    kidNodes = []
    kidVs = []
    value = 0
    data = data[2:]
    if kids > 0:
        for kid in range(kids):
            kid, data, totalMeta, kidV = createNode(data,
                                                    totalMeta,
                                                    counter+1)
            kidNodes.append(kid)
            kidVs.append(kidV)
    metaList = data[0:meta]
    totalMeta.append(metaList)
    if kids == 0:
        value = sum(metaList)
    else:
        for meta_i in metaList:
            if meta_i <= kids:
                value += kidVs[meta_i-1]
    #print(counter, value, kids, meta)
    return {"kids":kids, "meta":meta,
            "kN":kidNodes, "mL":metaList}, data[meta:], totalMeta, value

tree = [int(x) for x in open("input.txt").read().split(" ")]

#print(len(tree))
totalMeta = []

baseNode, data, totalMeta, value = createNode(tree, totalMeta)

mL = []

for metaList in totalMeta:
    for value_i in metaList:
        mL.append(value_i)

#print(len(totalMeta))
#print(len(mL))
print(sum(mL))
print(value)

