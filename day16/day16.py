f=open("day16.txt","r")

line=f.readline().rstrip()

number=format(int(line,16),'b')
while len(number)%4!=0:
    number='0'+number

versionSum=0
def getPacket(string):
    global versionSum
    v=int(string[0:3],2)
    versionSum+=v
    tid=int(string[3:6],2)
    if tid==4:
        i=6
        valString=""
        while string[i]=='1':
            valString+=string[i+1:i+5]
            i+=5
        valString+=string[i+1:i+5]
        val=int(valString,2)
        return val,string[i+5:]
    else:
        ltid=string[6]
        if ltid=="0":
            totLen=int(string[7:22],2)
            start=22
            vals = []
            subString = string[start:start + totLen]
            while subString != "":
                val, subString = getPacket(subString)
                vals.append(val)
            rest=string[start+totLen:]
        else:
            totLen=int(string[7:18],2)
            rest=string[18:]
            vals=[]
            for i in range(totLen):
                val, rest = getPacket(rest)
                vals.append(val)
        if tid==0:
            return sum(vals),rest
        elif tid==1:
            prod=1
            for c in vals:
                prod*=c
            return prod,rest
        elif tid==2:
            return min(vals),rest
        elif tid==3:
            return max(vals),rest
        elif tid==5:
            return vals[0]>vals[1],rest
        elif tid==6:
            return vals[0]<vals[1],rest
        elif tid==7:
            return vals[0]==vals[1],rest
        return vals,rest

print(getPacket(number)) # part 2 is the first number
print(versionSum) # part 1 is this number

f.close()