f=open("day7.txt","r")

allVals=list(map(int,f.readline().rstrip().split(",")))
valDict={}
for val in allVals:
    if val in valDict:
        valDict[val]=[valDict[val][0]+1,valDict[val][1]+1]
    else:
        valDict[val]=[1,1]

cost=0
while len(valDict)>1:
    minVal=min(valDict)
    maxVal=max(valDict)
    if valDict[minVal][1]>valDict[maxVal][1]:
        totMoved=valDict[maxVal][0]
        prevWeight=valDict[maxVal][1]
        valDict.pop(maxVal)
        newMax=maxVal-1
        cost+=prevWeight
        if newMax in valDict:
            valDict[newMax]=[valDict[newMax][0]+totMoved,prevWeight+totMoved+valDict[newMax][1]]
        else:
            valDict[newMax]=[totMoved,prevWeight+totMoved]
    else:
        totMoved = valDict[minVal][0]
        prevWeight = valDict[minVal][1]
        valDict.pop(minVal)
        newMin=minVal+1
        cost+=prevWeight
        if newMin in valDict:
            valDict[newMin]=[valDict[newMin][0]+totMoved,prevWeight+totMoved+valDict[newMin][1]]
        else:
            valDict[newMin]=[totMoved,prevWeight+totMoved]

print(valDict)
print(cost)
f.close()