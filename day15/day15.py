f=open("day15.txt")
import math as mt
from queue import Queue

def getNeighbors(i,j,allLocs):
    retList=[]
    if i==0:
        retList.append([1,j])
    elif i==len(allLocs)-1:
        retList.append([len(allLocs)-2,j])
    else:
        retList.append([i+1,j])
        retList.append([i-1,j])
    if j==0:
        retList.append([i,1])
    elif j==len(allLocs[0])-1:
        retList.append([i,len(allLocs[0])-2])
    else:
        retList.append([i,j-1])
        retList.append([i,j+1])
    return retList

allCells = []
costs = []
nLines=0
for line in f.readlines():
    line=line.rstrip()
    allCells.append([int(i) for i in line])
    for i in range(1,5):
        allCells[-1]=allCells[-1]+[(int(line[j])+i-1)%9+1 for j in range(len(line))]
    costs.append([mt.inf for _ in range(len(line)*5)])
    nLines+=1

for i in range(1,5):
    for j in range(nLines):
        allCells.append([(int(allCells[j][k])+i-1)%9+1 for k in range(len(line)*5)])
        costs.append([mt.inf for _ in range(len(line)*5)])

costs[0][0]=0
costQueue=Queue()
costQueue.put([0,0])

while not costQueue.empty():
    loc=costQueue.get()
    for n in getNeighbors(loc[0],loc[1],costs):
        if costs[loc[0]][loc[1]]+allCells[n[0]][n[1]]<costs[n[0]][n[1]]:
            costs[n[0]][n[1]]=costs[loc[0]][loc[1]]+allCells[n[0]][n[1]]
            costQueue.put(n)

print(costs[nLines-1][nLines-1])
print(costs[-1][-1])

f.close()