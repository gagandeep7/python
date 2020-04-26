gag={'age':20,'name':['gag' ,'deep']}
print(gag['name'][1])
print(gag.get('name'[0],'errror'))
for i,j in gag.items():
	print(i,':',j)
nums = [0, 1, 2, 3, 4] 
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0} # dict comprehension
even_num_to_square2 = [ x ** 2 for x in nums if x % 2 == 0] # list comprehension
even_num_to_square3={x**2 for x in nums}#set comprehension
print(even_num_to_square,even_num_to_square2,even_num_to_square3)  # Prints "{0: 0, 2: 4, 4: 16}
print(even_num_to_square3)
