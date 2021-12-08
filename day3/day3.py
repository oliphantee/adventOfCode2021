import numpy as np
import copy as cp

f=open("day3.txt","r")
mostCommon=np.zeros((12))
allVals=[]
for line in f.readlines():
    line=line.strip()
    allVals.append(line)
    for i,char in enumerate(line):
        if char=="0":
            mostCommon[i]+=1
        else:
            mostCommon[i]-=1

gamma=0
epsilon=0
for i in range(1,len(mostCommon)+1):
    if mostCommon[-i]<0:
        gamma+=2**(i-1)
    else:
        epsilon+=2**(i-1)
print(gamma*epsilon)

posVals=cp.deepcopy(allVals)
o2=0
for c in range(12):
    ones=[]
    zeros=[]
    for posVal in posVals:
        if posVal[c]=="1":
            ones.append(posVal)
        else:
            zeros.append(posVal)
    if len(ones)>=len(zeros):
        posVals=ones
    else:
        posVals=zeros
    if len(posVals)==1:
        print(posVals)
        o2=int(posVals[0],2)
        break

co2=0
for c in range(12):
    ones=[]
    zeros=[]
    for posVal in allVals:
        if posVal[c]=="1":
            ones.append(posVal)
        else:
            zeros.append(posVal)
    if len(ones)<len(zeros):
        allVals=ones
    else:
        allVals=zeros
    if len(allVals)==1:
        print(allVals)
        co2=int(allVals[0],2)
        break

print(co2,o2,co2*o2)