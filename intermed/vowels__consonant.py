s="gagandeep"
s=s.lower()
len=int(len(s))
count=0#to count vowels
cn=0#to count consonants
vowels=['a','e','i','o','u']# list of vowels
consonants='bcdfghjklmnpqrstvwxyz'
for i in range(0,len):
    print(s[i])
    if s[i] in vowels :
        count+=1
    else:
        cn+=1
print("no of vowels",count,"no of consonant",cn)
