import math as mt

f=open("day1.txt","r")
curCount=0
prevVal=[mt.inf,mt.inf,mt.inf]
for i,line in enumerate(f.readlines()):
    if int(line)>prevVal[i%3]:
        curCount+=1
    prevVal[i%3]=int(line)
print(curCount)

f.close()