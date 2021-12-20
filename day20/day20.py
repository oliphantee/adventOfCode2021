T_MAX=50

f=open("day20.txt","r")

def getVal(string):
    return int("".join(["1" if i=="#" else "0" for i in string]),2)

def printImage(image):
    for row in image:
        print(row)
    print()

def getNeighbors(image,i,j,t):
    neighbors=image[i-1][j-1:j+2]+image[i][j-1:j+2]+image[i+1][j-1:j+2]
    return neighbors

def getCount(image):
    count=0
    for row in image:
        for val in row:
            if val=="#":
                count+=1
    return count

enhance=f.readline().rstrip()
f.readline()

curImage=[]
for line in f.readlines():
    curImage.append(["." for _ in range(T_MAX+1)]+list(line.rstrip())+["." for _ in range(T_MAX+1)])

for _ in range(T_MAX+1):
    curImage=[["." for _ in range(len(line)+(T_MAX+1)*2)]]+curImage
    curImage.append(["." for _ in range(len(line)+(T_MAX+1)*2)])

for t in range(T_MAX):
    nextImage=[["." for _ in range(len(curImage[0]))] for _ in range(len(curImage))]
    if t%2==0:
        for i in range(len(nextImage)):
            if i==0 or len(nextImage)-1:
                for j in range(len(nextImage[0])):
                    nextImage[i][j]="#"
            else:
                nextImage[i][0]="#"
                nextImage[i][-1]="#"
    for i in range(1,len(curImage)-1):
        for j in range(1,len(curImage[0])-1):
            ninePixels=getNeighbors(curImage,i,j,t)
            nextImage[i][j]=enhance[getVal(ninePixels)]
    curImage=nextImage
    if t==1:
        print(getCount(curImage)) # part 1

print(getCount(curImage)) # part 2

f.close()