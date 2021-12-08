f=open("day6.txt","r")

LIFE_CYCLE=7
SIM_TIME=256

inputLine=f.readline().rstrip().split(",")
allFish={}
for i in range(LIFE_CYCLE + 2):
    allFish[i]=len(list(filter(lambda x: int(x)==i,inputLine)))
print(allFish)

for j in range(SIM_TIME):
    prevZeros=allFish[0]
    for i in range(LIFE_CYCLE + 1):
        allFish[i]=allFish[i+1]
    allFish[LIFE_CYCLE - 1]+=prevZeros
    allFish[LIFE_CYCLE + 1]=prevZeros

print(sum(allFish.values()))
f.close()