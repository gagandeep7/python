def mobile(num):
    if len(num) !=12:
        return False
    for i in num(0,3):
        if not num[i].isdecimal():
            return False
    if num[3] != '-':
        return False        
print(mobile('988-092-8889'))        ``