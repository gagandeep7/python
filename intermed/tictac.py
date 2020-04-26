game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
gags=[]
def game_map():
    for i,j in enumerate(game):
        if i==0:
            print("   0  1  2")
        print(i,j)
def choice1():
    try:
        inputs = (input("pl1 enter row col"))
        if inputs in gags:
            while True:
                 print('error')
                 inputs = (input("pl1 enter row col"))
                 if inputs not in gags:
                    break

        gags.append(inputs)
        print(gags)
        i=int(inputs[0]);j=int(inputs[1]);
        game[i][j]='X'
        game_map()
    except IndexError:
        print('wrong choice')

def choice2():
    try:
        inputs=(input("pl2 enter row col"))
        if inputs in gags:
            while True:
                 print('error')
                 inputs = (input("pl2 enter row col"))
                 if inputs not in gags:
                    break
        gags.append(inputs)
        print(gags)
        i=int(inputs[0]);j=int(inputs[1]);
        game[i][j]='O'
        game_map()

    except IndexError:
        print('wrong choice')

def horwin():
    for i in game:
         print(i)
         if (i.count('X'))==len(i):
             print ("pl1")
         elif (i.count('O'))==len(i):
             print("pl2")
         else:
             return 'tie'
# /while True:
i=0
for i in range(0,5):
    if i<=3:
        gag=choice1()
        choice2()
    else:
        gag = choice1()
        if horwin() == 'tie':
            if verwin()=='tie':
                if diagwin()=='tie':
                    print("tie")
                else:
                    diagwin()
            else:
                verwin()
        else:
            horwin()
    # if horwin() == 'pl1' or horwin() == 'pl2' or horwin() == 'tie':
    #     break