lis={6,5,9,1,8,2}
list2={'missing element are :'}
mins=min(lis)
maxs=max(lis)
for i in range(mins,maxs+1):
	list2.add((i))
list2=set(list2)
miss=list2.difference(lis)
print(miss)