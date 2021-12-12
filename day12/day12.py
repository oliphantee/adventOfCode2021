f=open("day12.txt","r")

allVertices={} # this is a rudimentary way of storing the nodes akin to OOP, would be cleaner to have a Node class
for line in f.readlines():
    line=line.rstrip().split("-")
    firstV=line[0]
    secondV=line[1]
    if firstV in allVertices:
        allVertices[firstV][0]+=[secondV]
    else:
        allVertices[firstV]=[[secondV],False]
    if secondV in allVertices:
        allVertices[secondV][0]+=[firstV]
    else:
        allVertices[secondV]=[[firstV],False]

count=0
def dfsRecursive(curNode,doubled,curAnswer): # a modified depth first search
    global count
    curAnswer+=curNode+","
    if curNode=="end":
        #print(curAnswer)
        count+=1
        return
    if curNode.lower()==curNode:
        allVertices[curNode][1]+=1
        if allVertices[curNode][1]==2:
            doubled=True
    for otherV in allVertices[curNode][0]:
        if allVertices[otherV][1]==0:
            dfsRecursive(otherV,doubled,curAnswer)
        elif doubled==False and allVertices[otherV][1]==1 and otherV!="start" and otherV!="end":
            dfsRecursive(otherV,doubled,curAnswer)
    if curNode.lower()==curNode:
        allVertices[curNode][1]-=1

dfsRecursive("start",True,"")
print(count) # part 1
count=0
dfsRecursive("start",False,"")
print(count) # part 2

f.close()