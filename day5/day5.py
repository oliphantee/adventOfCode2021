f = open("day5.txt","r")

used={}
for line in f.readlines():
    line=line.rstrip().split(" -> ")
    prev=line[0].split(",")
    fin=line[1].split(",")
    if prev[0]==fin[0]:
        lower=min([int(prev[1]),int(fin[1])])
        higher=max([int(prev[1]),int(fin[1])])
        for i in range(lower,higher+1):
            if prev[0]+","+str(i) in used:
                used[prev[0] + "," + str(i)]+=1
            else:
                used[prev[0]+","+str(i)]=1
    elif prev[1]==fin[1]:
        lower=min([int(prev[0]),int(fin[0])])
        higher=max([int(prev[0]),int(fin[0])])
        for i in range(lower,higher+1):
            if str(i) + "," + prev[1] in used:
                used[str(i) + "," + prev[1]]+=1
            else:
                used[str(i) + "," + prev[1]]=1
    elif int(prev[1])-int(fin[1])==int(prev[0])-int(fin[0]):
        tmp=prev
        if not int(prev[0])<int(fin[0]):
            prev=fin
            fin=tmp
        for i in range(0,int(fin[0])-int(prev[0])+1):
            if str(i+int(prev[0])) + "," + str(i+int(prev[1])) in used:
                used[str(i+int(prev[0])) + "," + str(i+int(prev[1]))]+=1
            else:
                used[str(i + int(prev[0])) + "," + str(i + int(prev[1]))] = 1
    else:
        tmp = prev
        if not int(prev[0]) < int(fin[0]):
            prev = fin
            fin = tmp
        for i in range(0, int(fin[0]) - int(prev[0])+1):
            if str(i+int(prev[0])) + "," + str(int(prev[1])-i) in used:
                used[str(i+int(prev[0])) + "," + str(int(prev[1])-i)]+=1
            else:
                used[str(i + int(prev[0])) + "," + str(int(prev[1])-i)] = 1

# for i in range(10):
#     for j in range(10):
#         if str(j)+","+str(i) in used:
#             print(used[str(j)+","+str(i)],end="")
#         else:
#             print("0",end="")
#     print("")

print(len(list(filter(lambda x: used[x]!=1,used))))
f.close()