from collections import deque

f=open("day10.txt","r")

fScore=0
allScores=[]
for line in f.readlines():
    score=0
    curStk=deque()
    fail=False
    for c in line.rstrip():
        if c in "({[<":
            curStk.append(c)
        else:
            openC=curStk.pop()
            if (openC=="(" and c!=")") or (openC=="[" and c!="]") or (openC=="{" and c!="}") or (openC=="<" and c!=">"):
                fail=True
                break
    if fail:
        if c==")":
            fScore+=3
        elif c=="]":
            fScore+=57
        elif c=="}":
            fScore+=1197
        elif c==">":
            fScore+=25137
    else:
        print(curStk)
        while len(curStk)!=0:
            c=curStk.pop()
            score*=5
            if c=="(":
                score+=1
            elif c=="[":
                score+=2
            elif c=="{":
                score+=3
            elif c=="<":
                score+=4
        allScores.append(score)

allScores.sort()
print(fScore) # part 1
print(allScores[len(allScores)//2]) # part 2

f.close()