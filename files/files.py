with open('gag1.txt','r')as rf:
    gag=rf.read()
    #gag1=rf.readlines() used to read all lines and readline for individual line
    print(gag)
    for i in gag:
        print(i,end='')
    size=30
    while len(gag):
        print(gag,end='')
        gag=rf.read(size)
   # while len(gag)>0:
    #    print(gag,end='')
with open('gag1.txt','r')as rf:
    with open('country7.txt', 'w')as wf:
        gag7=rf.read()
        for line in gag7:#copy lines
            wf.write(line)
with open('gag2.txt','w') as wg:
            wg.write('test')
