# password generator 

import random

let = ["a","b","c","d","e","f","g","h","i","j","k","l" ,"m","n","o","p","q","r","s","t","u","v","w","x","y","z", 
           "A","B","C","D","E","F","G","H","I","J","K","L","M","N"," O","P","Q","R","S","T","U","V","W","X","Y","Z" ]

nums =  ["0" ,"1", "2", "3", "4", "5", "6", "7", "8", "9" ]

sym = ["+","-", "*", "/","!",",","#","$","%","^","&","=","(",")","."]

print("PASSWORD GENERATOR")
letters = int(input("enter number of letters in  password : \n"))
numbers = int(input("enter how many number to be in password : \n"))
symbols = int(input("enter number of symbols in password : \n"))

password  = []

for char in range(1,letters+1):
    r_char = random.choice(let)
    password += r_char
   
for char in range(1,numbers+1):
    r_char = random.choice(nums)
    password += r_char
   
for char in range(1,symbols+1):
    r_char = random.choice(sym)
    password += r_char

random.shuffle(password)

aa =""
for xx in password:
        aa += xx
print(f"your new pass is \n{aa}")