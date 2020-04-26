import random
x= random.randint(1,20)

for i in range(0,5):
    y=int(input("enter guess"))
    if y ==x:
        print("right guess")
    else:
   
        print("try again")  

print(f"no was{x} ")          