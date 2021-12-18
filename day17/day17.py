f=open("day17.txt","r")

line=f.readline().rstrip()
line=line.split(", y=")
yMin,yMax=map(int,line[1].split(".."))
xMin,xMax=map(int,line[0].split("x=")[1].split(".."))

count=0
highest=0
for xV in range(0,xMax+1):
    curX=xV
    xLoc=0
    times=[]
    time=0
    while curX>0:
        time+=1
        xLoc+=curX
        curX-=1
        if xLoc>=xMin and xLoc<=xMax:
            times.append(time)
            if curX==0:
                times=times+list(range(time+1,yMin*-2+1))
    for yV in range(yMin,abs(yMin)):
        for t in times: # I'm not sure if using the times variable narrows the search beyond a naive implementation
            yLoc=(yV+.5)*t-t**2/2
            if yLoc>=yMin and yLoc<=yMax:
                count+=1
                yHigh=int(yV*(yV+1)/2)
                if yHigh>highest:
                    highest=yHigh
                break
print(highest)
print(count)
f.close()