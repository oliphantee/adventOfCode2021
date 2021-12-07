f=open("day2.txt")
curX=0
curY=0
aim=0
for line in f.readlines():
    line=line.split()
    if line[0]=="forward":
        curX+=int(line[1])
        curY+=int(line[1])*aim
    elif line[0]=="down":
        aim+=int(line[1])
    else:
        aim-=int(line[1])

print(curX,curY,curX*curY)