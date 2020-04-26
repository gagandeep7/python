def div(num):

    try:
        return 42/num
    except ZeroDivisionError:

        print('error divided by zero')
    except   TypeError:
        
        print('error use integer  not string') 
div('w')
div(0)       
print(div(int('7')))
print(int('8'))  
num=input()
try:
    print(type(num))
    if int(num) > 10:
        print("good")
    else:
        print('bad')    

except ValueError:# it cant convert int('six') to 6
    print('did not enter a number')
