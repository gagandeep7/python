def fact(num):
    if num==1 or num==0:# since factorial opf o and 1 is 1
        return 1
    else:
        return num*fact(num-1) # for eg factorial of 4= 4*3*2*1 it is equal to 4*fact of 3=  4*(3*2*1)
def facts(start,stop,steps=None):
    for i in range(start,stop,steps):
        print("factorial of", i, "is", fact(i))

