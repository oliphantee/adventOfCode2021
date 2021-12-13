import math as mt

f=open("day13.txt")

def fold(allDots,xy,pos):
    pos=int(pos)
    toRemove=[]
    toAdd=[]
    for loc in allDots:
        if xy=="x" and loc[0]<pos:
            toRemove.append(loc)
            toAdd.append((2*pos-loc[0],loc[1]))
        if xy=="y" and loc[1]<pos:
            toRemove.append(loc)
            toAdd.append((loc[0],2*pos-loc[1]))
    for loc in toAdd:
        allDots.add(loc)
    for loc in toRemove:
        allDots.remove(loc)
    return allDots

allDots=set()
xShift=0
yShift=0
for line in f.readlines():
    if "," in line:
        loc=line.rstrip().split(",")
        allDots.add((int(loc[0]),int(loc[1])))
    elif "fold" in line:
        cmd=line.rstrip().split()[-1]
        cmd=cmd.split("=")
        if cmd[0]=="x":
            val=int(cmd[1])+xShift
        else:
            val=int(cmd[1])+yShift
        allDots=fold(allDots,cmd[0],val)
        if cmd[0]=="x":
            xShift+=int(cmd[1])+1
        else:
            yShift+=int(cmd[1])+1
        print(len(allDots)) # part 1

minX=mt.inf
minY=mt.inf
maxX=0
maxY=0
for loc in allDots:
    if loc[0]>maxX:
        maxX=loc[0]
    if loc[0]<minX:
        minX=loc[0]
    if loc[1]>maxY:
        maxY=loc[1]
    if loc[1]<minY:
        minY=loc[1]

for j in range(maxY, minY-1,-1):
    for i in range(maxX,minX-1,-1):
        if (i,j) in allDots:
            print("#",end="")
        else:
            print(".",end="")
    print()

f.close()