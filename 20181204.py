def extractInformation(line):
    year = int(line[1:5])
    month = int(line[6:8])
    day = int(line[9:11])
    hour = int(line[12:14])
    minute = int(line[15:17])
    information = line[19:-1].strip()
    if information[0] == "G":
        ID = information[7:-13]
        information = "shift"
    else:
        ID = None
        if information[0] == "f":
            information = "sleep"
        else:
            information = "awake"
    return({"year":year, "month":month, "day":day,
            "hour":hour, "minute":minute,
            "information":information, "ID":ID})

import pandas as pd
import numpy as np
from operator import itemgetter

file = open("input.txt", "r")
lines = file.readlines()

values = [extractInformation(line) for line in lines]
sorted_values = sorted(values,
                       key=itemgetter("year","month",
                                      "day","hour",
                                      "minute"))
for i in range(1,len(sorted_values)):
    if sorted_values[i]["ID"] is None:
        sorted_values[i]["ID"] = sorted_values[i-1]["ID"]

editedValues = []

for line in sorted_values:
    if not line["information"] == "shift":
        dictVal = {"ID":line["ID"],
                   "month":line["month"],
                   "day":line["day"]}
        if line["information"] == "sleep":
            value = 1
        else:
            value = -1
        for i in range(60):
            if i < line["minute"]:
                dictVal["{0:02d}".format(i)]=0
            else:
                dictVal["{0:02d}".format(i)]=value
        editedValues.append(dictVal)

df = pd.DataFrame(editedValues)
dfSummed = df.groupby(["ID","day","month"]).aggregate(sum)
dfIDSum = dfSummed.\
     groupby(["ID"]).aggregate(sum)
#print(dfIDSum.head(23))
dfComplete = dfIDSum.aggregate(sum, axis=1).idxmax()
print("--------------------")
print("-     Part One     -")
print("--------------------")
print(dfComplete)
print("--------------------")
print(dfIDSum.loc[dfComplete].idxmax())
print("--------------------")
print(int(dfIDSum.loc[dfComplete].idxmax())*int(dfComplete))
dfIDMean = dfSummed.\
     groupby(["ID"]).aggregate('mean')
print("--------------------")
print("-     Part Two     -")
print("--------------------")
#print(dfIDMean.head(23))
dfIDMeanMax = dfIDMean.aggregate('max', axis=1)
#print("--------------------")
print(dfIDMeanMax.idxmax())
print("--------------------")
print(dfIDMean.loc[dfIDMeanMax.idxmax()].idxmax())
print("--------------------")
print(int(dfIDMean.loc[dfIDMeanMax.idxmax()].
          idxmax())*
      int(dfIDMeanMax.idxmax()))
