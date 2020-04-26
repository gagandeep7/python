x=input()
xlist=x.split(" ")
print(xlist)
first=xlist[1]# file to be copied
second=xlist[2]#copy of file
with open(f"{first}",'r')as rf:
    with open(f"{second}", 'w')as wf:
        gag7=rf.read()
        for line in gag7:#copy lines
            wf.write(line)


