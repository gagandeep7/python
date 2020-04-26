loop =4
while loop==4:
    if loop==4:
        print(" welcome to gagland\n you have to play with my rules" )
        print("you can use up down left and right to navigate \n you can input quit to end game")
        second=input("what is your choice")
        if second.lower()=='up':
            print("there is sea ")
            loop=5
        elif second.lower()=='down':
            print("there is forest")
            loop=6
        elif second.lower()=='left':
            print("there is city")
            loop=7
        elif second.lower()=='right':
            print("there is desert")
            loop=8
        elif second.lower()=='quit':
            break
        else:
            print("wrong choice")

    