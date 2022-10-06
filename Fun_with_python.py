print("                                IT'S TIME TO PLAY                ")
print("1.Stone, Paper, Scissor")
print("2.Try Your Luck")
print("3.Ludo Dice")
print("4.Toss A Coin")
print("5.Tic Tac Toe")
choice=int(input("Select the game you want to play \n"))
if(choice==1):
    import matplotlib.pyplot as plt 
    con=[]    
    print("1.Stone, Paper, Scissor")
    print("GAME START")
    Z=input("Enter Player name \n")
    count=0
    n=int(input("Enter the number of time you want to play \n"))
    for i in range(n):
        print("Select the choice :-")
        print("1.Stone")
        print("2.Paper")
        print("3.Scissor")
        a=int(input("enter the choice \n"))
        import random
        if (a==1):
            c=random.randrange(5,7)
            if (c==5):
                print("computer choice Paper")
                print("You Loose")
            elif(c==6):
                print("computer choice Scissor")
                print("You Win")
                count=count+1
        elif (a==2):
            d=random.randrange(5,7)
            if (d==5):
                print("computer choice Scissor")
                print("You Loose")
            elif(d==6):
                print("computer choice Stone")
                print("You Win")
                count=count+1
        elif (a==3):
            e=random.randrange(5,7)
            if (e==5):
                print("computer choice Stone")
                print("You Loose")
            elif(e==6):
                print("computer choice Paper")
                print("You Win")
                count=count+1
        else:
            print("enter valid choice (number)")
    print(Z,"HAS SCORED :- \n",count,"out of",n)
    q=n-count
    con.append(count)
    con.append(q)
    Zones=["Correct","Wrong"]
    plt.axis("equal")
    plt.pie(con,labels=Zones,autopct="%1.2f%%")
    plt.show()                    #Result_will_display_using_piechart
elif(choice==2):
    import matplotlib.pyplot as plt 
    con=[]
    print("2.Try Your Luck")
    print("GAME START")
    n=int(input("enter the number of time you want to play"))
    print("NOTE:-predict only 0 or 1")
    count=0
    import random
    for i in range(n):
        c=random.randrange(0,2)
        a=int(input("enter your prediction"))
        if(c==a):
            print("You Win Jackpot")
            count=count+1
        else:
            print("dice fall on",c)
            print("Better Luck Next Time")
    print("you have give correct prediction",count,"times")
    q=n-count
    con.append(count)
    con.append(q)
    Zones=["Correct","Wrong"]
    plt.axis("equal")
    plt.pie(con,labels=Zones,autopct="%1.2f%%")
    plt.show()           #Result_will_display_using_piechart
elif(choice==3):
    print("3.Ludo Dice")
print("GAME START")
import random
while (1<2):
    c=random.randrange(1,7)
    print("\nDice Display",c)
    
    if(c==1):
        import turtle
        a=turtle.Turtle()
        a.screen.bgcolor("yellow")  
        a.penup()
        a.forward(50)
        a.pendown()
        a.begin_fill()
        a.fillcolor("white")
        a.left(90)
        a.forward(50)
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(50)
        a.end_fill()
        a.penup()
        a.home()
        x=0
        y=-5
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(8)
        a.end_fill()
        a.penup()
        a.hideturtle()
        
    elif(c==2):
        import turtle
        a=turtle.Turtle()
        a.screen.bgcolor("yellow")
        a.penup()
        a.forward(50)
        a.pendown()
        a.begin_fill()
        a.fillcolor("white")
        a.left(90)
        a.forward(50)
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(50)
        a.end_fill()
        a.penup()
        a.home()
        y=0
        x=-20
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(8)
        a.end_fill()
        a.penup()
        a.home()
        y=0
        x=20
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(8)
        a.end_fill()
        a.penup()
        a.hideturtle()

    elif (c==3):
        import turtle
        a=turtle.Turtle()
        a.screen.bgcolor("yellow")
        a.penup()
        a.forward(50)
        a.pendown()
        a.begin_fill()
        a.fillcolor("white")
        a.left(90)
        a.forward(50)
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(50)
        a.end_fill()
        a.penup()
        a.home()
        y=0
        x=-30
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(8)
        a.end_fill()
        a.penup()
        a.home()
        y=0
        x=0
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(8)
        a.end_fill()
        a.penup()
        a.home()
        y=0
        x=30
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(8)
        a.end_fill()
        a.penup()
        a.hideturtle()

    
    elif(c==4):
        import turtle
        a=turtle.Turtle()
        a.screen.bgcolor("yellow")
        a.penup()
        a.forward(50)
        a.pendown()
        a.begin_fill()
        a.fillcolor("white")
        a.left(90)
        a.forward(50)
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(50)
        a.end_fill()
        a.penup()
        a.home()
        y=10
        x=-30
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(8)
        a.end_fill()
        a.penup()
        a.home()
        y=-30
        x=30
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(8)
        a.end_fill()
        a.penup()
        a.home()
        y=10
        x=30
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(8)
        a.end_fill()
        a.penup()
        a.home()
        y=-30
        x=-30
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(8)
        a.end_fill()
        a.penup()
        a.hideturtle()


    elif(c==5):
        import turtle
        a=turtle.Turtle()
        a.screen.bgcolor("yellow")
        a.penup()
        a.forward(50)
        a.pendown()
        a.begin_fill()
        a.fillcolor("white")
        a.left(90)
        a.forward(50)
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(50)
        a.end_fill()
        a.penup()
        a.home()
        y=10
        x=-30
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(8)
        a.end_fill()
        a.penup()
        a.home()
        y=-30
        x=30
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(8)
        a.end_fill()
        a.penup()
        a.home()
        y=-12
        x=0
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(8)
        a.end_fill()
        a.penup()
        a.home()
        y=10
        x=30
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(8)
        a.end_fill()
        a.penup()
        a.home()
        y=-30
        x=-30
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(8)
        a.end_fill()
        a.penup()
        a.hideturtle()


    elif(c==6):
        import turtle
        a=turtle.Turtle()
        a.screen.bgcolor("yellow")
        a.penup()
        a.forward(50)
        a.pendown()
        a.begin_fill()
        a.fillcolor("white")
        a.left(90)
        a.forward(50)
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(100)
        a.left(90)
        a.forward(50)
        a.end_fill()
        a.penup()
        a.home()
        y=20
        x=-30
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(6)
        a.end_fill()
        a.penup()
        a.home()
        y=-20
        x=30
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(6)
        a.end_fill()
        a.penup()
        a.home()
        y=-20
        x=-30
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(6)
        a.end_fill()
        a.penup()
        a.home()
        y=20
        x=30
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(6)
        a.end_fill()
        a.penup()
        a.home()
        y=0
        x=30
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(6)
        a.end_fill()
        a.penup()
        a.home()
        y=0
        x=-30
        a.goto(x,y)
        a.pendown()
        a.begin_fill()
        a.fillcolor("black")
        a.circle(6)
        a.end_fill()
        a.penup()
        a.hideturtle()

        
    e=int(input("\n1.Continue\n2.Break"))
    if (e!=1):
        break

elif(choice==4):
    print("4.Toss A Coin")
    print("GAME START")
    head=0
    tail=0
    import random
    import matplotlib.pyplot as plt 
    con=[]
    while(1<2):
        c=random.randrange(0,2)
        if(c==0):
            print("\nHead")
            head=head+1
        else:
            print("\nTail")
            tail=tail+1
        e=int(input("\n1.Continue\n2.Break"))
        if (e!=1):
            print("Number of times\n1.Head= ",head,"\n2.Tail= ",tail)
            break
    
    con.append(head)
    con.append(tail)
    Zones=["Head","Tail"]
    plt.axis("equal")
    plt.pie(con,labels=Zones,autopct="%1.2f%%")
    plt.show()
elif(choice==5):
    print("4.Tic Tac Toe")
    print("GAME START")
    def sum(x,y,z):
        return x+y+z

    def printboard(xstate,zstate):
        zero="X" if xstate[0] else("0" if zstate[0] else '')
        one="X" if xstate[1] else("0" if zstate[1] else '')
        two="X" if xstate[2] else("0" if zstate[2] else '')
        three="X" if xstate[3] else("0" if zstate[3] else '')
        four="X" if xstate[4] else("0" if zstate[4] else '')
        five="X" if xstate[5] else("0" if zstate[5] else '')
        six="X" if xstate[6] else("0" if zstate[6] else '')
        seven="X" if xstate[7] else("0" if zstate[7] else '')
        eight="X" if xstate[8] else("0" if zstate[8] else '')

        import turtle
        a=turtle.Turtle()
        a.screen.bgcolor("yellow")
        a.hideturtle()
        #board_construction
        a.width(10)
        a.penup()
        x=-50
        y=150
        a.goto(x,y)
        a.pendown()
        a.right(90)
        a.forward(300)
        a.penup()
        x=50
        y=150
        a.goto(x,y)
        a.pendown()
        a.forward(300)
        a.left(90)
        a.penup()
        x=-150
        y=50
        a.goto(x,y)
        a.pendown()
        a.forward(300)
        a.penup()
        x=-150
        y=-50
        a.goto(x,y)
        a.pendown()
        a.forward(300)

        #heading
        a.penup()
        x=-180
        y=200
        a.goto(x,y)
        a.pendown()
        a.write('Tic tac Toe',font=('airal',50,'bold'))
 
        a.penup()
        x=-120   #0
        y=70
        a.goto(x,y)
        a.pendown()
        a.write(f"{zero}",font=('airal',50,'bold'))
        
        a.penup()
        x=-20      #1
        y=70
        a.goto(x,y)
        a.pendown()
        a.write(f"{one}",font=('airal',50,'bold'))
        
        a.penup()
        x=80      #2
        y=70
        a.goto(x,y)
        a.pendown()
        a.write(f"{two}",font=('airal',50,'bold'))

        a.penup()
        x=-120   #3
        y=-35
        a.goto(x,y)
        a.pendown()
        a.write(f"{three}",font=('airal',50,'bold'))
        
        a.penup()
        x=-20   #4
        y=-35
        a.goto(x,y)
        a.pendown()
        a.write(f"{four}",font=('airal',50,'bold'))
        
        a.penup()
        x=80   #5
        y=-35
        a.goto(x,y)
        a.pendown()
        a.write(f"{five}",font=('airal',50,'bold'))
        
        a.penup()
        x=-120   #6
        y=-140
        a.goto(x,y)
        a.pendown()
        a.write(f"{six}",font=('airal',50,'bold'))
        
        a.penup()
        x=-20    #7
        y=-140
        a.goto(x,y)
        a.pendown()
        a.write(f"{seven}",font=('airal',50,'bold'))

        a.penup()
        x=80    #8
        y=-140
        a.goto(x,y)
        a.pendown()
        a.write(f"{eight}",font=('airal',50,'bold'))
        
    def checkwin(xstate,zstate):
        wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for win in wins:
            if (sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
                printboard(xstate,zstate)
                print("X win the Match")
                return 1
            if (sum(zstate[win[0]],zstate[win[1]],zstate[win[2]])==3):
                printboard(xstate,zstate)
                print("0 win the Match")
                return 0
        return -1
    if __name__=="__main__":
        xstate=[0,0,0,0,0,0,0,0,0]
        zstate=[0,0,0,0,0,0,0,0,0]
        print("welcome to Tic Tac Toe\n")
        choice=int(input("First chance :-\n 1. For X\n 2. For 0 "))
        turn=choice
        while(True):
            printboard(xstate,zstate)
            if (turn==1):
                print("X's chance")
                value=int(input("Enter the position "))
                xstate[value]=1
            else:
                print("0's chance")
                value=int(input("Enter the position "))
                zstate[value]=1
            cwin=checkwin(xstate,zstate)
            if (cwin !=-1):
                break
            turn=1-turn
         
else:
    print("Invalid Choice")

    
