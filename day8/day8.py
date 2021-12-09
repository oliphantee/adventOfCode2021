f = open("day8.txt","r")

def sortString(str): # from https://www.geeksforgeeks.org/python-ways-to-sort-letters-of-string-alphabetically/
    return ''.join(sorted(str))

def getExcludedChars(someStr):
    chars=[]
    for c in "abcdefg":
        if c not in someStr:
            chars.append(c)
    if len(chars)==1:
        return chars[0]
    return chars

count=0
for line in f.readlines():
    line=line.rstrip().split(" | ")
    fullLine=(line[0]+" "+line[1]).split()
    codes=[None for i in range(10)]
    codesLeft=[]
    for code in fullLine:
        if len(code)==2:
            codes[1]=sortString(code)
        elif len(code)==4:
            codes[4]=sortString(code)
        elif len(code)==3:
            codes[7]=sortString(code)
        elif len(code)==7:
            codes[8]=sortString(code)
        else:
            codesLeft.append(sortString(code))
    for code in codesLeft:
        if len(code)==6:
            exclChar=getExcludedChars(code)
            if exclChar in codes[1] or exclChar in codes[7]:
                codes[6]=code
            elif not (exclChar in codes[4]):
                codes[9]=code
            elif exclChar in codes[4] and (codes[1]!=None and (not (exclChar in codes[1])) or (codes[7]!=None and not (exclChar in codes[7]))):
                codes[0]=code
        else:
            exclChars=getExcludedChars(code)
            if (exclChars[0] in codes[1] or exclChars[1] in codes[1]) and exclChars[0] in codes[4] and exclChars[1] in codes[4]:
                codes[2] = code
            elif exclChars[0] in codes[1] or exclChars[1] in codes[1]:
                codes[5]=code
            elif exclChars[0] not in codes[1] and exclChars[1] not in codes[1]:
                codes[3]=code
    val=""
    for code in line[1].split():
        val+=str(codes.index(sortString(code)))
    count+=int(val)

print(count)
f.close()