import math as mt
import numpy as np

f=open("day4.txt","r")

order=list(map(int,f.readline().split(",")))

def checkRowWin(boolBoard,j):
    for k in range(len(boolBoard)):
        if boolBoard[k][j] != 1:
            return False
    return True

def checkColWin(boolBoard,i):
    for k in range(len(boolBoard)):
        if boolBoard[i][k] != 1:
            return False
    return True

def checkWin(boolBoard,i,j):
    if checkRowWin(boolBoard,j) or checkColWin(boolBoard,i):
        return True
    return False

def getScore(curBoard,boolBoard,n):
    curSum=0
    for i in range(len(curBoard)):
        for j in range(len(curBoard[0])):
            if boolBoard[i][j]==0:
                curSum+=curBoard[i][j]
    return curSum*n

def scoreBoard(curBoard):
    boolBoard=np.zeros((len(curBoard),len(curBoard[0])))
    for k in range(len(order)):
        for i in range(len(boolBoard)):
            for j in range(len(boolBoard[0])):
                if curBoard[i][j]==order[k]:
                    boolBoard[i][j]=1
                    if checkWin(boolBoard,i,j):
                        return k,getScore(curBoard,boolBoard,order[k])
    return mt.inf,getScore(curBoard,boolBoard,order[k])

curBoard=[]
bestTimeFin=0
bestScore=0
for line in f.readlines():
    if len(line)<2 and len(curBoard)>0:
        timeFin,score=scoreBoard(curBoard)
        curBoard=[]
        if timeFin>=bestTimeFin:
            bestTimeFin=timeFin
            bestScore=score
    elif len(line)>1:
        curBoard.append(list(map(int,line.rstrip().split())))

print(bestTimeFin,bestScore)
f.close()