x=input()
xlist=x.split(" ")
print(xlist)
first=xlist[1]# file to be copied
second=xlist[2]#copy of file
if(xlist[0]=="cp"):
    with open(f"{first}",'r')as rf:
        with open(f"{second}", 'w')as wf:
            gag7=rf.read()
            for line in gag7:#copy lines
                print(line)
                wf.write(line)

if xlist[0]=="mv":#rename file name

        with open(f"{first}", 'r')as rf:
            with open(f"{second}", 'w')as wf:
                gag7 = rf.read()
                for line in gag7:  # copy lines
                    wf.write(line)
        with open(f"{first}", 'w')as rf:
            rf.truncate()

