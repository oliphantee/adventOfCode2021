f=open("day11.txt","r")

tMax=100
flashCount=0

def getNeighbors(i,j,matrix): # note that for this problem, it is fine that a location is a neighbor of itself
    lowI=i-1
    highI=i+1
    lowJ=j-1
    highJ=j+1
    if i==0:
        lowI=0
    elif highI==len(matrix):
        highI=i
    if j==0:
        lowJ=0
    elif highJ==len(matrix[0]):
        highJ=j
    retList=[]
    for k in range(lowI,highI+1):
        for l in range(lowJ,highJ+1):
            retList+=[(k,l)]
    return retList

def flash(i,j,matrix):
    global flashCount
    for loc in getNeighbors(i,j,matrix):
        matrix[loc[0]][loc[1]]+=1
        if matrix[loc[0]][loc[1]]==10:
            flash(loc[0],loc[1],matrix)
            flashCount+=1

def printMatrix(matrix):
    for row in matrix:
        print(row)
    print()

matrix=[]
for line in f.readlines():
    matrix.append([int(i) for i in line.rstrip()])

t=0
while True:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j]+=1
            if matrix[i][j]==10:
                flash(i,j,matrix)
                flashCount+=1
    allFlash=True
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]>=10:
                matrix[i][j]=0
            else:
                allFlash=False
    if t==tMax:
        print(flashCount, "part 1") # part 1
    if allFlash:
        print(t+1, "part 2") # part 2
        break
    t+=1

f.close()