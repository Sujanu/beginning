# control flow in python

# using if else 

print("Odd Even NUmber Check")
num = int(input("Enter a number: "))

if  num % 2 == 0 :
      print(f"the given number {num} is even")  
else :
     print(f"the given number {num} is odd")

# # using if elif and else
#  body mass index based in user's weight and height

print("\n \n \n")
print("body mass index based in user's weight and height")
height = float(input("Enter the height in meter: "))
weight = float(input("Enter the weight in kg: " ))

BMI = round(weight / height ** 2)

if BMI < 18.5:
      print(f"Your BMI is {BMI} , you are underweight")

elif BMI < 25:
     print(f"Your BMI is {BMI} , you have normal weight")

elif BMI <30:
     print(f"Your BMI is {BMI} , you are overweight")

elif BMI <35:
     print(f"Your BMI is {BMI} , you are obese")

else :
 print(f"Your BMI is {BMI} , you are clinically obese")

print("\n \n \n")

# leap year program

print(" leap year program")
year = int(input("enter a year: "))

if year % 4 ==0 :
    if year % 100 == 0 :
    
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else :
            print(f"{year} is not a leap year")
    
    else:
     print(f"{year} is a leap year")

else:
    print(f"{year} is  not a leap year")