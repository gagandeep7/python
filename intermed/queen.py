# board=[[0,0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0,0]]
# n=8

# def PrintBoard():
#     for i in range(n):
#         for j in range (n):
#             print(board[i][j],end='')
#         print()


# def CanQueenSafe(board,row,col):
#     for i in range(col):
#         if board[row][i]=='q':
#             return False
#     for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
#         if board[i][j]=='q':
#             return False
#     for i,j in zip(range(row,n,1),range(col,-1,-1)):
#         if board[i][j]=='q':
#             return False

#     return True






        


# def SolveQueen(board,col):
#     if col>=n:
#         return True
#     for i in range(n):
#         if CanQueenSafe(board,i,col):
#             board[i][col]='q'
#             if SolveQueen(board,col+1)==True:
#                 return True

#             board[i][col]=0


#     return False




# result=SolveQueen(board,1)
# if result==False:
#     print('Solution doesnot exist')
# else:
#     PrintBoard()
nums=10
count=0
i=0
gag=[]
end=(nums/2)
while count<end:
  if i==0:
    gag.append(i)
    gag.append(i+1)
    i=i+3
  else:
    gag.append(i)
    gag.append(i+1)
    i=i+4  
  count+=1
print(gag)