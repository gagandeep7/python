nums=[20,40,10,50,70,30]
sorts=sorted(nums)
def bub(arr):
    n=1

    for  j in range (0,len(arr)-n):# it is iteration for for list sorting
        
        print(" pass",j+1)
        
        for i in range (0,len(arr)-1):# it is iteration for comparison
            
            
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                print(arr)
    n=n+1            
    return arr
print(bub(nums))


# without using nested loops
def sort(arr):
    while True:# loop while continue until it is true 
        corrected=False
        for i in range (0,len(arr)-1):# it is iteration for comparison
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                corrected=True
        print(arr)        
        if not corrected:# it will check value of corrected and execute when coreected = false
            break
            

            
(bub(nums))















