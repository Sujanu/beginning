# pizza order program

size = input("Enter pizza size of your choice Small(S) , Medium(M) or Large(L) \n")

bill = 0
if size == "S"  or size == "s":
    bill += 15
elif size == "M" or size == "m" :
    bill += 20
else :
    bill += 25
    
addp = input("add pepperoni ? \n Y \t N  \n")
if addp == "Y" or addp =="y" :
    if size == "S" : 
        bill += 2
    elif size == "M" :
        bill += 3
    else :
        bill += 3

addc = input("add cheese ? \n Y \t N \n") 
if addc == "Y" or addc =="y"  :
    bill += 1

print(f"your total bill is {bill}")
