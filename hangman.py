import random as rm
import os
# last update 25-JUL-2024
#done this is the last day of karfiew form 16july 2024


h9="""
-------------
    |       ||
    O       ||
   /|\      ||
    |       ||
   / \      ||
  _DEAD_    ||
____________||
"""
h8="""
-------------
    |       ||
    O       ||
   /|\      ||
    |       ||
   / \      ||
            ||
____________||
"""
h7="""
-------------
    |       ||
    O       ||
   /|\      ||
    |       ||
   /        ||
            ||
____________||
"""
h6="""
-------------
    |       ||
    O       ||
   /|\      ||
    |       ||
            ||
            ||
____________||
"""
h5="""
-------------
    |       ||
    O       ||
   /|\      ||
            ||
            ||
            ||
____________||
"""
h4="""
-------------
    |       ||
    O       ||
   /|       ||
            ||
            ||
            ||
____________||
"""
h3="""
-------------
    |       ||
    O       ||
   /        ||
            ||
            ||
            ||
____________||
"""
h2="""
-------------
    |       ||
    O       ||
            ||
            ||
            ||
            ||
____________||
"""
h1="""
-------------
    |       ||
            ||
            ||
            ||
            ||
            ||
____________||
"""
h0="""
-------------
            ||
            ||
            ||
            ||
            ||
            ||
____________||
"""
os.system('cls' if os.name == 'nt' else 'clear')

slst=[h9,h8,h7,h6,h5,h4,h3,h2,h1,h0]
lst0=["book","look","cool","cook","sky","cry","apple","bed"]
lst1=["python","intiger","float","string","tuple","macbook","windows"]
lst2=["facebook","dictionary","twitter","instragram","youtube","array"]  
print(f"Choose your level\n0.Easy\n1.Medium\n2.Hard")

user=int(input("\nEnter:-"))

if user==2:
    rms=rm.choice(lst2)
elif user==1:
    rms=rm.choice(lst1)
elif user==0:
    rms=rm.choice(lst0)
else:
    print(f"Invalid input!! Starting With Easy")
    rms=rm.choice(lst0)

# print(f"{rms}")

ln=len(rms)
dashlst=[" - " for n in range(ln)]
if ln>=10:
    manlife=9
else:
    manlife=ln

def display():
    dshstr=""
    for k in dashlst:
        dshstr+=k
    return dshstr

print(f"{display()}\n[Note: if you want hint just type 'hint']\nGuess the letter to save your man .Life remaining= {manlife}")  

while True:
    userguess=input( ":-")
    if userguess in rms:
        c=0
        for i in rms:
           if i==userguess:
                dashlst[c]=i
           c+=1
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"{display()},\nYour man life remaining = {manlife}{slst[manlife]}")   
    elif userguess=="hint":
        if manlife-2>=2:
            hnt=display().find(" - ")
            dashlst[hnt]=rms[hnt]
            manlife-=2
            os.system('cls' if os.name == 'nt' else 'clear')

            print(f"hint given and 2 life taken\nYour man life remaining = {manlife} \n{display()}\n{slst[manlife]}")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Not enough life\nYour man life remaining = {manlife} \n{display()}\n{slst[manlife]}")
            
            pass

    else:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f'You guessed {userguess}  , thats not in the word. You lose a life.\nYour man life remaining = {manlife}\n{display()}{slst[manlife]}')

        manlife-=1
    if manlife ==0:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"\nYou lost !! \n{slst[manlife]}\nFailed to saved the hang-man.\nCORRECT ANSWER=> {rms}")
        break
    elif " - " not in dashlst:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(slst[manlife])
        print( rms ,"\nCongooooo !! You saved the hang-man.")
        break
    

import all_test_01 





