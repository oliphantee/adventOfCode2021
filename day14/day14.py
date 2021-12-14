f=open("day14.txt","r")

seq=f.readline().rstrip()
f.readline()
allPairs={}
first=seq[0]
last=seq[-1]
for i in range(len(seq)-1):
    if seq[i:i+2] in allPairs:
        allPairs[seq[i:i+2]]+=1
    else:
        allPairs[seq[i:i+2]]=1

rules={}
for line in f.readlines():
    line=line.rstrip().split(" -> ")
    rules[line[0]]=line[1]

def pairInsertion(allPairs):
    global rules
    newAllPairs={}
    for pair in allPairs:
        if pair in rules:
            count=allPairs[pair]
            newPair1=pair[0]+rules[pair]
            newPair2=rules[pair]+pair[1]
            if newPair1 in newAllPairs:
                newAllPairs[newPair1]+=count
            else:
                newAllPairs[newPair1]=count
            if newPair2 in newAllPairs:
                newAllPairs[newPair2]+=count
            else:
                newAllPairs[newPair2]=count
        else:
            if pair in newAllPairs:
                newAllPairs[pair]+=allPairs[pair]
            else:
                newAllPairs[pair]=allPairs[pair]
    return newAllPairs

def getLetterDiff(allPairs):
    global first
    global last
    letterDict={}
    for pair in allPairs:
        if pair[0] in letterDict:
            letterDict[pair[0]] += allPairs[pair]
        else:
            letterDict[pair[0]] = allPairs[pair]
        if pair[1] in letterDict:
            letterDict[pair[1]] += allPairs[pair]
        else:
            letterDict[pair[1]] = allPairs[pair]
    for letter in letterDict:
        if letter==first or letter==last:
            letterDict[letter]=(letterDict[letter]+1)/2
        else:
            letterDict[letter]/=2
    print(max(letterDict.values()) - min(letterDict.values()))

for t in range(10):
    allPairs=pairInsertion(allPairs)

getLetterDiff(allPairs) # part 1

for t in range(30):
    allPairs=pairInsertion(allPairs)

getLetterDiff(allPairs) # part 2
f.close()