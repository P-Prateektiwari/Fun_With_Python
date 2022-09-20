print("                                IT'S TIME TO PLAY                ")
print("1.Stone, Paper, Scissor")
print("2.Try Your Luck")
print("3.Ludo Dice")
print("4.Toss A Coin")
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
        e=int(input("\n1.Continue\n2.Break"))
        if (e!=1):
            break
elif(choice==4):
    print("4.Toss A Coin")
    print("GAME START")
    head=0
    tail=0
    import random
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
    else:
        print("Invalid Choice")

    
