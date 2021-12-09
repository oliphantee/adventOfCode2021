from collections import deque

f=open("day9.txt","r")

allLocs=[]
for line in f.readlines():
    allLocs.append(list(line.rstrip()))

allLocs=[list(map(int,i)) for i in allLocs]

def getNeighbors(i,j,allLocs):
    retList=[]
    if i==0:
        retList.append(allLocs[1][j])
    elif i==len(allLocs)-1:
        retList.append(allLocs[-2][j])
    else:
        retList.append(allLocs[i+1][j])
        retList.append(allLocs[i-1][j])
    if j==0:
        retList.append(allLocs[i][1])
    elif j==len(allLocs[0])-1:
        retList.append(allLocs[i][-2])
    else:
        retList.append(allLocs[i][j-1])
        retList.append(allLocs[i][j+1])
    return retList

allSinks=[]
riskSum=0
for i in range(len(allLocs)):
    for j in range(len(allLocs[0])):
        if min(getNeighbors(i,j,allLocs))>allLocs[i][j]:
            riskSum+=1+allLocs[i][j]
            allSinks.append((i,j))
print(riskSum)

def getBasinSize(i,j,allLocs):
    size=0
    unUsed=deque()
    unUsed.append((i,j))
    used=set()
    while len(unUsed)!=0:
        cur=unUsed.pop()
        i=cur[0]
        j=cur[1]
        if i>=0 and i<len(allLocs) and j>=0 and j<len(allLocs[0]) and allLocs[i][j]!=9 and cur not in used:
            size+=1
            unUsed.append((i+1,j))
            unUsed.append((i-1,j))
            unUsed.append((i,j+1))
            unUsed.append((i,j-1))
        used.add(cur)
    print(size)
    return size

allSizes=[]
for sink in allSinks:
    allSizes.append(getBasinSize(sink[0],sink[1],allLocs))

allSizes.sort()

print(allSizes[-1]*allSizes[-2]*allSizes[-3])
f.close()