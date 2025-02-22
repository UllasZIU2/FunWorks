
dic={}
print(f'Welcome to the secret auction program.')
while True:
    dic[input("What is your name?: " )]=int(input("What's your bid?: $"))
    bid=input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if bid=='no':
        break
    elif bid!="yes" or bid!="no":
        bid=input("Invalid input !!\nEnter valid input else biding will be finished !! Type 'yes' or 'no'.").lower()
        if bid=='no':
            break
        elif bid!="yes" or bid!="no":
            break
            
print(dic)
maxbidname=""
max=0
for i , j in dic.items():
    if j>max:
        max=j
        maxbidname=i

print(f"The winner is  {maxbidname} with a bid of {max} ")

# import atuo clear terminal after every input check day 9 of 100 days of code
# hi its me at 2025 to 2030