import random,string
def generator():
    j=0
    gen_list=[]
    print("enter five words name")
    vowels='aeiou'
    consonant='bcdfghjklmnpqrstvwxyz'
    while(j<5):#loop for every different character
        i=input("enter v for vowels ,c for consonat and other alphabet directly ")
        if(i.lower()=='v'):
            gen_list.append(random.choice(vowels))
        elif(i.lower() == 'c'):
            gen_list.append(random.choice(consonant))
        else:
            gen_list.append(i)
        j=j+1
    print(gen_list)
    strr= "".join(gen_list)#convert list to string and removed commas
    print(strr)

(generator())#function callloing and printing