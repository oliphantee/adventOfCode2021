f=open("day19test.txt")

class Scanner:
    def __init__(self,id):
        self.allLocs=[]
        self.id=id

    def rotate(self):
        for i in range(len(self.allLocs)):
            x,y,z=self.allLocs[i]
            self.allLocs[i]=[y,z,x]

    def flip(self,axis=0):
        if axis==0: # x flip
            for i in range(len(self.allLocs)):
                x,y,z=self.allLocs[i]
                self.allLocs[i]=[-x,y,z]
        elif axis==1: # y flip
            for i in range(len(self.allLocs)):
                x,y,z=self.allLocs[i]
                self.allLocs[i]=[x,-y,z]
        elif axis==2: # z flip
            for i in range(len(self.allLocs)):
                x, y, z = self.allLocs[i]
                self.allLocs[i] = [x, y, -z]

    def shift(self,delX,delY,delZ):
        for i in range(len(self.allLocs)):
            x,y,z=self.allLocs[i]
            self.allLocs[i]=[x+delX,y+delY,z+delZ]

    def merge(self,other,delta):
        delX=delta[0]
        delY=delta[1]
        delZ=delta[2]
        print(delta)
        other.shift(delX,delY,delZ)
        for loc in other.allLocs:
            if loc not in self.allLocs:
                self.allLocs.append(loc)
            # else:
            #     print(loc)

    def overlap(self,other):
        print(other.allLocs)
        for flipVal in range(8):
            if flipVal%4==0:
                other.flip(0)
            if flipVal%2==0:
                other.flip(1)
            other.flip(2)
            for rot in range(3):
                allDeltas={}
                for i in range(len(self.allLocs)):
                    x,y,z=self.allLocs[i]
                    for j in range(len(other.allLocs)):
                        a,b,c=other.allLocs[j]
                        if (x-a,y-b,z-c) in allDeltas:
                            allDeltas[(x-a,y-b,z-c)]+=1
                        else:
                            allDeltas[(x-a,y-b,z-c)]=1
                #print(max(allDeltas.values()))
                if max(allDeltas.values())>=12:
                    for key in allDeltas.keys():
                        if allDeltas[key]>=12:
                            delta=key
                    self.merge(other,delta)
                    return True
                other.rotate()
        return False
id=0
scanners=[]
for line in f.readlines():
    if "--" in line:
        scanners.append(Scanner(id))
        id+=1
    elif line!="\n":
        scanners[-1].allLocs.append(list(map(int,line.rstrip().split(","))))

i=1
scanners[0].shift(-1105,1205,-1229)
while len(scanners)>1:
    #print(len(scanners),i)
    if scanners[0].overlap(scanners[i]):
        print("merged",scanners[0].id,scanners[i].id,len(scanners[0].allLocs),len(scanners[-1].allLocs))
        scanners.pop(i)
        i=1
    else:
        i=i%(len(scanners)-1)+1

f.close()