
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random as r
u1=int(input("Hello there welcome to rock paper scissors .\n0.Rock\n1.Paper\n2.Scissors .\nPlease enter number of Trial "))

usercount=0
cmpcount=0
movelst=[rock,paper,scissors]
for i in range(u1):
    usermove=int(input("choose your move between 0, 1 or 2 :"))
    print(f'Your move {movelst[usermove]}')
    cmpmove=r.randint(0,2)
    print(f'Computer move {movelst[cmpmove]}')
    if usermove==cmpmove:
        print("drawwwwww")
    elif usermove not in [0,1 ,2]:
        print("Invalid Input,, YOU lost the game !")
        break
    else:
        if usermove==0:
            if cmpmove==1:
                print("Better Luck NEXT TIME ")
                cmpcount+=1
            elif cmpmove==2:
                print('Congoooooooo ')
                usercount+=1
        elif usermove==1:
            if cmpmove==2:
                print("Better Luck NEXT TIME ")
                cmpcount+=1
            elif cmpmove==0:
                print('Congoooooooo ')
                usercount+=1    
        elif usermove==2:
            if cmpmove==0:
                print("Better Luck NEXT TIME ")
                cmpcount+=1
            elif cmpmove==2:
                print('Congoooooooo ')   
                usercount+=1 
    print(cmpcount, usercount)
if usercount==cmpcount:
    print("Match draw")
elif usercount>cmpcount:
    print("Hurreah,,,you won the game ")
elif usercount<cmpcount:
    print("YOU lost the game \nBetter Luck Next time")
