import random


cube=int(input("enter"))
start=0
stops=cube

for i in range(20):
    guess=random.randrange(start,stops)
    print("random guess",guess)
    ans=guess**3
    if ans==cube:
        print("cube root is",guess)
        break
    elif ans>cube:
        print("true")
        stops=guess     
    else:
        start=guess

        
    print(start,stops)
# 	root=ans**3
# 	ans=ans+1
# 	count=count+1
# 	if root==cube:
# 		print(f"cube of {cube} is {ans-1}")
# 		break
# print(count)