import copy as cp

f=open("day18.txt","r")

class BinaryNode:
    def __init__(self):
        self.left=None
        self.right=None
        self.parent=None
        self.isLeaf=False
        self.val=None

    def reduce(self):
        while True:
            exploded=self.explode()
            if not exploded:
                if not self.split():
                    return

    def getMagnitude(self):
        if self.isLeaf:
            return self.val
        else:
            return self.left.getMagnitude()*3+self.right.getMagnitude()*2

    def explode(self,count=0):
        if self.isLeaf:
            return False
        if self.left.isLeaf and self.right.isLeaf:
            if count>=4:
                leftVal=self.left.val
                rightVal=self.right.val
                self.left=None
                self.right=None
                self.isLeaf=True
                self.val=0
                successor=self.getSuccessor()
                if successor!=None:
                    successor.val+=rightVal
                predecessor=self.getPredecessor()
                if predecessor!=None:
                    predecessor.val+=leftVal
                return True
            else:
                return False
        else:
            if self.left.explode(count+1):
                return True
            else:
                return self.right.explode(count+1)

    def split(self):
        if self.isLeaf==False:
            if self.left.split():
                return True
            else:
                return self.right.split()
        else:
            if self.val>=10:
                self.isLeaf=False
                self.left=BinaryNode()
                self.right=BinaryNode()
                self.left.parent=self
                self.right.parent=self
                self.left.isLeaf=True
                self.right.isLeaf=True
                self.left.val=self.val//2
                self.right.val=(self.val+1)//2
                return True
            return False

    def getPredecessor(self):
        prevNode=self
        node=self.parent
        while prevNode==node.left:
            prevNode=node
            node=node.parent
            if node==None:
                return None
        node=node.left
        while node.isLeaf==False:
            node=node.right
        return node

    def getSuccessor(self):
        prevNode=self
        node=self.parent
        while prevNode==node.right:
            prevNode=node
            node=node.parent
            if node==None:
                return None
        node=node.right
        while node.isLeaf==False:
            node=node.left
        return node

    def __repr__(self): # for debugging purposes
        if self.isLeaf:
            return str(self.val)
        return "["+str(self.left)+","+str(self.right)+"]"

def makeSnailNum(line):
    root=BinaryNode()
    curNode=root
    for i in range(len(line)):
        if line[i]=="[":
            left=BinaryNode()
            curNode.left=left
            left.parent=curNode
            curNode=left
        elif line[i]=="]":
            curNode=curNode.parent
        elif line[i].isdigit():
            curNode.val=int(line[i])
            curNode.isLeaf=True
            curNode=curNode.parent
        elif line[i]==",":
            right=BinaryNode()
            curNode.right=right
            right.parent=curNode
            curNode=right
    return root

curSum=None
prevLine=None
maxSum=0
allSn=[]
for line in f.readlines():
    curSn=makeSnailNum(line.rstrip())
    curSn.reduce()
    allSn.append(cp.deepcopy(curSn))
    if curSum!=None:
        newNode=BinaryNode()
        newNode.left=curSum
        newNode.right=curSn
        curSum.parent=newNode
        curSn.parent=newNode
        newNode.reduce()
        curSum=newNode
    else:
        curSum=curSn

print(curSum.getMagnitude()) # part 1

for i in range(len(allSn)):
    for j in range(len(allSn)):
        if i!=j:
            sN1=cp.deepcopy(allSn[i])
            sN2=cp.deepcopy(allSn[j])
            newNode = BinaryNode()
            newNode.left = sN1
            newNode.right = sN2
            sN1.parent = newNode
            sN2.parent = newNode
            newNode.reduce()
            if newNode.getMagnitude()>maxSum:
                maxSum=newNode.getMagnitude()

print(maxSum) # part 2
f.close()