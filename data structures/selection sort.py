lis=[9,2,5,3,8,1]

for i in range(0,len(lis)-1):
    index=lis.index(min(lis[i:]))
    (lis[i],lis[index])=(lis[index],lis[i])
    print(lis)
